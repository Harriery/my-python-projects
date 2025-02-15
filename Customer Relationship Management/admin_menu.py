from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminMenu(object):
    def setupUi(self, AdminMenu):
        AdminMenu.setObjectName("AdminMenu")
        AdminMenu.resize(850, 640)
        AdminMenu.setMinimumSize(QtCore.QSize(850, 640))
        AdminMenu.setMaximumSize(QtCore.QSize(850, 640))
        AdminMenu.setStyleSheet("QWidget {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #7CCBA2, stop:1 #5FAFD3);\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #2196F3;\n"
"    border-radius: 16px;\n"
"    border: 2px solid #1976D2;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    color: white;\n"
"    box-shadow: 0 4px #1976D2;\n"
"    transition: all 0.3s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #42A5F5;\n"
"    box-shadow: 0 8px #1976D2;\n"
"    transform: scale(1.2);  /* Butonu büyüt */\n"
"    font-size: 24px; /* Yazıyı büyüt */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E88E5;\n"
"    box-shadow: 0 2px #1976D2;\n"
"    transform: scale(1.1); /* Basılınca biraz küçült */\n"
"    font-size: 30px; /* Yazıyı biraz küçült */\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(parent=AdminMenu)
        self.label.setGeometry(QtCore.QRect(0, 0, 861, 141))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget {\n"
"    font: bold 28px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #9ABDE3, stop:0.3 #C3D9F0, stop:0.7 #A1B9C9, stop:1 #6E8BB9);\n"
"\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_mentorMeeting_4 = QtWidgets.QPushButton(parent=AdminMenu)
        self.pushButton_mentorMeeting_4.setGeometry(QtCore.QRect(837, 920, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_mentorMeeting_4.setFont(font)
        self.pushButton_mentorMeeting_4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_mentorMeeting_4.setObjectName("pushButton_mentorMeeting_4")
        self.pushButton_event_recording = QtWidgets.QPushButton(parent=AdminMenu)
        self.pushButton_event_recording.setGeometry(QtCore.QRect(50, 180, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_event_recording.setFont(font)
        self.pushButton_event_recording.setObjectName("pushButton_event_recording")
        self.pushButton_mail = QtWidgets.QPushButton(parent=AdminMenu)
        self.pushButton_mail.setGeometry(QtCore.QRect(630, 180, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_mail.setFont(font)
        self.pushButton_mail.setObjectName("pushButton_mail")
        self.tableWidget_butunGorusmeler = QtWidgets.QTableWidget(parent=AdminMenu)
        self.tableWidget_butunGorusmeler.setGeometry(QtCore.QRect(50, 260, 741, 281))
        self.tableWidget_butunGorusmeler.setStyleSheet("background-color: rgb(176, 255, 249);")
        self.tableWidget_butunGorusmeler.setObjectName("tableWidget_butunGorusmeler")
        self.tableWidget_butunGorusmeler.setColumnCount(4)
        self.tableWidget_butunGorusmeler.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_butunGorusmeler.setHorizontalHeaderItem(3, item)
        self.tableWidget_butunGorusmeler.horizontalHeader().setDefaultSectionSize(185)
        self.tableWidget_butunGorusmeler.horizontalHeader().setHighlightSections(False)
        self.pushButton_geriDon = QtWidgets.QPushButton(parent=AdminMenu)
        self.pushButton_geriDon.setGeometry(QtCore.QRect(50, 557, 426, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_geriDon.setFont(font)
        self.pushButton_geriDon.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/return.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_geriDon.setIcon(icon)
        self.pushButton_geriDon.setObjectName("pushButton_geriDon")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=AdminMenu)
        self.pushButton_Exit.setGeometry(QtCore.QRect(650, 560, 145, 51))
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
        self.pushButton_Exit.setObjectName("pushButton_Exit")

        self.retranslateUi(AdminMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminMenu)

    def retranslateUi(self, AdminMenu):
        _translate = QtCore.QCoreApplication.translate
        AdminMenu.setWindowTitle(_translate("AdminMenu", "Admin Menu"))
        self.label.setText(_translate("AdminMenu", "ADMIN MENU"))
        self.pushButton_mentorMeeting_4.setText(_translate("AdminMenu", "Exit"))
        self.pushButton_event_recording.setText(_translate("AdminMenu", "Event Recording"))
        self.pushButton_mail.setText(_translate("AdminMenu", "E-mail"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(0)
        item.setText(_translate("AdminMenu", "Meeting Title"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(1)
        item.setText(_translate("AdminMenu", "Start Time"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(2)
        item.setText(_translate("AdminMenu", "Participant E-mail"))
        item = self.tableWidget_butunGorusmeler.horizontalHeaderItem(3)
        item.setText(_translate("AdminMenu", "Organizer E-mail"))
        self.pushButton_geriDon.setText(_translate("AdminMenu", "Back To Preview-Menu"))
        self.pushButton_Exit.setText(_translate("AdminMenu", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminMenu = QtWidgets.QWidget()
    ui = Ui_AdminMenu()
    ui.setupUi(AdminMenu)
    AdminMenu.show()
    sys.exit(app.exec())
