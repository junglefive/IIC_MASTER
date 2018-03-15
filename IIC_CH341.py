from ctypes import *
import time
import numpy as np


# 注意：写最大29byte，读最大32byte
# 注意：写最大29byte，读最大32byte
# 注意：写最大29byte，读最大32byte
def write_address_byte(ch_341_index,ch341dll,dev_addr,self_address,write_byte):
    result = False
    try:
        s1 = bytes((np.hstack(([dev_addr],self_address,[write_byte]))).tolist())
        result = ch341dll.IIC_WriteBytesAck(ch_341_index,len(s1),s1)
        # print(str(result)+" send:"+ " ".join('{:02x}'.format(x) for x in s1))
    except Exception as e:
        raise Exception("write_address_byte:写数据异常"+str(e))
    finally:
        return result


def write_address_bytes(ch_341_index,ch341dll,dev_addr,self_address,write_bytes):

    result = False
    try:
        s1 = np.hstack(([dev_addr],self_address,write_bytes))
        s1 = s1.tolist()
        s1 = bytes(s1)
        # print("send: "+str(s1))
        result = ch341dll.IIC_WriteBytesAck(ch_341_index,len(s1),s1)
        # print(str(result)+" send:"+ " ".join('{:02x}'.format(x) for x in s1))
    except Exception as e:
        raise Exception("write_address_bytes:写数据异常"+str(e))
    finally:
        return result

def write_iic_bytes(ch_341_index,ch341dll,write_bytes):
    result = False
    try:
        s1 = bytes(write_bytes)
        # print("输出:",len(s1))
        result = ch341dll.IIC_WriteBytesAck(ch_341_index,len(s1),s1)
        # print(str(result)+" send:"+ " ".join('{:02x}'.format(x) for x in s1))
    except Exception as e:
        raise Exception("write_bytes:写数据异常"+str(e))
    finally:
        return result

def read_address_byte(ch_341_index,ch341dll, dev_addr, self_addr):
    result = False
    try:
        s1 = bytes((np.hstack(([dev_addr],self_addr))).tolist())
        s2 = bytes([0xFF])
        result = ch341dll.IIC_WriteBytesAckReadByteAck(ch_341_index,len(s1),s1,dev_addr+1,s2)
        # print(str(result)+" send:"+" ".join('{:02x}'.format(x) for x in s1)+"->read:"+" ".join('{:02x}'.format(x) for x in s2))
    except Exception as e:
        raise Exception("read_address_byte:写数据异常"+str(e))
    finally:
        return  result,s2

def read_address_bytes(ch_341_index,ch341dll,dev_addr,self_address,length):
    result = False
    try:
        s1 = bytes((np.hstack(([dev_addr],self_address))).tolist())
        s2 = bytes(bytearray(512))
        result = ch341dll.IIC_WriteBytesAckReadBytesAck(ch_341_index,len(s1),s1,dev_addr+1,length,s2)
        print(str(bool(result))+"-recieve %s bytes:"+" ".join('{:02x}'.format(x) for x in s2[0:length])%(length))
    except Exception as e:
        raise Exception(("连续读数据异常"+str(e)))
    finally:
        return result, s2[0:length]

def reset_io_D0(ch_341_index, ch341dll, s):

    ch341dll.CH341IICOpenDevice(ch_341_index)
    ch341dll.CH341IICSet_D5_D0(ch_341_index,0x01,0x00)
    time.sleep(s)
    ch341dll.CH341IICSet_D5_D0(ch_341_index,0x01,0xff)
    ch341dll.CH341IICCloseDevice(ch_341_index)
    return True

def get_input_D7(ch_341_index,ch341dll):

    status = bytes([0xff,0xff])
    ch341dll.CH341IICOpenDevice(ch_341_index)
    ch341dll.CH341IICSet_Output(ch_341_index,0x04,0x01,0xff)
    result = ch341dll.CH341IICGet_Input(ch_341_index,status)
    ch341dll.CH341IICCloseDevice(ch_341_index)
    # print(str(result),hex(status[0]))
    return status[0]&0x80 == 0x80

def set_clk(ch_341_index, ch341dll,clk_freq):

    ch341dll.CH341IICOpenDevice(ch_341_index)
    res = ch341dll.CH341IICSetStream(ch_341_index,clk_freq)
    ch341dll.CH341IICCloseDevice(ch_341_index)
    return(res)

class CH341AIIC(object):
    """docstring for CH341AIIC"""
    ch341dll = None
    device = 0xA0 #從機地址
    ch_index = 0     #
    IIC_CLK_20kHz = 0x00
    IIC_CLK_100kHz =0x01 #default
    IIC_CLK_400kHz =0x02
    IIC_CLK_750kHz =0x03
    def __init__(self, index = 0x00):
        super(CH341AIIC, self).__init__()
        self.index = index
        try:
            self.ch341dll = cdll.LoadLibrary("./dll/CH341_IIC.DLL")
        except Exception as e:
            raise Exception("CH341_IIC.DLL异常,请检查模块是否正确连接.")
    def write_byte(self, address,byte):

        address &= 0xffff
        address_high = address>>8
        address_low  = address&0xff
        return write_address_byte(self.index, self.ch341dll,self.device, [address_high,address_low],byte)

    def write_iap_bytes(self, address, array_bytes):
        # print("write_iap_bytes"+str(array_bytes))
        address &= 0xffff
        address_high = address >> 8
        address_low = address & 0xff
        return write_address_bytes(self.index, self.ch341dll, self.device, [address_high, address_low], array_bytes)

    def write_bytes(self, array_bytes):

        return write_iic_bytes(self.index, self.ch341dll, array_bytes)


    def read_byte(self,address):
        address &= 0xffff
        address_high = address>>8
        address_low  = address&0xff
        return read_address_byte(self.index, self.ch341dll, self.device, [address_high,address_low])

    def read_bytes(self,address,length):
        address &= 0xffff
        address_high = address>>8
        address_low  = address&0xff
        return read_address_bytes(self.index,self.ch341dll,self.device,[address_high,address_low],length)

    def reset_io_D0(self, second):

        return reset_io_D0(self.index, self.ch341dll, second)

    def get_input_D7(self):

        return get_input_D7(self.index,self.ch341dll)

    def set_clk(self, clk):

        return set_clk(self.index,self.ch341dll, clk)


if __name__ == '__main__':
    result = False
    ret = False
    # ch341dll = cdll.LoadLibrary("./dll/CH341_IIC.DLL")
    print("函数库测试中.....")
    protocol = CH341AIIC()
    # protocol.reset_io_D0(0.001)
    # time.sleep(0.10)
    # ret = protocol.set_clk(protocol.IIC_CLK_400kHz)
    # address_write = 0x1058
    # print("写起始地址：",hex(address_write))
    # print("write:")
    # for i in range(32):
    #     ret = protocol.write_byte(address_write+i,2*i)
    #     if ret == True:
    #         print(str(i),end= ' ')
    # print(' ')
    # address_read = 0x1060
    # ret = protocol.set_clk(protocol.IIC_CLK_750kHz)

    # print("逐个读地址：",hex(address_read))
    # for i in range(32):
    #     ret = protocol.read_byte(address_read+i)
    #     if ret[0] == True:
    #         for x in ret[1]:
    #             print(str(x),end=' ')
    #     else:
    #         print(' ,')
    # print(' ')
    # print("读起始地址：",hex(address_read))
    # ret = protocol.read_bytes(address_read,32)
    # print("read:")
    # protocol.reset_io_D0(0.001)
    # if ret[0] == True:
    #     for x in ret[1]:
    #         print(str(x),end=' ')
    #     print(" ")
    #     print("读取成功")
    # else:
    #     print("读取失败")
    # print("测试结束,按任意键退出")
    # print("D7:",protocol.get_input_D7())
    # out = bytearray(512)
    # out[0]=0xA0
    # out[1]=0xA1
    # out[2]=0xA2
    # out[320]=0xA2
    # out[511]=0xAA
    # protocol.reset_io_D0(0.001)
    # result= protocol.write_bytes(out)
    # protocol.reset_io_D0(0.001)
    # print(str(result))
    # input()
    protocol.reset_io_D0(0.01)
    res,ret = protocol.read_bytes(0xEC00,512)
    protocol.reset_io_D0(0.01)
    print((ret.hex()))
    input()







