# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator_tracking_SendRoutingInfoForSM.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 910)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hlr_t = QtWidgets.QLineEdit(self.centralwidget)
        self.hlr_t.setGeometry(QtCore.QRect(190, 220, 311, 31))
        self.hlr_t.setObjectName("hlr_t")
        self.cip = QtWidgets.QLineEdit(self.centralwidget)
        self.cip.setGeometry(QtCore.QRect(200, 0, 301, 31))
        self.cip.setObjectName("cip")
        self.sport = QtWidgets.QLineEdit(self.centralwidget)
        self.sport.setGeometry(QtCore.QRect(200, 130, 311, 31))
        self.sport.setObjectName("sport")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 131, 21))
        self.label_3.setStyleSheet("font: 16pt \"Noto Sans\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 120, 131, 21))
        self.label_4.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 220, 201, 31))
        self.label_6.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 160, 201, 31))
        self.label_5.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.sip = QtWidgets.QLineEdit(self.centralwidget)
        self.sip.setGeometry(QtCore.QRect(200, 90, 311, 31))
        self.sip.setObjectName("sip")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(450, 700, 191, 41))
        self.run.setObjectName("run")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(501, 750, 181, 31))
        self.label_13.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_13.setObjectName("label_13")
        self.netindicator = QtWidgets.QLineEdit(self.centralwidget)
        self.netindicator.setGeometry(QtCore.QRect(200, 170, 311, 31))
        self.netindicator.setObjectName("netindicator")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 131, 21))
        self.label_2.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.cport = QtWidgets.QLineEdit(self.centralwidget)
        self.cport.setGeometry(QtCore.QRect(200, 40, 311, 41))
        self.cport.setObjectName("cport")
        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(11, 780, 1561, 191))
        self.output.setObjectName("output")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 270, 1571, 20))
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 151, 21))
        self.label.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 300, 551, 391))
        self.tableView.setObjectName("tableView")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(20, 440, 201, 31))
        self.label_25.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_25.setObjectName("label_25")
        self.smsc = QtWidgets.QLineEdit(self.centralwidget)
        self.smsc.setGeometry(QtCore.QRect(230, 440, 311, 31))
        self.smsc.setObjectName("smsc")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 360, 201, 31))
        self.label_10.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_10.setObjectName("label_10")
        self.msc = QtWidgets.QLineEdit(self.centralwidget)
        self.msc.setGeometry(QtCore.QRect(210, 360, 311, 31))
        self.msc.setObjectName("msc")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(250, 300, 201, 31))
        self.label_14.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_14.setObjectName("label_14")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(620, 300, 591, 391))
        self.tableView_2.setObjectName("tableView_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(810, 300, 181, 31))
        self.label_12.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_12.setObjectName("label_12")
        self.imsi = QtWidgets.QLineEdit(self.centralwidget)
        self.imsi.setGeometry(QtCore.QRect(820, 410, 311, 31))
        self.imsi.setObjectName("imsi")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 410, 201, 31))
        self.label_9.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 220, 201, 31))
        self.label_7.setStyleSheet("font: 16pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.msisdn = QtWidgets.QLineEdit(self.centralwidget)
        self.msisdn.setGeometry(QtCore.QRect(710, 220, 311, 31))
        self.msisdn.setObjectName("msisdn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "simulator_tracking_SendRoutingInfoForSM"))
        self.hlr_t.setText(_translate("MainWindow", "(i.e 201179008255)"))
        self.cip.setText(_translate("MainWindow", "(i.e 192.168.56.101)"))
        self.sport.setText(_translate("MainWindow", "(i.e 2906)"))
        self.label_3.setText(_translate("MainWindow", "server_ip"))
        self.label_4.setText(_translate("MainWindow", "server_port"))
        self.label_6.setText(_translate("MainWindow", "Targer_HLR"))
        self.label_5.setText(_translate("MainWindow", "Network_Indicator"))
        self.sip.setText(_translate("MainWindow", "(i.e 192.168.56.102)"))
        self.run.setText(_translate("MainWindow", "run"))
        self.label_13.setText(_translate("MainWindow", "Output"))
        self.netindicator.setText(_translate("MainWindow", "(i.e 0)"))
        self.label_2.setText(_translate("MainWindow", "client_port"))
        self.cport.setText(_translate("MainWindow", "(i.e 2905)"))
        self.label_11.setText(_translate("MainWindow", "_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.label.setText(_translate("MainWindow", "client_ip"))
        self.label_25.setText(_translate("MainWindow", "Targer_SMSC"))
        self.smsc.setText(_translate("MainWindow", "(i.e 201012344323)"))
        self.label_10.setText(_translate("MainWindow", "Targer_MSC"))
        self.msc.setText(_translate("MainWindow", "(i.e 201012344321)"))
        self.label_14.setText(_translate("MainWindow", "Attacker"))
        self.label_12.setText(_translate("MainWindow", "Simulator"))
        self.imsi.setText(_translate("MainWindow", "(i.e 602027891234567)"))
        self.label_9.setText(_translate("MainWindow", "Targer_IMSI"))
        self.label_7.setText(_translate("MainWindow", "Targer_MSISDN"))
        self.msisdn.setText(_translate("MainWindow", "(i.e 201179008255)"))

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


        Targer_MSISDN = str(self.msisdn.text()).replace(")","").replace("(","")

        Targer_HLR = str(self.hlr_t.text()).replace(")","").replace("(","")

        Targer_IMSI = str(self.imsi.text()).replace(")","").replace("(","")
        if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
            from PyQt5.QtWidgets import  QPushButton, QMessageBox
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("IMSI len should be 15 or 16")
            msgBox.setWindowTitle("IMSI Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            exit(0)

        Targer_MSC = str(self.msc.text()).replace(")","").replace("(","")
        Targer_SMSC = str(self.smsc.text()).replace(")","").replace("(","")


        

        ts_gui.simulator_tracking_SendRoutingInfoForSM(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_MSISDN,Targer_MSC,Targer_SMSC)
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
