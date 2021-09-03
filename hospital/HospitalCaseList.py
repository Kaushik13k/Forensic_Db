import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from admin.global_variables import GlobalStatic
from assignDoctor import AssignDoctor


class HospitalCaseList(object):
    def __init__(self):
        super().__init__()

        self.__all_cases_list = []

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
        self.dclUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.dclUpdate.setGeometry(QtCore.QRect(120, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dclUpdate.setFont(font)
        self.dclUpdate.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "")
        self.dclUpdate.setObjectName("dclUpdate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 0, 481, 71))
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
        self.dvlDelete = QtWidgets.QPushButton(self.centralwidget)
        self.dvlDelete.setGeometry(QtCore.QRect(270, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dvlDelete.setFont(font)
        self.dvlDelete.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "")
        self.dvlDelete.setObjectName("dvlDelete")
        # self.dvlClear = QtWidgets.QPushButton(self.centralwidget)
        # self.dvlClear.setGeometry(QtCore.QRect(340, 680, 101, 41))
        # font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        # self.dvlClear.setFont(font)
        # self.dvlClear.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        #                             "")
        # self.dvlClear.setObjectName("dvlClear")
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
        self.dcl_id = QtWidgets.QLabel(self.centralwidget)
        self.dcl_id.setGeometry(QtCore.QRect(30, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_id.setFont(font)
        self.dcl_id.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "")
        self.dcl_id.setObjectName("dcl_id")
        self.dcl_name = QtWidgets.QLabel(self.centralwidget)
        self.dcl_name.setGeometry(QtCore.QRect(30, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_name.setFont(font)
        self.dcl_name.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        self.dcl_name.setObjectName("dcl_name")
        self.dclExp = QtWidgets.QLabel(self.centralwidget)
        self.dclExp.setGeometry(QtCore.QRect(30, 330, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dclExp.setFont(font)
        self.dclExp.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "")
        self.dclExp.setObjectName("dclExp")
        self.dcl_age = QtWidgets.QLabel(self.centralwidget)
        self.dcl_age.setGeometry(QtCore.QRect(30, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_age.setFont(font)
        self.dcl_age.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "")
        self.dcl_age.setObjectName("dcl_age")
        self.dclPhone = QtWidgets.QLabel(self.centralwidget)
        self.dclPhone.setGeometry(QtCore.QRect(30, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dclPhone.setFont(font)
        self.dclPhone.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        self.dclPhone.setObjectName("dclPhone")
        self.dclPlace = QtWidgets.QLabel(self.centralwidget)
        self.dclPlace.setGeometry(QtCore.QRect(30, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dclPlace.setFont(font)
        self.dclPlace.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        self.dclPlace.setObjectName("dclPlace")
        self.dcl_Emanil = QtWidgets.QLabel(self.centralwidget)
        self.dcl_Emanil.setGeometry(QtCore.QRect(30, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_Emanil.setFont(font)
        self.dcl_Emanil.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "")
        self.dcl_Emanil.setObjectName("dcl_Emanil")
        self.dlcid = QtWidgets.QLineEdit(self.centralwidget)
        # self.dlcid.setText("Hello world")
        self.dlcid.setGeometry(QtCore.QRect(190, 180, 231, 31))
        self.dlcid.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                 "")
        self.dlcid.setObjectName("dlcid")
        self.dclname = QtWidgets.QLineEdit(self.centralwidget)
        self.dclname.setGeometry(QtCore.QRect(190, 230, 231, 31))
        self.dclname.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "")
        self.dclname.setObjectName("dclname")
        self.dclage = QtWidgets.QLineEdit(self.centralwidget)
        self.dclage.setGeometry(QtCore.QRect(190, 280, 231, 31))
        self.dclage.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                  "")
        self.dclage.setObjectName("dclage")
        self.dcl_exp = QtWidgets.QLineEdit(self.centralwidget)
        self.dcl_exp.setGeometry(QtCore.QRect(190, 330, 231, 31))
        self.dcl_exp.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "")
        self.dcl_exp.setObjectName("dcl_exp")
        self.dcl_place = QtWidgets.QLineEdit(self.centralwidget)
        self.dcl_place.setGeometry(QtCore.QRect(190, 380, 231, 31))
        self.dcl_place.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "")
        self.dcl_place.setObjectName("dcl_place")
        self.dclPhone_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.dclPhone_2.setGeometry(QtCore.QRect(190, 430, 231, 31))
        self.dclPhone_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "")
        self.dclPhone_2.setObjectName("dclPhone_2")
        #         self.dcclEmail = QtWidgets.QLineEdit(self.selfcentralwidget)
        #         self.dcclEmail.setGeometry(QtCore.QRect(190, 480, 231, 31))
        #         self.dcclEmail.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        # "")
        #         self.dcclEmail.setObjectName("dcclEmail")
        self.dcl_search_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.dcl_search_entry.setGeometry(QtCore.QRect(970, 120, 201, 41))
        self.dcl_search_entry.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                            "")
        self.dcl_search_entry.setObjectName("dcl_search_entry")
        self.dCl_search = QtWidgets.QPushButton(self.centralwidget)
        self.dCl_search.setGeometry(QtCore.QRect(1240, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dCl_search.setFont(font)
        self.dCl_search.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "")
        self.dCl_search.setObjectName("dCl_search")
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
        self.dcl_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dcl_comboBox.setGeometry(QtCore.QRect(750, 120, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_comboBox.setFont(font)
        self.dcl_comboBox.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                        "")
        self.dcl_comboBox.setObjectName("dcl_comboBox")
        self.dcl_comboBox.addItem("")
        self.dcl_comboBox.addItem("")
        self.dcl_comboBox.addItem("")
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
        self.tableWidget.setColumnCount(9)
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
        # self.tableWidget.setHorizontalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.tableWidget.cellClicked.connect(self._cell_clicked)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.dcl_Email_2 = QtWidgets.QLabel(self.centralwidget)
        self.dcl_Email_2.setGeometry(QtCore.QRect(30, 480, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_Email_2.setFont(font)
        self.dcl_Email_2.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "")
        self.dcl_Email_2.setObjectName("dcl_Emanil_2")
        self.dcl_Emanil_3 = QtWidgets.QLabel(self.centralwidget)
        self.dcl_Emanil_3.setGeometry(QtCore.QRect(30, 530, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_Emanil_3.setFont(font)
        self.dcl_Emanil_3.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "")
        self.dcl_Emanil_3.setObjectName("dcl_Emanil_3")
        self.dcl_Emanil_4 = QtWidgets.QLabel(self.centralwidget)
        self.dcl_Emanil_4.setGeometry(QtCore.QRect(30, 580, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dcl_Emanil_4.setFont(font)
        self.dcl_Emanil_4.setStyleSheet("background-color: rgb(59, 43, 1);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "")
        self.dcl_Emanil_4.setObjectName("dcl_Emanil_4")
        self.dclEmail_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.dclEmail_2.setGeometry(QtCore.QRect(190, 480, 231, 31))
        self.dclEmail_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "")
        self.dclEmail_2.setObjectName("dclEmail_2")
        self.dlcEmail_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.dlcEmail_3.setGeometry(QtCore.QRect(190, 530, 231, 31))
        self.dlcEmail_3.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "")
        self.dlcEmail_3.setObjectName("dlcEmail_3")
        self.dclEmail_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.dclEmail_4.setGeometry(QtCore.QRect(190, 580, 231, 31))  # (190, 630, 231, 31)
        self.dclEmail_4.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "")
        self.dclEmail_4.setObjectName("dclEmail_4")
        self.graphicsView_3.raise_()
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.dclUpdate.raise_()
        self.label.raise_()
        self.graphicsView_4.raise_()
        self.dvlDelete.raise_()
        # self.dvlClear.raise_()
        self.dlBack.raise_()
        self.label_2.raise_()
        self.dcl_id.raise_()
        self.dcl_name.raise_()
        self.dclExp.raise_()
        self.dcl_age.raise_()
        self.dclPhone.raise_()
        self.dclPlace.raise_()
        self.dcl_Emanil.raise_()
        self.dlcid.raise_()
        self.dclname.raise_()
        self.dclage.raise_()
        self.dcl_exp.raise_()
        self.dcl_place.raise_()
        self.dclPhone_2.raise_()
        # self.dcclEmail.raise_()
        self.dcl_search_entry.raise_()
        self.dCl_search.raise_()
        self.label_10.raise_()
        self.dcl_comboBox.raise_()
        self.tableWidget.raise_()
        self.dcl_Email_2.raise_()
        self.dcl_Emanil_3.raise_()
        self.dcl_Emanil_4.raise_()
        self.dclEmail_2.raise_()
        self.dlcEmail_3.raise_()
        self.dclEmail_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dlBack.clicked.connect(lambda: self.hmclosescr(MainWindow))
        self.dclUpdate.clicked.connect(self.Assigndoc)

    def Assigndoc(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = AssignDoctor()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def hmclosescr(self, MainWindow):
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dclUpdate.setText(_translate("MainWindow", "ADD"))
        self.label.setText(_translate("MainWindow", "HOSPITAL CASE LIST"))
        self.dvlDelete.setText(_translate("MainWindow", "DELETE"))
        # self.dvlClear.setText(_translate("MainWindow", "CLEAR"))
        self.dlBack.setText(_translate("MainWindow", "<-BACK"))
        self.label_2.setWhatsThis(_translate("MainWindow",
                                             "<html><head/><body><p>background-color: rgb(217, 217, 217);</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "     DETAILS"))
        self.dcl_id.setText(_translate("MainWindow", "  Case_id"))
        self.dcl_name.setText(_translate("MainWindow", "  Name"))
        self.dclExp.setText(_translate("MainWindow", "  Date"))
        self.dcl_age.setText(_translate("MainWindow", "  Type"))
        self.dclPhone.setText(_translate("MainWindow", "  Location"))
        self.dclPlace.setText(_translate("MainWindow", "  Time"))
        # self.dcl_Emanil.setText(_translate("MainWindow", "  Email"))
        self.dCl_search.setText(_translate("MainWindow", "SEARCH"))
        self.dCl_search.clicked.connect(self.search_data_case)
        self.label_10.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p>background-color: rgb(217, 217, 217);</p><p><br/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "  SEARCH BY"))
        self.dcl_comboBox.setItemText(0, _translate("MainWindow", "c_id"))
        self.dcl_comboBox.setItemText(1, _translate("MainWindow", "c_name"))
        self.dcl_comboBox.setItemText(2, _translate("MainWindow", "c_typr"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Case_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Location"))
        # item = self.tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Police"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Police_Station"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Doctor"))
        self.dcl_Email_2.setText(_translate("MainWindow", "  Police"))
        self.dcl_Emanil_3.setText(_translate("MainWindow", "  Police_st"))
        self.dcl_Emanil_4.setText(_translate("MainWindow", "  Doctor"))
        self.__load_case_data()
        self.dvlDelete.clicked.connect(self.delete_data)
        # self.tableWidget.cellClicked.connect(self.get_cursor)

    def __load_case_data(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cur = conn.cursor()
        cur.execute("select c_id, c_name,c_typr,c_date,c_time,c_location,p_id,pst_id,d_id from case_ where h_id=?;",
                    (GlobalStatic.hospital_id))
        rows = cur.fetchall()
        self.tableWidget.setRowCount(50)
        tableindex = 0

        self.__all_cases_list = rows

        for row in rows:
            print(row)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tableindex, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tableindex, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tableindex, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tableindex, 8, QtWidgets.QTableWidgetItem(row[8]))
            tableindex += 1
            conn.commit()
        conn.close()

    def _cell_clicked(self, row_index, column_index):
        # print(f"Signal received: {row} {column}")
        row = self.__all_cases_list[row_index]
        print(f"Case selected: {row}")
        GlobalStatic.set_case_info(row)
        GlobalStatic.test = True
        print(f"Setting test to True")
        GlobalStatic.set_case_info(row)

        self.dlcid.setText(row[0])
        self.dclname.setText(row[1])
        self.dclage.setText(row[2])
        self.dcl_exp.setText(row[3])
        self.dcl_place.setText(row[4])
        self.dclPhone_2.setText(row[5])
        self.dclEmail_2.setText(row[6])
        self.dlcEmail_3.setText(row[7])
        self.dclEmail_4.setText(row[8])

    def delete_data(self):
        msg = QMessageBox()

        # conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cur = conn.cursor()
        cur.execute("Update case_ set h_id = NULL where c_id = ?", (GlobalStatic.case_info_tuple[0]))
        conn.commit()
        msg.setText("Successfully Deleted!!")
        msg.setWindowTitle("Success")
        # self.fetch_data()
        # self.clear()
        conn.close()
        msg.setText("Successfully Deleted!!")
        msg.setWindowTitle("Success")
        msg.exec_()


    def search_data_case(self):
        # conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-EAC2CGC\KAUSHIK;"
            "Database=forensic;"
            "Trusted_Connection=yes;"
        )
        cur = conn.cursor()

        query = f"SELECT c_id, c_name,c_typr,c_date,c_time,c_location,p_id,pst_id,d_id from case_ WHERE {self.dcl_comboBox.currentText()} LIKE '%{self.dcl_search_entry.text()}%'"
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

