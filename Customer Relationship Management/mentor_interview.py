from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MentorInterview(object):
    def setupUi(self, MentorInterview):
        MentorInterview.setObjectName("MentorInterview")
        MentorInterview.resize(850, 640)
        MentorInterview.setMinimumSize(QtCore.QSize(850, 640))
        MentorInterview.setMaximumSize(QtCore.QSize(850, 640))
        MentorInterview.setStyleSheet("QWidget {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #66B77D, stop:1 #57A8D9);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #2196F3;\n"
"    border-radius: 16px;\n"
"    border: 2px solid #1976D2;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"    box-shadow: 0 4px #1976D2;\n"
"    transition: all 0.3s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #42A5F5;\n"
"    box-shadow: 0 8px #1976D2;\n"
"    transform: scale(1.2);  /* Butonu büyüt */\n"
"    font-size: 22px; /* Yazıyı büyüt */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E88E5;\n"
"    box-shadow: 0 2px #1976D2;\n"
"    transform: scale(1.1); /* Basılınca biraz küçült */\n"
"    font-size: 30px; /* Yazıyı biraz küçült */\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(parent=MentorInterview)
        self.label.setGeometry(QtCore.QRect(-20, 0, 881, 141))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget {\n"
"    font: bold 32px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"    stop:0 #A4C4E9, stop:0.5 #C1D8F0, stop:1 #5F84B8);\n"
"\n"
"\n"
"    text-shadow: 1px 1px 3px #003366;\n"
"    border-radius: 18px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.applications_search_line = QtWidgets.QLineEdit(parent=MentorInterview)
        self.applications_search_line.setGeometry(QtCore.QRect(50, 200, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.applications_search_line.setFont(font)
        self.applications_search_line.setStyleSheet("background-color: rgb(197, 255, 254);\n"
"color: rgb(0, 0, 0);")
        self.applications_search_line.setText("")
        self.applications_search_line.setObjectName("applications_search_line")
        self.interviews_search_button = QtWidgets.QPushButton(parent=MentorInterview)
        self.interviews_search_button.setGeometry(QtCore.QRect(650, 200, 151, 44))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/search.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.interviews_search_button.setIcon(icon)
        self.interviews_search_button.setObjectName("interviews_search_button")
        self.pushButton_tumGorusmeler = QtWidgets.QPushButton(parent=MentorInterview)
        self.pushButton_tumGorusmeler.setGeometry(QtCore.QRect(580, 270, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_tumGorusmeler.setFont(font)
        self.pushButton_tumGorusmeler.setObjectName("pushButton_tumGorusmeler")
        self.comboBox_ = QtWidgets.QComboBox(parent=MentorInterview)
        self.comboBox_.setGeometry(QtCore.QRect(50, 270, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_.setFont(font)
        self.comboBox_.setStyleSheet("background-color: rgb(198, 255, 249);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_.setObjectName("comboBox_")
        self.comboBox_.addItem("")
        self.tableWidget_butunGorusmeler = QtWidgets.QTableWidget(parent=MentorInterview)
        self.tableWidget_butunGorusmeler.setGeometry(QtCore.QRect(50, 340, 751, 191))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidget_butunGorusmeler.setFont(font)
        self.tableWidget_butunGorusmeler.setStyleSheet("background-color: rgb(201, 255, 254);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget_butunGorusmeler.setObjectName("tableWidget_butunGorusmeler")
        self.tableWidget_butunGorusmeler.setColumnCount(6)
        self.tableWidget_butunGorusmeler.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(5, item)
        self.tableWidget_butunGorusmeler.horizontalHeader().setDefaultSectionSize(131)
        self.pushButton_geriDon = QtWidgets.QPushButton(parent=MentorInterview)
        self.pushButton_geriDon.setGeometry(QtCore.QRect(50, 550, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_geriDon.setFont(font)
        self.pushButton_geriDon.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/return.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_geriDon.setIcon(icon1)
        self.pushButton_geriDon.setObjectName("pushButton_geriDon")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=MentorInterview)
        self.pushButton_Exit.setGeometry(QtCore.QRect(657, 550, 145, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setStyleSheet("QPushButton {\n"
"  background-color: #1565C0;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #1976D2;\n"
"    padding: 10px 20px;\n"
"    font-size: 22px;\n"
"    color: white;\n"
"    box-shadow: 0 4px #1976D2;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #42A5F5;\n"
"    box-shadow: 0 6px #1976D2;\n"
"    transform: translateY(-4px);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E88E5;\n"
"    box-shadow: 0 2px #1976D2;\n"
"    transform: translateY(2px);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/exit.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Exit.setIcon(icon2)
        self.pushButton_Exit.setObjectName("pushButton_Exit")

        self.retranslateUi(MentorInterview)
        QtCore.QMetaObject.connectSlotsByName(MentorInterview)

    def retranslateUi(self, MentorInterview):
        _translate = QtCore.QCoreApplication.translate
        MentorInterview.setWindowTitle(_translate("MentorInterview", "Mentor Interview"))
        self.label.setText(_translate("MentorInterview", "MENTOR INTERVIEW"))
        self.applications_search_line.setPlaceholderText(_translate("MentorInterview", "  Search application"))
        self.interviews_search_button.setText(_translate("MentorInterview", "Search"))
        self.pushButton_tumGorusmeler.setText(_translate("MentorInterview", "All Interviews"))
        self.comboBox_.setItemText(0, _translate("MentorInterview", "Selelct an option..."))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(0)
        item.setText(_translate("MentorInterview", "Date"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(1)
        item.setText(_translate("MentorInterview", "Name"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(2)
        item.setText(_translate("MentorInterview", "Mentor"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(3)
        item.setText(_translate("MentorInterview", "IT Experience"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(4)
        item.setText(_translate("MentorInterview", "Intensity Status"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(5)
        item.setText(_translate("MentorInterview", "Comment"))
        self.pushButton_geriDon.setText(_translate("MentorInterview", "Back To Preview-Menu"))
        self.pushButton_Exit.setText(_translate("MentorInterview", "Exit"))
