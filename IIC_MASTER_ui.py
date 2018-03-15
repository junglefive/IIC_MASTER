# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IIC_MASTER.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(787, 242)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout = QtWidgets.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.line_cmd_write = QtWidgets.QLineEdit(self.tab)
        self.line_cmd_write.setEnabled(True)
        self.line_cmd_write.setAccessibleDescription("")
        self.line_cmd_write.setObjectName("line_cmd_write")
        self.horizontalLayout_22.addWidget(self.line_cmd_write)
        self.btn_cmd_write = QtWidgets.QPushButton(self.tab)
        self.btn_cmd_write.setAccessibleDescription("")
        self.btn_cmd_write.setObjectName("btn_cmd_write")
        self.horizontalLayout_22.addWidget(self.btn_cmd_write)
        self.horizontalLayout_22.setStretch(0, 6)
        self.horizontalLayout_22.setStretch(1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_22)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_cmd_read = QtWidgets.QLineEdit(self.tab)
        self.line_cmd_read.setEnabled(True)
        self.line_cmd_read.setAccessibleDescription("")
        self.line_cmd_read.setObjectName("line_cmd_read")
        self.horizontalLayout_3.addWidget(self.line_cmd_read)
        self.line_cmd_read_dis = QtWidgets.QLineEdit(self.tab)
        self.line_cmd_read_dis.setObjectName("line_cmd_read_dis")
        self.horizontalLayout_3.addWidget(self.line_cmd_read_dis)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_3)
        self.btn_cmd_read = QtWidgets.QPushButton(self.tab)
        self.btn_cmd_read.setAccessibleDescription("")
        self.btn_cmd_read.setObjectName("btn_cmd_read")
        self.horizontalLayout_18.addWidget(self.btn_cmd_read)
        self.horizontalLayout_18.setStretch(0, 6)
        self.horizontalLayout_18.setStretch(1, 1)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_18)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_14.raise_()
        self.label_19.raise_()
        self.comboBox.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IIC_Master"))
        self.label_19.setText(_translate("MainWindow", "自定义写命令（写一个Byte）"))
        self.line_cmd_write.setText(_translate("MainWindow", "0xA0 0x10 0x58 0xAA"))
        self.btn_cmd_write.setToolTip(_translate("MainWindow", "硬件地址+发送数据地址+发送数据"))
        self.btn_cmd_write.setText(_translate("MainWindow", "发送"))
        self.label_14.setText(_translate("MainWindow", "自定义读命令（读取一个byte）"))
        self.line_cmd_read.setText(_translate("MainWindow", "0xA0 0x10 0x58"))
        self.btn_cmd_read.setToolTip(_translate("MainWindow", "硬件地址+读取数据地址"))
        self.btn_cmd_read.setText(_translate("MainWindow", "读取"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "命令区（功能）"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:16pt; font-weight:600;\">注意事项</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:16pt;\"> </span><span style=\" font-family:\'Consolas\'; font-size:12pt;\">    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:16pt; font-weight:600;\">    1</span><span style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600;\">.</span><span style=\" font-family:\'Simsum\'; font-size:12pt; color:#000000;\"> 可能需要安装微软官方C++类库:</span><a href=\" https://www.microsoft.com/en-us/download/details.aspx?id=48145\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.microsoft.com/en-us/download/details.aspx?id=48145</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas\';\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "帮助/使用手册"))

