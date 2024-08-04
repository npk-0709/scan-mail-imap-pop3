"""
 * Author: NGUYEN PHU KHUONG (K.AUTO) 
 * Email: dev.phukhuong0709@hotmail.com
 * Github: npk-0709
 * TELE: @khuongdev79
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 210)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 201, 16))
        self.label.setObjectName("label")
        self.btnEvent = QtWidgets.QPushButton(self.centralwidget)
        self.btnEvent.setGeometry(QtCore.QRect(180, 100, 171, 41))
        self.btnEvent.setObjectName("btnEvent")
        self.count = QtWidgets.QSpinBox(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(290, 70, 71, 22))
        self.count.setObjectName("count")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 65, 91, 31))
        self.label_2.setObjectName("label_2")
        self.account = QtWidgets.QLineEdit(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(150, 40, 231, 20))
        self.account.setObjectName("account")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TOOL ĐỌC HOTMAIL - IMAP"))
        self.btnEvent.setText(_translate("MainWindow", "CHẠY"))
        self.label_2.setText(_translate("MainWindow", "SỐ LƯỢNG"))
        self.account.setPlaceholderText(_translate("MainWindow", "USERNAME |  PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
