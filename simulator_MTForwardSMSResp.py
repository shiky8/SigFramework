# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator_MTForwardSMSResp.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 922)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cip = QtWidgets.QLineEdit(self.centralwidget)
        self.cip.setGeometry(QtCore.QRect(200, 20, 301, 31))
        self.cip.setObjectName("cip")
        self.cport = QtWidgets.QLineEdit(self.centralwidget)
        self.cport.setGeometry(QtCore.QRect(200, 60, 311, 41))
        self.cport.setObjectName("cport")
        self.sip = QtWidgets.QLineEdit(self.centralwidget)
        self.sip.setGeometry(QtCore.QRect(200, 110, 311, 31))
        self.sip.setObjectName("sip")
        self.sport = QtWidgets.QLineEdit(self.centralwidget)
        self.sport.setGeometry(QtCore.QRect(200, 150, 311, 31))
        self.sport.setObjectName("sport")
        self.netindicator = QtWidgets.QLineEdit(self.centralwidget)
        self.netindicator.setGeometry(QtCore.QRect(200, 190, 311, 31))
        self.netindicator.setObjectName("netindicator")
        self.msc = QtWidgets.QLineEdit(self.centralwidget)
        self.msc.setGeometry(QtCore.QRect(200, 230, 311, 41))
        self.msc.setObjectName("msc")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 151, 21))
        self.label.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 131, 21))
        self.label_2.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 131, 21))
        self.label_3.setStyleSheet("font: 16pt \"Noto Sans\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 140, 131, 21))
        self.label_4.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 180, 201, 31))
        self.label_5.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 230, 181, 31))
        self.label_6.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 300, 131, 31))
        self.label_8.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 360, 131, 31))
        self.label_9.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_9.setObjectName("label_9")
        self.imsi = QtWidgets.QLineEdit(self.centralwidget)
        self.imsi.setGeometry(QtCore.QRect(150, 360, 461, 51))
        self.imsi.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.imsi.setObjectName("imsi")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 430, 121, 21))
        self.label_10.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_10.setObjectName("label_10")
        self.locael_gt = QtWidgets.QLineEdit(self.centralwidget)
        self.locael_gt.setGeometry(QtCore.QRect(150, 420, 451, 41))
        self.locael_gt.setObjectName("locael_gt")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(-10, 280, 1151, 20))
        self.label_11.setObjectName("label_11")
        self.smsc_gt = QtWidgets.QLineEdit(self.centralwidget)
        self.smsc_gt.setGeometry(QtCore.QRect(150, 470, 461, 51))
        self.smsc_gt.setObjectName("smsc_gt")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 470, 111, 31))
        self.label_12.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(0, 530, 151, 31))
        self.label_13.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_13.setObjectName("label_13")
        self.sender_name = QtWidgets.QLineEdit(self.centralwidget)
        self.sender_name.setGeometry(QtCore.QRect(150, 530, 471, 41))
        self.sender_name.setObjectName("sender_name")
        self.sms_conet = QtWidgets.QLineEdit(self.centralwidget)
        self.sms_conet.setGeometry(QtCore.QRect(150, 580, 471, 41))
        self.sms_conet.setObjectName("sms_conet")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(0, 580, 151, 41))
        self.label_14.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_14.setObjectName("label_14")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(310, 640, 181, 41))
        self.run.setObjectName("run")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 690, 141, 31))
        self.label_7.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(0, 740, 1131, 131))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "simulator_MTForwardSMSResp"))
        self.cip.setText(_translate("MainWindow", "(i.e 192.168.56.101)"))
        self.cport.setText(_translate("MainWindow", "(i.e 2905)"))
        self.sip.setText(_translate("MainWindow", "(i.e 192.168.56.102)"))
        self.sport.setText(_translate("MainWindow", "(i.e 2906)"))
        self.netindicator.setText(_translate("MainWindow", "(i.e 0)"))
        self.msc.setText(_translate("MainWindow", "(i.e 201512345678)"))
        self.label.setText(_translate("MainWindow", "client_ip"))
        self.label_2.setText(_translate("MainWindow", "client_port"))
        self.label_3.setText(_translate("MainWindow", "server_ip"))
        self.label_4.setText(_translate("MainWindow", "server_port"))
        self.label_5.setText(_translate("MainWindow", "Network_Indicator"))
        self.label_6.setText(_translate("MainWindow", "Target_MSC"))
        self.label_8.setText(_translate("MainWindow", "Attacker"))
        self.label_9.setText(_translate("MainWindow", "Target_IMSI"))
        self.imsi.setText(_translate("MainWindow", "(i.e 602027891234567)"))
        self.label_10.setText(_translate("MainWindow", "locael_GT"))
        self.locael_gt.setText(_translate("MainWindow", "(i.e 999599)"))
        self.label_11.setText(_translate("MainWindow", "________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.smsc_gt.setText(_translate("MainWindow", "(i.e 595999)"))
        self.label_12.setText(_translate("MainWindow", "SMSC_GT"))
        self.label_13.setText(_translate("MainWindow", "Sender_Name"))
        self.sender_name.setText(_translate("MainWindow", "(i.e Facebook"))
        self.sms_conet.setText(_translate("MainWindow", "Enter SMS Content in one string (i.e hi_shiky)"))
        self.label_14.setText(_translate("MainWindow", "SMS_Content"))
        self.run.setText(_translate("MainWindow", "run"))
        self.label_7.setText(_translate("MainWindow", "output"))

        self.run.clicked.connect(self.runing)
 
    
    def runing(self):
        import test_gui_web as ts_gui
        import os
        import subprocess as sp

        client_ip = str(self.cip.text()).replace(")","").replace("(","")
        client_port = str(self.cport.text()).replace(")","").replace("(","")
        server_ip = str(self.sip.text()).replace(")","").replace("(","")
        server_port = str(self.sport.text()).replace(")","").replace("(","")
        Network_Indicator = str(self.netindicator.text()).replace(")","").replace("(","")

     
        Target_MSC = str(self.msc.text()).replace(")","").replace("(","")

        Target_IMSI = str(self.imsi.text()).replace(")","").replace("(","")
        if(len(Target_IMSI) < 15 or len(Target_IMSI) > 16):
            from PyQt5.QtWidgets import  QPushButton, QMessageBox
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("IMSI len should be 15 or 16")
            msgBox.setWindowTitle("IMSI Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            exit(0)

        locael_GT = str(self.locael_gt.text()).replace(")","").replace("(","")
        SMSC_GT = str(self.smsc_gt.text()).replace(")","").replace("(","")
        Sender_Name = str(self.sender_name.text()).replace(")","").replace("(","")
        SMS_Content = str(self.sms_conet.text()).replace(")","").replace("(","")

        # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_MSC+" "+Target_IMSI+" "+locael_GT+" "+SMSC_GT+" "+Sender_Name+" "+SMS_Content)

        ts_gui.simulator_MTForwardSMSResp(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_MSC,Target_IMSI,locael_GT,SMSC_GT,Sender_Name,SMS_Content)
        data = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
        self.output.append(str(data))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
