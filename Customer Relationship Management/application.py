from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Applications(object):
    def setupUi(self, Applications):
        Applications.setObjectName("Applications")
        Applications.resize(850, 640)
        Applications.setMinimumSize(QtCore.QSize(850, 640))
        Applications.setMaximumSize(QtCore.QSize(850, 640))
        Applications.setStyleSheet("QWidget {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #5E9D56, stop:1 #58A9D9);\n"
"\n"
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
        self.applications_search_line = QtWidgets.QLineEdit(parent=Applications)
        self.applications_search_line.setGeometry(QtCore.QRect(50, 188, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applications_search_line.setFont(font)
        self.applications_search_line.setStyleSheet("background-color: rgb(194, 255, 255);")
        self.applications_search_line.setText("")
        self.applications_search_line.setObjectName("applications_search_line")
        self.applications_table = QtWidgets.QTableWidget(parent=Applications)
        self.applications_table.setGeometry(QtCore.QRect(50, 418, 741, 131))
        self.applications_table.setStyleSheet("background-color: rgb(185, 252, 255);\n"
"color: rgb(0, 0, 0);")
        self.applications_table.setRowCount(0)
        self.applications_table.setColumnCount(7)
        self.applications_table.setObjectName("applications_table")
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_table.setHorizontalHeaderItem(6, item)
        self.applications_table.horizontalHeader().setCascadingSectionResizes(False)
        self.applications_table.horizontalHeader().setDefaultSectionSize(135)
        self.applications_all_button = QtWidgets.QPushButton(parent=Applications)
        self.applications_all_button.setGeometry(QtCore.QRect(540, 258, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.applications_all_button.setFont(font)
        self.applications_all_button.setStyleSheet("")
        self.applications_all_button.setObjectName("applications_all_button")
        self.applications_defined_button = QtWidgets.QPushButton(parent=Applications)
        self.applications_defined_button.setGeometry(QtCore.QRect(51, 258, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.applications_defined_button.setFont(font)
        self.applications_defined_button.setStyleSheet("")
        self.applications_defined_button.setObjectName("applications_defined_button")
        self.applications_undefined_button = QtWidgets.QPushButton(parent=Applications)
        self.applications_undefined_button.setGeometry(QtCore.QRect(51, 338, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.applications_undefined_button.setFont(font)
        self.applications_undefined_button.setStyleSheet("")
        self.applications_undefined_button.setObjectName("applications_undefined_button")
        self.applications_search_button = QtWidgets.QPushButton(parent=Applications)
        self.applications_search_button.setGeometry(QtCore.QRect(670, 188, 121, 41))
        self.applications_search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/search.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.applications_search_button.setIcon(icon)
        self.applications_search_button.setProperty("ico n", icon)
        self.applications_search_button.setObjectName("applications_search_button")
        self.pushButton_geriDon = QtWidgets.QPushButton(parent=Applications)
        self.pushButton_geriDon.setGeometry(QtCore.QRect(450, 338, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_geriDon.setFont(font)
        self.pushButton_geriDon.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/return.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_geriDon.setIcon(icon1)
        self.pushButton_geriDon.setObjectName("pushButton_geriDon")
        self.applications_title_label = QtWidgets.QLabel(parent=Applications)
        self.applications_title_label.setGeometry(QtCore.QRect(-10, 0, 871, 141))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.applications_title_label.setFont(font)
        self.applications_title_label.setStyleSheet("QWidget {\n"
"    font: bold 32px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #A1C4E9, stop:0.5 #C2D9F0, stop:1 #7A9EB9);\n"
"\n"
"\n"
"    text-shadow: 1px 1px 3px #003366;\n"
"    border-radius: 18px;\n"
"}")
        self.applications_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.applications_title_label.setObjectName("applications_title_label")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=Applications)
        self.pushButton_Exit.setGeometry(QtCore.QRect(645, 565, 145, 51))
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

        self.retranslateUi(Applications)
        QtCore.QMetaObject.connectSlotsByName(Applications)

    def retranslateUi(self, Applications):
        _translate = QtCore.QCoreApplication.translate
        Applications.setWindowTitle(_translate("Applications", "Application"))
        self.applications_search_line.setPlaceholderText(_translate("Applications", "  Search application"))
        item = self.applications_table.horizontalHeaderItem(0)
        item.setText(_translate("Applications", "Date"))
        item = self.applications_table.horizontalHeaderItem(1)
        item.setText(_translate("Applications", "Name"))
        item = self.applications_table.horizontalHeaderItem(2)
        item.setText(_translate("Applications", "New Column"))
        item = self.applications_table.horizontalHeaderItem(3)
        item.setText(_translate("Applications", "Phone"))
        item = self.applications_table.horizontalHeaderItem(4)
        item.setText(_translate("Applications", "Post Code"))
        item = self.applications_table.horizontalHeaderItem(5)
        item.setText(_translate("Applications", "State"))
        item = self.applications_table.horizontalHeaderItem(6)
        item.setText(_translate("Applications", "Status"))
        self.applications_all_button.setText(_translate("Applications", " All Applications"))
        self.applications_defined_button.setText(_translate("Applications", "Mentor Meeting (Defined)"))
        self.applications_undefined_button.setText(_translate("Applications", "Mentor Meeting (Undefined)"))
        self.pushButton_geriDon.setText(_translate("Applications", "Back To Preview-Menu"))
        self.applications_title_label.setText(_translate("Applications", "APPLICATIONS"))
        self.pushButton_Exit.setText(_translate("Applications", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Applications = QtWidgets.QWidget()
    ui = Ui_Applications()
    ui.setupUi(Applications)
    Applications.show()
    sys.exit(app.exec())
