import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from admin.global_variables import GlobalStatic, DbConnector


class DocUpdate(object):
    def setupUi(self, MainWindow):
        print("next page")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1166, 946)
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 1091, 901))
        self.graphicsView.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "border: 3px solid white;")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 50, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.cs_id = QtWidgets.QLabel(self.centralwidget)
        self.cs_id.setGeometry(QtCore.QRect(120, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cs_id.setFont(font)
        self.cs_id.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.cs_id.setObjectName("cs_id")
        self.body = QtWidgets.QLabel(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(120, 430, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.body.setFont(font)
        self.body.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.body.setObjectName("body")
        self.weapon = QtWidgets.QLabel(self.centralwidget)
        self.weapon.setGeometry(QtCore.QRect(120, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.weapon.setFont(font)
        self.weapon.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.weapon.setObjectName("weapon")
        self.fl_type = QtWidgets.QLabel(self.centralwidget)
        self.fl_type.setGeometry(QtCore.QRect(120, 590, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fl_type.setFont(font)
        self.fl_type.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.fl_type.setObjectName("fl_type")
        self.assignHospital = QtWidgets.QLabel(self.centralwidget)
        self.assignHospital.setGeometry(QtCore.QRect(120, 760, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assignHospital.setFont(font)
        self.assignHospital.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.assignHospital.setObjectName("assignHospital")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(470, 470, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Submit.setObjectName("Submit")

        print("ui loaded")

        try:
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                "Database=forensic;"
                "Trusted_Connection=yes;"
            )
            cur = conn.cursor()

            print("Got connection")
        except Exception as e:
            print(f"Error getting cursor: {e}")

        print(f"evi_upd_info_tuple: {GlobalStatic.evi_evidence_doc_tuple}")
        if GlobalStatic.evi_evidence_doc_tuple:
            case_evidence = GlobalStatic.evi_evidence_doc_tuple

            case_id = GlobalStatic.evi_evidence_doc_tuple[0]

            print(f"Querying evidence for case id: {case_id}")
            cur.execute("SELECT * FROM evidence_ WHERE c_id=?", (case_id))
            self.evidence_list = cur.fetchall()

            print(f"Evidence for {case_id} is {self.evidence_list}")
            conn.commit()


            if self.evidence_list:
                print(f"Case evidence is: {case_evidence}")
                # case_id = self.evidence_list[0][0]
                body = self.evidence_list[0][1]
                body_analysis = self.evidence_list[0][2]
                weapon = self.evidence_list[0][3]
                weapon_analysis = self.evidence_list[0][4]
                fluid_type = self.evidence_list[0][5]
                fluid_type_analysis = self.evidence_list[0][6]
                personal_belongings = self.evidence_list[0][7]
                personal_belongings_analysis = self.evidence_list[0][8]

                print(f"Values are: {case_id}, {body}, {weapon}, {fluid_type}, {personal_belongings}, {body_analysis}, {weapon_analysis}, {fluid_type_analysis}, {personal_belongings_analysis}")

            else:
                # case_evidence = None
                # case_id = None
                body = ""
                weapon = ""
                fluid_type = ""
                personal_belongings = ""
                weapon_analysis = ""
                body_analysis = ""
                fluid_type_analysis = ""
                personal_belongings_analysis = ""


        self.Case_id = QtWidgets.QLineEdit(self.centralwidget)
        self.Case_id.setGeometry(QtCore.QRect(120, 180, 231, 41))
        self.Case_id.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Case_id.setObjectName("Case_id")
        self.Case_id.setText(case_id)

        self.Body = QtWidgets.QTextEdit(self.centralwidget)
        self.Body.setGeometry(QtCore.QRect(120, 470, 291, 101))
        self.Body.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Body.setObjectName("Body")

        if body:
            self.Body.setText(body)

        self.weapon_ = QtWidgets.QTextEdit(self.centralwidget)
        self.weapon_.setGeometry(QtCore.QRect(120, 300, 291, 101))
        self.weapon_.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.weapon_.setObjectName("weapon_")

        if weapon:
            self.weapon_.setText(weapon)

        self.Fluid = QtWidgets.QTextEdit(self.centralwidget)
        self.Fluid.setGeometry(QtCore.QRect(120, 630, 291, 101))
        self.Fluid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Fluid.setObjectName("Fluid")

        if fluid_type:
            self.Fluid.setText(fluid_type)

        self.personal_ = QtWidgets.QTextEdit(self.centralwidget)
        self.personal_.setGeometry(QtCore.QRect(120, 800, 291, 101))
        self.personal_.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.personal_.setObjectName("personal_")

        if personal_belongings:
            self.personal_.setText(personal_belongings)

        self.fl_typeAnalysis = QtWidgets.QLabel(self.centralwidget)
        self.fl_typeAnalysis.setGeometry(QtCore.QRect(760, 530, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fl_typeAnalysis.setFont(font)
        self.fl_typeAnalysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.fl_typeAnalysis.setObjectName("fl_typeAnalysis")
        self.bodyAnalysis = QtWidgets.QLabel(self.centralwidget)
        self.bodyAnalysis.setGeometry(QtCore.QRect(760, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bodyAnalysis.setFont(font)
        self.bodyAnalysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.bodyAnalysis.setObjectName("bodyAnalysis")

        self.weapon_Analysis = QtWidgets.QTextEdit(self.centralwidget)
        self.weapon_Analysis.setGeometry(QtCore.QRect(760, 240, 291, 101))
        self.weapon_Analysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.weapon_Analysis.setObjectName("weapon_Analysis")

        if weapon_analysis:
            self.weapon_Analysis.setText(weapon_analysis)

        self.Body_Analysis = QtWidgets.QTextEdit(self.centralwidget)
        self.Body_Analysis.setGeometry(QtCore.QRect(760, 410, 291, 101))
        self.Body_Analysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Body_Analysis.setObjectName("Body_Analysis")


        if body_analysis:
            self.Body_Analysis.setText(body_analysis)


        print("body")
        self.Fluid_Analysis = QtWidgets.QTextEdit(self.centralwidget)
        self.Fluid_Analysis.setGeometry(QtCore.QRect(760, 570, 291, 101))
        self.Fluid_Analysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Fluid_Analysis.setObjectName("Fluid_Analysis")

        if fluid_type_analysis:
            self.Fluid_Analysis.setText(fluid_type_analysis)
        #
        print("fluid")


        self.weaponAnalysis = QtWidgets.QLabel(self.centralwidget)
        self.weaponAnalysis.setGeometry(QtCore.QRect(760, 200, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.weaponAnalysis.setFont(font)
        self.weaponAnalysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.weaponAnalysis.setObjectName("weaponAnalysis")
        self.assignHospitalAnalysis = QtWidgets.QLabel(self.centralwidget)
        self.assignHospitalAnalysis.setGeometry(QtCore.QRect(760, 700, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assignHospitalAnalysis.setFont(font)
        self.assignHospitalAnalysis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.assignHospitalAnalysis.setObjectName("assignHospitalAnalysis")
        self.personal_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.personal_1.setGeometry(QtCore.QRect(760, 740, 291, 101))
        self.personal_1.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.personal_1.setObjectName("personal_1")

        if personal_belongings_analysis:
            self.personal_1.setText(personal_belongings_analysis)
        print("personal")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Submit.clicked.connect(self.update_data)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "        Evidance Analysis"))
        self.cs_id.setText(_translate("MainWindow", "   Case_id"))
        self.body.setText(_translate("MainWindow", "   Body"))
        self.weapon.setText(_translate("MainWindow", "   Weapon"))
        self.fl_type.setText(_translate("MainWindow", "   Fluid Type"))
        self.assignHospital.setText(_translate("MainWindow", "   Personal Belongings"))
        self.Submit.setText(_translate("MainWindow", "Update"))
        self.fl_typeAnalysis.setText(_translate("MainWindow", "   Fluid Analysis"))
        self.bodyAnalysis.setText(_translate("MainWindow", "   Body Analysis"))
        self.weaponAnalysis.setText(_translate("MainWindow", "   Weapon Analysis"))
        self.assignHospitalAnalysis.setText(_translate("MainWindow", "   Personal Belongings Analysis"))

    def update_data(self):
        msg = QMessageBox()

        try:
            # conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                "Database=forensic;"
                "Trusted_Connection=yes;"
            )
            cur = conn.cursor()
            print("connection successful")

            cur.execute(
                "UPDATE evidence_ SET body_analysis=?, weapon_analysis=?, fluid_analysis = ?,personal_belong_analy = ? WHERE c_id=?",
                (
                    self.Body_Analysis.toPlainText(),
                    self.weapon_Analysis.toPlainText(),
                    self.Fluid_Analysis.toPlainText(),
                    self.personal_1.toPlainText(),
                    self.Case_id.text()
                ))
            # messagebox.showinfo("Success", f"Successfully Updated", parent=self.root)

            conn.commit()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Analysis Successfully Updated!")
            msg.setWindowTitle("Success")
            msg.exec_()
            # self.fetch_data()
            # self.clear()
            # conn.close()

        except Exception as es:
            print(f"Error Due To : {str(es)}")
            msg.setText(f"Error Due To : {str(es)}")
            msg.setWindowTitle("WARNING")
            msg.exec_()
        # messagebox.showerror("Error", f"Error Due To : {str(es)}", parent=self.root)
