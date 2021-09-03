import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from admin.global_variables import GlobalStatic


class CaseRegister(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 790)
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 30, 961, 721))
        self.graphicsView.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "border: 3px solid white;")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 50, 431, 61))
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
        self.assignPolice.setGeometry(QtCore.QRect(130, 530, 141, 31))
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
        self.Submit.setGeometry(QtCore.QRect(350, 660, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Submit.setObjectName("Submit")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(610, 660, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Back.setFont(font)
        self.Back.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Back.setObjectName("Back")
        self.Case_id = QtWidgets.QLineEdit(self.centralwidget)
        self.Case_id.setGeometry(QtCore.QRect(130, 210, 231, 41))
        self.Case_id.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Case_id.setObjectName("Case_id")
        self.Case_name = QtWidgets.QLineEdit(self.centralwidget)
        self.Case_name.setGeometry(QtCore.QRect(670, 210, 231, 41))
        self.Case_name.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Case_name.setObjectName("Case_name")
        self.Type_Of_Crime = QtWidgets.QLineEdit(self.centralwidget)
        self.Type_Of_Crime.setGeometry(QtCore.QRect(130, 330, 231, 41))
        self.Type_Of_Crime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Type_Of_Crime.setObjectName("Type_Of_Crime")
        self.Date_Of_Crime = QtWidgets.QLineEdit(self.centralwidget)
        self.Date_Of_Crime.setGeometry(QtCore.QRect(670, 330, 231, 41))
        self.Date_Of_Crime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Date_Of_Crime.setObjectName("Date_Of_Crime")
        self.Time_Of_crime = QtWidgets.QLineEdit(self.centralwidget)
        self.Time_Of_crime.setGeometry(QtCore.QRect(130, 450, 231, 41))
        self.Time_Of_crime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Time_Of_crime.setObjectName("Time_Of_crime")
        self.Location_ = QtWidgets.QLineEdit(self.centralwidget)
        self.Location_.setGeometry(QtCore.QRect(670, 450, 231, 41))
        self.Location_.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Location_.setObjectName("Location_")
        self.AssignPol_combo = QtWidgets.QComboBox(self.centralwidget)
        self.AssignPol_combo.setGeometry(QtCore.QRect(130, 570, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AssignPol_combo.setFont(font)
        self.AssignPol_combo.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.AssignPol_combo.setObjectName("AssignPol_combo")
        self.AssignPol_combo.addItem("")
        # self.AssignPol_combo.addItem("")
        # self.AssignPol_combo.addItem("")
        # self.AssignPol_combo.addItem("")
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Back.clicked.connect(lambda: self.crclosescr(MainWindow))
        self.Submit.clicked.connect(self.StCaseRegistration)

    def crclosescr(self, MainWindow):
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  CASE REGISTRATION"))
        self.cs_id.setText(_translate("MainWindow", "   Case_id"))
        self.cs_name.setText(_translate("MainWindow", "   Name"))
        self.typeofcrime.setText(_translate("MainWindow", "   Type Of Crime"))
        self.dateOfCrime.setText(_translate("MainWindow", "   Date Of Crime"))
        self.timOfCrime.setText(_translate("MainWindow", "   Time Of Report"))
        self.location.setText(_translate("MainWindow", "   Location"))
        self.assignPolice.setText(_translate("MainWindow", "   Assign Police"))
        self.assignHospital.setText(_translate("MainWindow", "   Assign Hospital"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.Back.setText(_translate("MainWindow", "<- Back"))

        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT p_id,p_name FROM police where pst_id=?", GlobalStatic.police_station_id)
        res_tuple_list = cursor.fetchall()
        self.name_list = []
        for first, s in enumerate(res_tuple_list):
            p_id, name = s
            self.name_list.append(f"{name}-{p_id}")
            self.AssignPol_combo.insertItem(first, _translate("MainWindow",f"{name}-{p_id}"))
            # self.AssignPol_combo.addItem("")

        # print(name_list)

        self.AssignPol_combo.currentIndexChanged.connect(self.__on_police_changed)


        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT h_id,h_name FROM hospital")  # where pst_id=?"),GlobalStatic.pst_id)
        res_tuple_list1 = cursor.fetchall()
        self.name_list1 = []
        for index, k in enumerate(res_tuple_list1):
            h_id, h_name = k
            self.name_list1.append(f"{h_name}-{h_id}")
            print(f"Hospital is: {k}")
            self.AssignDoc_combo.insertItem(index, _translate("MainWindow", f"{h_name}-{h_id}"))
        # print(name_list1)

        self.AssignDoc_combo.currentIndexChanged.connect(self.__on_doctor_changed)

    def StCaseRegistration(self):
        c_id = self.Case_id.text()
        c_name = self.Case_name.text()
        c_type = self.Type_Of_Crime.text()
        c_Date = self.Date_Of_Crime.text()
        c_time = self.Time_Of_crime.text()
        c_loc = self.Location_.text()
        # p_email = self.AssignPol_combo.text()
        # p_pass = self.AssignDoc_combo.text()
        # print("ID" + d_id)
        # print("Name" + d_name)
        # print("Age" + d_age)
        # print("place" + d_place)
        # print("phone" + d_phone)
        # print("exp" + d_exp)
        # print("email" + d_email)
        # print("pass" + d_pass)
        # print(f"Obtained hospital id: {GlobalStatic.hospital_id}")

        msg = QMessageBox()

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if c_id == "" or c_name == "" or c_type == "" or c_Date == "" or c_time == "" or c_loc == "":
            msg.setText("All Fields need to be filled!")
            msg.setWindowTitle("WARNING")
            msg.exec_()

        # elif not self.txt_dexp.get().isdigit():
        #     messagebox.showerror("Error", "Enter valid Experiance!", parent=self.root)
        # #
        # elif not self.txt_dage.get().isdigit():
        #     # messagebox.showerror("Error", "Enter valid Age!", parent=self.root)
        # #
        # elif not self.txt_dphone.get().isdigit():
        #     messagebox.showerror("Error", "Enter valid Phone no!", parent=self.root)
        #
        # elif len(self.txt_dphone.get()) > 10 or len(self.txt_dphone.get()) < 10:
        #     messagebox.showerror("Error", "Enter valid Phone no!", parent=self.root)
        # #
        # elif not (re.search(regex, self.txt_demail.get())):
        #     messagebox.showerror("Error", "Enter valid Email_id!", parent=self.root)

        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                    "Database=forensic;"
                    "Trusted_Connection=yes;"
                )
                cur = conn.cursor()
                cur.execute("select * from doctor where d_email=?", c_id)
                row = cur.fetchone()
                print(row)
                if row != None:
                    msg.setText("Check Username/Password")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
                else:
                    # print(f"Police and hospital data: {self.AssignPol_combo.text()}, {self.AssignDoc_combo.text()}")
                    # police_pid = self.AssignPol_combo.itemText().split("-")[1]
                    # hospital_pid = self.AssignDoc_combo.itemText().split("-")[1]
                    cur.execute(
                        "insert into case_ (c_id, c_name, c_typr,c_date, c_time, c_location,p_id, h_id,pst_id) values(?,?,?,?,?,?,?,?,?);",
                        (c_id,
                         c_name,
                         c_type,
                         c_Date,
                         c_time,
                         c_loc,
                         GlobalStatic.assign_pid_tuple,
                         GlobalStatic.assign_did_tuple,
                         GlobalStatic.police_station_id
                         )
                    )
                    msg.setText("Registration SuccessFull!")
                    msg.setWindowTitle("Success")
                    msg.exec_()
                    conn.commit()
                    conn.close()

            except Exception as es:
                print(str(es))
                msg.setText(f"Error Due To: {str(es)}!")
                msg.setWindowTitle("WARNING")
                msg.exec_()

    def __on_police_changed(self, index):
        print(f"Current police is: {self.name_list[index]}")
        pid = self.name_list[index].split("-")[1]
        GlobalStatic.set_assign_pid_tuple(pid)
        print(f"current pid is:{pid}")

    def __on_doctor_changed(self, index):
        print(f"Current doctor is: {self.name_list1[index]}")
        did = self.name_list1[index].split("-")[1]
        GlobalStatic.set_assign_did_tuple(did)
        print(f"current did is:{did}")