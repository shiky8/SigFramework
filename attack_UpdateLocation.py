# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attack_UpdateLocation.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 724)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sport = QtWidgets.QLineEdit(self.centralwidget)
        self.sport.setGeometry(QtCore.QRect(200, 130, 311, 31))
        self.sport.setObjectName("sport")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 131, 21))
        self.label_3.setStyleSheet("font: 16pt \"Noto Sans\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 151, 21))
        self.label.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 120, 131, 21))
        self.label_4.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.cport = QtWidgets.QLineEdit(self.centralwidget)
        self.cport.setGeometry(QtCore.QRect(200, 40, 311, 41))
        self.cport.setObjectName("cport")
        self.cip = QtWidgets.QLineEdit(self.centralwidget)
        self.cip.setGeometry(QtCore.QRect(200, 0, 301, 31))
        self.cip.setObjectName("cip")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 160, 201, 31))
        self.label_5.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 131, 21))
        self.label_2.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.sip = QtWidgets.QLineEdit(self.centralwidget)
        self.sip.setGeometry(QtCore.QRect(200, 90, 311, 31))
        self.sip.setObjectName("sip")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 470, 181, 31))
        self.label_13.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_13.setObjectName("label_13")
        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(1, 500, 1181, 191))
        self.output.setObjectName("output")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(440, 420, 191, 41))
        self.run.setObjectName("run")
        self.netindicator = QtWidgets.QLineEdit(self.centralwidget)
        self.netindicator.setGeometry(QtCore.QRect(200, 170, 311, 31))
        self.netindicator.setObjectName("netindicator")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 220, 201, 31))
        self.label_6.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.imsi = QtWidgets.QLineEdit(self.centralwidget)
        self.imsi.setGeometry(QtCore.QRect(190, 220, 311, 31))
        self.imsi.setObjectName("imsi")
        self.imsi_mgt = QtWidgets.QLineEdit(self.centralwidget)
        self.imsi_mgt.setGeometry(QtCore.QRect(190, 270, 311, 31))
        self.imsi_mgt.setObjectName("imsi_mgt")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 270, 201, 31))
        self.label_8.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(0, 370, 201, 31))
        self.label_14.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_14.setObjectName("label_14")
        self.locael_vlr = QtWidgets.QLineEdit(self.centralwidget)
        self.locael_vlr.setGeometry(QtCore.QRect(190, 370, 311, 31))
        self.locael_vlr.setObjectName("locael_vlr")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(0, 320, 201, 31))
        self.label_15.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_15.setObjectName("label_15")
        self.locael_gt = QtWidgets.QLineEdit(self.centralwidget)
        self.locael_gt.setGeometry(QtCore.QRect(190, 320, 311, 31))
        self.locael_gt.setObjectName("locael_gt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attacker_UpdateLocation"))
        self.sport.setText(_translate("MainWindow", "(i.e 2906)"))
        self.label_3.setText(_translate("MainWindow", "server_ip"))
        self.label.setText(_translate("MainWindow", "client_ip"))
        self.label_4.setText(_translate("MainWindow", "server_port"))
        self.cport.setText(_translate("MainWindow", "(i.e 2905)"))
        self.cip.setText(_translate("MainWindow", "(i.e 192.168.56.101)"))
        self.label_5.setText(_translate("MainWindow", "Network_Indicator"))
        self.label_2.setText(_translate("MainWindow", "client_port"))
        self.sip.setText(_translate("MainWindow", "(i.e 192.168.56.102)"))
        self.label_13.setText(_translate("MainWindow", "Output"))
        self.run.setText(_translate("MainWindow", "run"))
        self.netindicator.setText(_translate("MainWindow", "(i.e 0)"))
        self.label_6.setText(_translate("MainWindow", "Target_IMSI"))
        self.imsi.setText(_translate("MainWindow", "i.e 602027891234567)"))
        self.imsi_mgt.setText(_translate("MainWindow", "(i.e 20107891234567)"))
        self.label_8.setText(_translate("MainWindow", "Targer_IMSI_MGT"))
        self.label_14.setText(_translate("MainWindow", "locael_vlr"))
        self.locael_vlr.setText(_translate("MainWindow", "(i.e 96512345678)"))
        self.label_15.setText(_translate("MainWindow", "locael_GT"))
        self.locael_gt.setText(_translate("MainWindow", "(i.e 96512345678)"))

        self.run.clicked.connect(self.runing)

    def runing(self):
        import attack_gui_web as atck_gui
        import os
        import subprocess as sp

        client_ip = str(self.cip.text()).replace(")","").replace("(","")
        client_port = str(self.cport.text()).replace(")","").replace("(","")
        server_ip = str(self.sip.text()).replace(")","").replace("(","")
        server_port = str(self.sport.text()).replace(")","").replace("(","")
        Network_Indicator = str(self.netindicator.text()).replace(")","").replace("(","")

        locael_GT = str(self.locael_gt.text()).replace(")","").replace("(","")

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

     
        Targer_IMSI_MGT = str(self.imsi_mgt.text()).replace(")","").replace("(","")

        
        locael_vlr2 = str(self.locael_vlr.text()).replace(")","").replace("(","")

        

        atck_gui.attack_UpdateLocation(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_IMSI,Targer_IMSI_MGT,locael_GT,locael_vlr2)
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
