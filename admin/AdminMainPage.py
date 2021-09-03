from PyQt5 import QtCore, QtGui, QtWidgets
from AdminStationRegistration import StationRegUi
from AdminHospitalRegistration import hospReg

class AdminMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 801)
        MainWindow.setMaximumSize(QtCore.QSize(1073, 801))
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(35, 31, 1001, 731))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.st_reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.st_reg_btn.setGeometry(QtCore.QRect(120, 260, 321, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.st_reg_btn.setFont(font)
        self.st_reg_btn.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.st_reg_btn.setObjectName("pushButton")
        self.hos_reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hos_reg_btn.setGeometry(QtCore.QRect(630, 260, 321, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hos_reg_btn.setFont(font)
        self.hos_reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.hos_reg_btn.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.hos_reg_btn.setObjectName("pushButton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 40, 991, 711))
        self.graphicsView_2.setStyleSheet("background-color: rgb(59, 43, 1);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.st_reg_btn.raise_()
        self.label.raise_()
        self.hos_reg_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.st_reg_btn.clicked.connect(self.StnReg)
        self.hos_reg_btn.clicked.connect(self.HospReg)

    def StnReg(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = StationRegUi()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def HospReg(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = hospReg()
        ui.setupUi(MainWindow)
        MainWindow.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.st_reg_btn.setText(_translate("MainWindow", "STATION REGISTRATION"))
        self.hos_reg_btn.setText(_translate("MainWindow", "HOSPITAL REGISTRATION"))

