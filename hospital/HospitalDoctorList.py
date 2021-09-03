import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from admin.global_variables import GlobalStatic


class docList(object):
    def __init__(self):
        super().__init__()

        self.__all_cases_list_ = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1387, 783)
        MainWindow.setStyleSheet("background-color: rgb(191, 140, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, -20, 1451, 101))
        self.graphicsView_2.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                          "border: 3px solid white;\n"
                                          "")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-30, 0, 1421, 81))
        self.graphicsView.setStyleSheet("background-color: rgb(233, 255, 246);")
        self.graphicsView.setObjectName("graphicsView")
        self.dlUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.dlUpdate.setGeometry(QtCore.QRect(120, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dlUpdate.setFont(font)
        self.dlUpdate.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                    "")
        self.dlUpdate.setObjectName("dlUpdate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 0, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                 "color: rgb(255, 0, 4);\n"
                                 "")
        self.label.setObjectName("label")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(25, 101, 441, 651))
        self.graphicsView_3.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                          "border: 3px solid white;\n"
                                          "")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(480, 100, 891, 651))
        self.graphicsView_4.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                          "border: 3px solid white;\n"
                                          "")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.dlDelete = QtWidgets.QPushButton(self.centralwidget)
        self.dlDelete.setGeometry(QtCore.QRect(270, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dlDelete.setFont(font)
        self.dlDelete.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                    "")
        self.dlDelete.setObjectName("dlDelete")
        #         self.dlClear = QtWidgets.QPushButton(self.centralwidget)
        #         self.dlClear.setGeometry(QtCore.QRect(340, 680, 101, 41))
        #         font = QtGui.QFont()
        #         font.setFamily("Times New Roman")
        #         font.setPointSize(12)
        #         font.setBold(True)
        #         font.setWeight(75)
        #         self.dlClear.setFont(font)
        #         self.dlClear.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        # "")
        #         self.dlClear.setObjectName("dlClear")
        self.dlBack = QtWidgets.QPushButton(self.centralwidget)
        self.dlBack.setGeometry(QtCore.QRect(10, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dlBack.setFont(font)
        self.dlBack.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                  "")
        self.dlBack.setObjectName("dlBack")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.dl_id = QtWidgets.QLabel(self.centralwidget)
        self.dl_id.setGeometry(QtCore.QRect(30, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dl_id.setFont(font)
        self.dl_id.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "")
        self.dl_id.setObjectName("dl_id")
        self.dl_name = QtWidgets.QLabel(self.centralwidget)
        self.dl_name.setGeometry(QtCore.QRect(30, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dl_name.setFont(font)
        self.dl_name.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "")
        self.dl_name.setObjectName("dl_name")
        self.dlExp = QtWidgets.QLabel(self.centralwidget)
        self.dlExp.setGeometry(QtCore.QRect(30, 400, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dlExp.setFont(font)
        self.dlExp.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "")
        self.dlExp.setObjectName("dlExp")
        self.dl_age = QtWidgets.QLabel(self.centralwidget)
        self.dl_age.setGeometry(QtCore.QRect(30, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dl_age.setFont(font)
        self.dl_age.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "")
        self.dl_age.setObjectName("dl_age")
        self.dlPhone = QtWidgets.QLabel(self.centralwidget)
        self.dlPhone.setGeometry(QtCore.QRect(30, 520, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dlPhone.setFont(font)
        self.dlPhone.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "")
        self.dlPhone.setObjectName("dlPhone")
        self.dlPlace = QtWidgets.QLabel(self.centralwidget)
        self.dlPlace.setGeometry(QtCore.QRect(30, 460, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dlPlace.setFont(font)
        self.dlPlace.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "")
        self.dlPlace.setObjectName("dlPlace")
        self.dl_Emanil = QtWidgets.QLabel(self.centralwidget)
        self.dl_Emanil.setGeometry(QtCore.QRect(30, 580, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dl_Emanil.setFont(font)
        self.dl_Emanil.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "")
        self.dl_Emanil.setObjectName("dl_Emanil")
        self.dlid = QtWidgets.QLineEdit(self.centralwidget)
        self.dlid.setGeometry(QtCore.QRect(190, 200, 231, 31))
        self.dlid.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                "")
        self.dlid.setObjectName("dlid")
        self.dlname = QtWidgets.QLineEdit(self.centralwidget)
        self.dlname.setGeometry(QtCore.QRect(190, 270, 231, 31))
        self.dlname.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                  "")
        self.dlname.setObjectName("dlname")
        self.dlage = QtWidgets.QLineEdit(self.centralwidget)
        self.dlage.setGeometry(QtCore.QRect(190, 340, 231, 31))
        self.dlage.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                 "")
        self.dlage.setObjectName("dlage")
        self.dl_exp = QtWidgets.QLineEdit(self.centralwidget)
        self.dl_exp.setGeometry(QtCore.QRect(190, 400, 231, 31))
        self.dl_exp.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                  "")
        self.dl_exp.setObjectName("dl_exp")
        self.dl_place = QtWidgets.QLineEdit(self.centralwidget)
        self.dl_place.setGeometry(QtCore.QRect(190, 460, 231, 31))
        self.dl_place.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                    "")
        self.dl_place.setObjectName("dl_place")
        self.dlPhone_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.dlPhone_2.setGeometry(QtCore.QRect(190, 520, 231, 31))
        self.dlPhone_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "")
        self.dlPhone_2.setObjectName("dlPhone_2")
        self.dlEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.dlEmail.setGeometry(QtCore.QRect(190, 580, 231, 31))
        self.dlEmail.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "")
        self.dlEmail.setObjectName("dlEmail")
        self.dl_search_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.dl_search_entry.setGeometry(QtCore.QRect(970, 120, 201, 41))
        self.dl_search_entry.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                           "")
        self.dl_search_entry.setObjectName("dl_search_entry")
        self.dl_search = QtWidgets.QPushButton(self.centralwidget)
        self.dl_search.setGeometry(QtCore.QRect(1240, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dl_search.setFont(font)
        self.dl_search.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "")
        self.dl_search.setObjectName("dl_search")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 120, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        self.label_10.setObjectName("label_10")
        self.dl_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dl_comboBox.setGeometry(QtCore.QRect(750, 120, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dl_comboBox.setFont(font)
        self.dl_comboBox.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                       "")
        self.dl_comboBox.setObjectName("dl_comboBox")
        self.dl_comboBox.addItem("")
        self.dl_comboBox.addItem("")
        self.dl_comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(500, 200, 851, 531))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                       "border: 3px solid white;\n"
                                       "")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.cellClicked.connect(self._cell_clicked)

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1330, 230, 21, 501))
        self.verticalScrollBar.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.graphicsView_3.raise_()
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.dlUpdate.raise_()
        self.label.raise_()
        self.graphicsView_4.raise_()
        self.dlDelete.raise_()
        # self.dlClear.raise_()
        self.dlBack.raise_()
        self.label_2.raise_()
        self.dl_id.raise_()
        self.dl_name.raise_()
        self.dlExp.raise_()
        self.dl_age.raise_()
        self.dlPhone.raise_()
        self.dlPlace.raise_()
        self.dl_Emanil.raise_()
        self.dlid.raise_()
        self.dlname.raise_()
        self.dlage.raise_()
        self.dl_exp.raise_()
        self.dl_place.raise_()
        self.dlPhone_2.raise_()
        self.dlEmail.raise_()
        self.dl_search_entry.raise_()
        self.dl_search.raise_()
        self.label_10.raise_()
        self.dl_comboBox.raise_()
        self.tableWidget.raise_()
        self.verticalScrollBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dlBack.clicked.connect(lambda: self.hcclosescr(MainWindow))

    def hcclosescr(self, MainWindow):
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dlUpdate.setText(_translate("MainWindow", "UPDATE"))
        self.dlUpdate.clicked.connect(self.update_data)
        self.label.setText(_translate("MainWindow", "DOCTOR LIST"))
        self.dlDelete.setText(_translate("MainWindow", "DELETE"))
        # self.dlClear.setText(_translate("MainWindow", "CLEAR"))
        self.dlBack.setText(_translate("MainWindow", "<-BACK"))
        self.label_2.setWhatsThis(_translate("MainWindow",
                                             "<html><head/><body><p>background-color: rgb(217, 217, 217);</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "     DETAILS"))
        self.dl_id.setText(_translate("MainWindow", "  Doctor_id"))
        self.dl_name.setText(_translate("MainWindow", "  Name"))
        self.dlExp.setText(_translate("MainWindow", "  Experiance"))
        self.dl_age.setText(_translate("MainWindow", "  Age"))
        self.dlPhone.setText(_translate("MainWindow", "  Phone"))
        self.dlPlace.setText(_translate("MainWindow", "  Place"))
        self.dl_Emanil.setText(_translate("MainWindow", "  Email"))
        self.dl_search.setText(_translate("MainWindow", "SEARCH"))
        self.dl_search.clicked.connect(self.search_data)
        self.label_10.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p>background-color: rgb(217, 217, 217);</p><p><br/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "  SEARCH BY"))
        self.dl_comboBox.setItemText(0, _translate("MainWindow", "d_id"))
        self.dl_comboBox.setItemText(1, _translate("MainWindow", "d_name"))
        self.dl_comboBox.setItemText(2, _translate("MainWindow", "d_phone"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Doctor_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Experience"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Place"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        self.__load_case_data_()
        self.dlDelete.clicked.connect(self.delete_data)

    def __load_case_data_(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cur = conn.cursor()
        cur.execute("select d_id,d_name,d_age,d_exp,d_place,d_phone,d_email from doctor where h_id=?;",
                    (GlobalStatic.hospital_id))
        rows = cur.fetchall()
        self.tableWidget.setRowCount(50)
        tableindex = 0

        self.__all_cases_list_ = rows

        for row in rows:
            print(row)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tableindex, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tableindex, 6, QtWidgets.QTableWidgetItem(row[6]))
            # self.tableWidget.setItem(tableindex, 7, QtWidgets.QTableWidgetItem(row[7]))
            # self.tableWidget.setItem(tableindex, 8, QtWidgets.QTableWidgetItem(row[8]))
            tableindex += 1
            conn.commit()
        conn.close()

    def _cell_clicked(self, row_index, column_index):
        # print(f"Signal received: {row} {column}")
        row = self.__all_cases_list_[row_index]

        GlobalStatic.set_delete_doc(row[0])

        print(f"Case selected: {row}")
        self.dlid.setText(row[0])
        self.dlname.setText(row[1])
        self.dlage.setText(row[2])
        self.dl_exp.setText(row[3])
        self.dl_place.setText(row[4])
        self.dlPhone_2.setText(row[5])
        self.dlEmail.setText(row[6])
        # self.dlcEmail_3.setText(row[7])
        # self.dclEmail_4.setText(row[8])

    def delete_data(self, row_index):
        msg = QMessageBox()

        print(GlobalStatic.set_delete_doc)
        # conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
        try:
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                "Database=forensic;"
                "Trusted_Connection=yes;"
            )
            cur = conn.cursor()
            cur.execute("delete from doctor where d_id=?", (GlobalStatic.set_delete_doc))
            conn.commit()
            msg.setText("Successfully Deleted!!")
            msg.setWindowTitle("Success")
            msg.exec_()
            # self.fetch_data()
            # self.clear()
            conn.close()
        except Exception as es:
            print(f"the exception is {es}")

    def search_data(self):
        # conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cur = conn.cursor()

        query = f"SELECT d_id,d_name,d_age,d_exp,d_place,d_phone,d_email FROM doctor WHERE {self.dl_comboBox.currentText()} LIKE '%{self.dl_search_entry.text()}%'"
        print(f"Querying for: {query}")
        cur.execute(query)

        rows = cur.fetchall()

        print(f"Query result: {rows}")

        try:
            self.tableWidget.clear()
            for i, data in enumerate(rows):
                for j, entry in enumerate(data):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(entry))
        except Exception as e:
            print(e)
        conn.commit()

    def update_data(self):
        msg = QMessageBox()

        print(GlobalStatic.set_delete_doc)

        try:
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                "Database=forensic;"
                "Trusted_Connection=yes;"
            )
            cur = conn.cursor()
            cur.execute("Update doctor set d_name = ?, d_age=?, d_exp=?, d_place=?, d_phone=?, d_email=? where d_id = ?", (self.dlname.text(),
                                                                                                                                        self.dlage.text(),
                                                                                                                                        self.dl_exp.text(),
                                                                                                                                        self.dl_place.text(),
                                                                                                                                        self.dlPhone_2.text(),
                                                                                                                                        self.dlEmail.text(),
                                                                                                                                        GlobalStatic.set_delete_doc))
            conn.commit()
            conn.close()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Successfully updated the data")
            msg.setWindowTitle("Success")
            msg.exec_()
        except Exception as es:
            print(f"the exception is{es}")
