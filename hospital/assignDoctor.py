import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from admin.global_variables import GlobalStatic


class AssignDoctor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 790)
        print(f"Test: {GlobalStatic.test}")
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 30, 961, 721))
        self.graphicsView.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "border: 3px solid white;")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 50, 341, 61))
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
        self.cs_name = QtWidgets.QLabel(self.centralwidget)
        self.cs_name.setGeometry(QtCore.QRect(670, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cs_name.setFont(font)
        self.cs_name.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.cs_name.setObjectName("cs_name")
        self.typeofcrime = QtWidgets.QLabel(self.centralwidget)
        self.typeofcrime.setGeometry(QtCore.QRect(130, 290, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.typeofcrime.setFont(font)
        self.typeofcrime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.typeofcrime.setObjectName("typeofcrime")
        self.dateOfCrime = QtWidgets.QLabel(self.centralwidget)
        self.dateOfCrime.setGeometry(QtCore.QRect(670, 290, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateOfCrime.setFont(font)
        self.dateOfCrime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.dateOfCrime.setObjectName("dateOfCrime")
        self.timOfCrime = QtWidgets.QLabel(self.centralwidget)
        self.timOfCrime.setGeometry(QtCore.QRect(130, 410, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timOfCrime.setFont(font)
        self.timOfCrime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.timOfCrime.setObjectName("timOfCrime")
        self.location = QtWidgets.QLabel(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(670, 410, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.location.setFont(font)
        self.location.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.location.setObjectName("location")
        self.assignPolice = QtWidgets.QLabel(self.centralwidget)
        self.assignPolice.setGeometry(QtCore.QRect(130, 530, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assignPolice.setFont(font)
        self.assignPolice.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.assignPolice.setObjectName("assignPolice")
        self.assignHospital = QtWidgets.QLabel(self.centralwidget)
        self.assignHospital.setGeometry(QtCore.QRect(670, 530, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assignHospital.setFont(font)
        self.assignHospital.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.assignHospital.setObjectName("assignHospital")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(400, 660, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Submit.setObjectName("Submit")
        # self.Back = QtWidgets.QPushButton(self.centralwidget)
        # self.Back.setGeometry(QtCore.QRect(610, 660, 171, 61))
        # font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(75)
        # self.Back.setFont(font)
        # self.Back.setStyleSheet("background-color: rgb(217, 217, 217);")
        # self.Back.setObjectName("Back")

        crime_id = GlobalStatic.case_info_tuple[0] if GlobalStatic.case_info_tuple else ""
        # print(crime_id)
        self.Case_id = QtWidgets.QLineEdit(self.centralwidget)
        self.Case_id.setText(crime_id)
        self.Case_id.setGeometry(QtCore.QRect(130, 210, 231, 41))
        self.Case_id.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Case_id.setObjectName("Case_id")
        self.Case_name = QtWidgets.QLineEdit(self.centralwidget)

        name = GlobalStatic.case_info_tuple[1] if GlobalStatic.case_info_tuple else ""
        self.Case_name.setText(name)

        self.Case_name.setGeometry(QtCore.QRect(670, 210, 231, 41))
        self.Case_name.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Case_name.setObjectName("Case_name")

        type = GlobalStatic.case_info_tuple[2] if GlobalStatic.case_info_tuple else ""

        self.Type_Of_Crime = QtWidgets.QLineEdit(self.centralwidget)
        self.Type_Of_Crime.setGeometry(QtCore.QRect(130, 330, 231, 41))
        self.Type_Of_Crime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Type_Of_Crime.setObjectName("Type_Of_Crime")
        self.Type_Of_Crime.setText(type)

        date = GlobalStatic.case_info_tuple[3] if GlobalStatic.case_info_tuple else ""

        self.Date_Of_Crime = QtWidgets.QLineEdit(self.centralwidget)
        self.Date_Of_Crime.setGeometry(QtCore.QRect(670, 330, 231, 41))
        self.Date_Of_Crime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Date_Of_Crime.setObjectName("Date_Of_Crime")
        self.Date_Of_Crime.setText(date)



        time = GlobalStatic.case_info_tuple[4] if GlobalStatic.case_info_tuple else ""


        self.Time_Of_crime = QtWidgets.QLineEdit(self.centralwidget)
        self.Time_Of_crime.setGeometry(QtCore.QRect(130, 450, 231, 41))
        self.Time_Of_crime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Time_Of_crime.setObjectName("Time_Of_crime")
        self.Time_Of_crime.setText(time)


        loc = GlobalStatic.case_info_tuple[5] if GlobalStatic.case_info_tuple else ""

        self.Location_ = QtWidgets.QLineEdit(self.centralwidget)
        self.Location_.setGeometry(QtCore.QRect(670, 450, 231, 41))
        self.Location_.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Location_.setObjectName("Location_")
        self.Location_.setText(loc)


        self.AssignDoc_combo = QtWidgets.QComboBox(self.centralwidget)
        self.AssignDoc_combo.setGeometry(QtCore.QRect(670, 570, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AssignDoc_combo.setFont(font)
        self.AssignDoc_combo.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.AssignDoc_combo.setObjectName("AssignDoc_combo")
        self.AssignDoc_combo.addItem("")
        self.AssignDoc_combo.addItem("")

        asspol = GlobalStatic.case_info_tuple[6] if GlobalStatic.case_info_tuple else ""
        self.Time_Of_crime_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Time_Of_crime_2.setGeometry(QtCore.QRect(130, 570, 231, 41))
        self.Time_Of_crime_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Time_Of_crime_2.setObjectName("Time_Of_crime_2")
        self.Time_Of_crime_2.setText(asspol)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Submit.clicked.connect(self.update_data)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "        Assign Doctor"))
        self.cs_id.setText(_translate("MainWindow", "   Case_id"))
        self.cs_name.setText(_translate("MainWindow", "   Name"))
        self.typeofcrime.setText(_translate("MainWindow", "   Type Of Crime"))
        self.dateOfCrime.setText(_translate("MainWindow", "   Date Of Crime"))
        self.timOfCrime.setText(_translate("MainWindow", "   Time Of Report"))
        self.location.setText(_translate("MainWindow", "   Location"))
        self.assignPolice.setText(_translate("MainWindow", "   Assigned Police"))
        self.assignHospital.setText(_translate("MainWindow", "   Assign Doctor"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        # self.Back.setText(_translate("MainWindow", "<- Back"))

        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT d_id,d_name FROM doctor where h_id=?", GlobalStatic.hospital_id)
        res_tuple_list3 = cursor.fetchall()
        self.name_list3 = []
        for index, l in enumerate(res_tuple_list3):
            d_id, d_name = l
            self.name_list3.append(f"{d_id}-{d_name}")
            print(f"Hospital is: {l}")
            self.AssignDoc_combo.insertItem(index, _translate("MainWindow", f"{d_id}-{d_name}"))
        # print(name_list1)

        self.AssignDoc_combo.currentIndexChanged.connect(self.__on_AssignDoc_changed)

    def __on_AssignDoc_changed(self, index):
        print(f"Current doctor is: {self.name_list3[index]}")
        hospital_assign_did = self.name_list3[index].split("-")[0]
        GlobalStatic.set_hospital_assign_did_tuple(hospital_assign_did)
        print(f"current did is:{hospital_assign_did}")


    def update_data(self):
        # conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
        msg = QMessageBox()

        try:
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                "Database=forensic;"
                "Trusted_Connection=yes;"
            )
            cur = conn.cursor()

            cur.execute("update case_ set d_id = ? where c_id=?", (GlobalStatic.hospital_assign_did, GlobalStatic.case_info_tuple[0]))
            msg.setText("Registration SuccessFull!")
            msg.setWindowTitle("Success")
            conn.commit()
            # self.fetch_data()
            # self.clear()
            conn.close()
            msg.exec_()

        except Exception as es:
            msg.setText(f"Error {es}")
            msg.setWindowTitle("Error")
            msg.exec_()

