import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from admin.global_variables import GlobalStatic, DbConnector


class PoliceEvidance(object):
    def __init__(self):
        self.evidence_list = None

    def setupUi(self, MainWindow):
        print(f"Setting up UI")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1166, 891)
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 1091, 841))
        self.graphicsView.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "border: 3px solid white;")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 50, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.cs_id = QtWidgets.QLabel(self.centralwidget)
        self.cs_id.setGeometry(QtCore.QRect(130, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cs_id.setFont(font)
        self.cs_id.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.cs_id.setObjectName("cs_id")
        self.body = QtWidgets.QLabel(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(670, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.body.setFont(font)
        self.body.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.body.setObjectName("body")
        self.weapon = QtWidgets.QLabel(self.centralwidget)
        self.weapon.setGeometry(QtCore.QRect(130, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.weapon.setFont(font)
        self.weapon.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.weapon.setObjectName("weapon")
        self.fl_type = QtWidgets.QLabel(self.centralwidget)
        self.fl_type.setGeometry(QtCore.QRect(670, 350, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fl_type.setFont(font)
        self.fl_type.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.fl_type.setObjectName("fl_type")
        self.assignHospital = QtWidgets.QLabel(self.centralwidget)
        self.assignHospital.setGeometry(QtCore.QRect(460, 580, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assignHospital.setFont(font)
        self.assignHospital.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.assignHospital.setObjectName("assignHospital")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(450, 760, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Submit.setObjectName("Submit")

        print(f"UI setup finished. Data is: {GlobalStatic.evi_upd_info_tuple}")
        # crime_ = GlobalStatic.evi_upd_info_tup
        # le[0] if GlobalStatic.evi_upd_info_tuple else ""

        try:
            conn = DbConnector.get_connection()
            cur = conn.cursor()

            print("Got connection")
        except Exception as e:
            print(f"Error getting cursor: {e}")

        if GlobalStatic.evi_upd_info_tuple:
            case_evidence = GlobalStatic.evi_upd_info_tuple

            case_id = GlobalStatic.evi_upd_info_tuple[0]

            print(f"Querying evidence for case id: {case_id}")
            cur.execute("SELECT * FROM evidence_ WHERE c_id=?", (case_id,))
            self.evidence_list = cur.fetchall()

            print(f"Evidence for {case_id} is {self.evidence_list}")
            conn.commit()

            if self.evidence_list:

                print(f"Case evidence is: {case_evidence}")

                self.Submit.setText("Update")
                # case_id = self.evidence_list[0][0]
                body = self.evidence_list[0][1]
                weapon = self.evidence_list[0][3]
                fluid_type = self.evidence_list[0][5]
                personal_belongings = self.evidence_list[0][7]

                print(f"Values are: {case_id}, {body}, {weapon}, {fluid_type}, {personal_belongings}")
            else:
                # case_id = ""
                body = ""
                weapon = ""
                fluid_type = ""
                personal_belongings = ""
                self.Submit.setText("Insert")
                print("Else part")

        print("Processing ui")
        self.Case_id = QtWidgets.QLineEdit(self.centralwidget)
        self.Case_id.setGeometry(QtCore.QRect(130, 210, 231, 41))
        self.Case_id.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Case_id.setObjectName("Case_id")
        self.Case_id.setText(case_id)
        # self.Case_id.insertPlainText(case_id)

        self.Body = QtWidgets.QTextEdit(self.centralwidget)
        self.Body.setGeometry(QtCore.QRect(670, 200, 291, 101))
        self.Body.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Body.setObjectName("Body")

        if body:
            self.Body.setText(body)

        self.weapon_ = QtWidgets.QTextEdit(self.centralwidget)
        self.weapon_.setGeometry(QtCore.QRect(130, 390, 291, 101))
        self.weapon_.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.weapon_.setObjectName("weapon_")
        if weapon:
            self.weapon_.setText(weapon)

        self.Fluid = QtWidgets.QTextEdit(self.centralwidget)
        self.Fluid.setGeometry(QtCore.QRect(670, 390, 291, 101))
        self.Fluid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Fluid.setObjectName("Fluid")

        if fluid_type:
            self.Fluid.setText(fluid_type)

        self.personal_ = QtWidgets.QTextEdit(self.centralwidget)
        self.personal_.setGeometry(QtCore.QRect(420, 620, 291, 101))
        self.personal_.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.personal_.setObjectName("personal_")

        if personal_belongings:
            self.personal_.setText(personal_belongings)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "        Add Evidance"))
        self.cs_id.setText(_translate("MainWindow", "   Case_id"))
        self.body.setText(_translate("MainWindow", "   Body"))
        self.weapon.setText(_translate("MainWindow", "   Weapon"))
        self.fl_type.setText(_translate("MainWindow", "Fluid Type"))
        self.assignHospital.setText(_translate("MainWindow", "   Personal Belongings"))
        # self.Submit.setText(_translate("MainWindow", "Update"))
        self.Submit.clicked.connect(self.update_data)

    #
    def update_data(self):
        msg = QMessageBox()

        try:
            conn = DbConnector.get_connection()
            cur = conn.cursor()

            print("Got connection and cursor.")
            if self.evidence_list:
                cur.execute(
                    "UPDATE evidence_ SET body=?, weapon=?, fluid_type = ?,personal_belongings = ? where c_id=?",
                    (
                        self.Body.toPlainText(),
                        self.weapon_.toPlainText(),
                        self.Fluid.toPlainText(),
                        self.personal_.toPlainText(),
                        self.Case_id.text(),
                    ))
                conn.commit()
                print("Executed update query")
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"Successfully Updated")
                msg.setWindowTitle("Success")
                msg.exec_()

            else:
                cur.execute("INSERT INTO evidence_(c_id,body,weapon,fluid_type,personal_belongings) VALUES(?,?,?,?,?)",
                            (self.Case_id.text(),
                             self.Body.toPlainText(),
                             self.weapon_.toPlainText(),
                             self.Fluid.toPlainText(),
                             self.personal_.toPlainText()
                             ))
                print("Executed insert query.")
                conn.commit()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"Successfully Inserted")
                msg.setWindowTitle("Success")
                msg.exec_()
            # conn.close()
        except Exception as es:
            print(f"Exception: {es}")
            msg.setText(f"Error Due To : {str(es)}")
            msg.setWindowTitle("Error")
            msg.exec_()
