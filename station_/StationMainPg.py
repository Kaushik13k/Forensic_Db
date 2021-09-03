from PyQt5 import QtCore, QtGui, QtWidgets

from StationCaseList import PolCaseList
from StationPoliceList import PoliceList
from StationPoliceRegistration import policeRegistrationPage
from StationcaseRegister import CaseRegister


class PoliceMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1405, 822)
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 1341, 771))
        self.graphicsView.setStyleSheet("background-color: rgb(233, 255, 246);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 40, 1321, 751))
        self.graphicsView_2.setStyleSheet("background-color: rgb(59, 43, 1);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.dtrReg = QtWidgets.QPushButton(self.centralwidget)
        self.dtrReg.setGeometry(QtCore.QRect(470, 160, 471, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dtrReg.setFont(font)
        self.dtrReg.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                  "")
        self.dtrReg.setObjectName("dtrReg")
        self.caseReg = QtWidgets.QPushButton(self.centralwidget)
        self.caseReg.setGeometry(QtCore.QRect(230, 360, 421, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.caseReg.setFont(font)
        self.caseReg.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "")
        self.caseReg.setObjectName("caseReg")
        self.caseList = QtWidgets.QPushButton(self.centralwidget)
        self.caseList.setGeometry(QtCore.QRect(770, 360, 421, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.caseList.setFont(font)
        self.caseList.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                    "")
        self.caseList.setObjectName("caseList")
        self.docList = QtWidgets.QPushButton(self.centralwidget)
        self.docList.setGeometry(QtCore.QRect(500, 550, 421, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.docList.setFont(font)
        self.docList.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "")
        self.docList.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dtrReg.clicked.connect(self.PoliceRegister)
        self.caseList.clicked.connect(self.casList)
        self.docList.clicked.connect(self.PloiceLis)
        self.caseReg.clicked.connect(self.CaseRegister)

    def CaseRegister(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = CaseRegister()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


    def PoliceRegister(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = policeRegistrationPage()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def casList(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = PolCaseList()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def PloiceLis(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = PoliceList()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  WELCOME"))
        self.dtrReg.setText(_translate("MainWindow", "POLICE REGISTRATION"))
        self.caseReg.setText(_translate("MainWindow", "CASE REGISTRATION"))
        self.caseList.setText(_translate("MainWindow", "CASE LIST"))
        self.docList.setText(_translate("MainWindow", "POLICE LIST"))

