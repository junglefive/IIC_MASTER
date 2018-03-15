import sys,time,os
from IIC_MASTER_ui import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from serial.tools.list_ports import *
from picture_qrc import  *
import datetime
from IIC_CH341 import *
import numpy as np


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        Ui_MainWindow.__init__(self)
        # logo
        self.setWindowIcon(QIcon(":picture/img/110.png"))
        # 默认时间戳
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')

        self.btn_cmd_write.clicked.connect(self.on_click_btn_cmd_write)
        self.btn_cmd_read.clicked.connect(self.on_click_btn_cmd_read)




    def on_click_btn_cmd_write(self):
        self.btn_cmd_write.setEnabled(False)
        self.iic_send_bytes(self.line_cmd_write.text(),True)
        self.btn_cmd_write.setEnabled(True)

    def on_click_btn_cmd_read(self):
        self.btn_cmd_read.setEnabled(False)
        self.iic_read_byte(self.line_cmd_read.text(),True,self.line_cmd_read_dis)
        self.btn_cmd_read.setEnabled(True)

    def iic_read_byte(self,hex_str,dis_success,dis_line):
        try:
            cmd_hex = hex_str.replace("0x", "")
            cmd_bytes = bytes.fromhex(cmd_hex)
            print(hex_str)
            protocol = CH341AIIC()
            print(hex(cmd_bytes[1]),hex(cmd_bytes[2]))
            address_read = (cmd_bytes[1]*256+cmd_bytes[2])
            print("read：", hex(address_read))
            result,read = protocol.read_byte(address_read)
            dis_line.setText("读取到数据："+hex(read[0]))
            if dis_success & result:
                QMessageBox.information(self, "提示", "读取成功")
            elif dis_success:
                QMessageBox.information(self, "错误", "读取失败,请检查硬件")
        except Exception as e:
            print(str(e))
            QMessageBox.information(self, "错误", "读取失败,请检查硬件" + str(e))

    def refresh_app(self):

        qApp.processEvents()

    def iic_send_bytes(self,hex_str, dis_success = False):

        try:
            cmd_hex = hex_str.replace("0x","")
            cmd_bytes = bytes.fromhex(cmd_hex)

            protocol = CH341AIIC()
            protocol.set_clk(protocol.IIC_CLK_100kHz)
            result = protocol.write_bytes(cmd_bytes)
            print(str(cmd_bytes.hex()))
            if dis_success&result:
                QMessageBox.information(self,"提示","发送成功")
            elif dis_success:
                QMessageBox.information(self, "错误", "发送失败,请检查硬件" )
        except Exception as e:
            print(str(e))
            QMessageBox.information(self,"错误","发送失败,请检查硬件"+str(e))



    def init_default_display(self):
        # size
        self.__desktop = QApplication.desktop()
        qRect = self.__desktop.screenGeometry()  # 设备屏幕尺寸
        self.resize(qRect.width() * 45/ 100, qRect.height() * 90 / 100)
        self.move(qRect.width() / 3, qRect.height() / 30)


class MainLoop(QThread):
      # const
      def  __init__(self):
          super(MainLoop, self).__init__()
      def run(self):
          pass
          try:
              # 串口工作主流程
              """主循环"""
              while True:
                pass
                time.sleep(0.1)
          except Exception as e:
                print(str(e))

      def mainloop_app(self):
          try:
              pass
              app = QtWidgets.QApplication(sys.argv)
              window = MyApp()
              window.show()
              pass
          except Exception as e:
              print(str(e))
          finally:
              sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        custum = MainLoop()
        custum.start()
        custum.mainloop_app()
    except Exception as e:
        print(str(e))
    finally:
        pass




