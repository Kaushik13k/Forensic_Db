import sys

import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from HospitalMainPg import HospitalMainWindow
from admin.global_variables import GlobalStatic


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 309)
        # ----
        MainWindow.setMaximumSize(QtCore.QSize(636, 309))
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 80, 591, 201))
        self.graphicsView.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "border: 3px solid white;\n"
                                        "")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 30, 281, 51))
        self.graphicsView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 35, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_user.setGeometry(QtCore.QRect(60, 130, 291, 41))
        self.txt_user.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.txt_user.setObjectName("lineEdit")
        self.txt_passw = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_passw.setGeometry(QtCore.QRect(60, 220, 291, 41))
        self.txt_passw.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.txt_passw.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "border: 3px solid gray;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.LoginHospital)

    def mainPage(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = HospitalMainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HOSPITAL LOGIN"))
        self.label_2.setText(_translate("MainWindow", "  USERNAME"))
        self.label_3.setText(_translate("MainWindow", "  PASSWORD"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))

    def LoginHospital(self):

        msg = QMessageBox()
        username = self.txt_user.text()
        password = self.txt_passw.text()

        if username == "" or password == "":
            msg.setText('Dont Leave Any Blank Spaces')
            msg.setWindowTitle("WARNING")
            msg.exec_()
            # app.quit()
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                    "Database=forensic;"
                    "Trusted_Connection=yes;"
                )
                cur = conn.cursor()
                cur.execute("select * from hospital where h_email=? and h_password=?",
                            (username, password))
                hospital_tuple = cur.fetchone()
                print(hospital_tuple)

                GlobalStatic.set_hospital_id(hospital_tuple[0])
                if hospital_tuple == None:
                    msg.setText("Invalid Username or Password")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                    # app.quit()
                else:
                    self.mainPage()
                    msg.setText("Welcome!!")
                    msg.setWindowTitle("Success")
                    msg.exec_()
                conn.close()
            except Exception as es:
                msg.setText(f"Error Due To : {str(es)}")
                msg.setWindowTitle("WARNING")
                msg.exec_()
                # app.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
