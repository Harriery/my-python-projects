from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Interviews(object):
    def setupUi(self, Interviews):
        Interviews.setObjectName("Interviews")
        Interviews.resize(850, 640)
        Interviews.setMinimumSize(QtCore.QSize(850, 640))
        Interviews.setMaximumSize(QtCore.QSize(850, 640))
        Interviews.setStyleSheet("QWidget {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #7A9A5D, stop:1 #7AB9FF);\n"
"\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #2196F3;\n"
"    border-radius: 16px;\n"
"    border: 2px solid #1976D2;\n"
"    padding: 10px 20px;\n"
"    font-size: 22px;\n"
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
        self.pushButton_project_submitted = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_project_submitted.setGeometry(QtCore.QRect(560, 250, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_project_submitted.setFont(font)
        self.pushButton_project_submitted.setStyleSheet("")
        self.pushButton_project_submitted.setObjectName("pushButton_project_submitted")
        self.interviews_search_line = QtWidgets.QLineEdit(parent=Interviews)
        self.interviews_search_line.setGeometry(QtCore.QRect(50, 170, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.interviews_search_line.setFont(font)
        self.interviews_search_line.setStyleSheet("background-color: rgb(202, 255, 254);\n"
"color: rgb(0, 0, 0);")
        self.interviews_search_line.setFrame(True)
        self.interviews_search_line.setPlaceholderText("  Search")
        self.interviews_search_line.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.interviews_search_line.setObjectName("interviews_search_line")
        self.interviews_table = QtWidgets.QTableWidget(parent=Interviews)
        self.interviews_table.setGeometry(QtCore.QRect(40, 310, 761, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.interviews_table.setFont(font)
        self.interviews_table.setStyleSheet("background-color: rgb(192, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.interviews_table.setRowCount(17)
        self.interviews_table.setColumnCount(3)
        self.interviews_table.setObjectName("interviews_table")
        item = QtWidgets.QTableWidgetItem()
        self.interviews_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.interviews_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.interviews_table.setHorizontalHeaderItem(2, item)
        self.interviews_table.horizontalHeader().setCascadingSectionResizes(False)
        self.interviews_table.horizontalHeader().setDefaultSectionSize(208)
        self.interviews_table.horizontalHeader().setStretchLastSection(True)
        self.interviews_table.verticalHeader().setMinimumSectionSize(24)
        self.pushButton_Exit = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_Exit.setGeometry(QtCore.QRect(660, 540, 145, 51))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/exit.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Exit.setIcon(icon)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.interviews_title_label = QtWidgets.QLabel(parent=Interviews)
        self.interviews_title_label.setGeometry(QtCore.QRect(-40, 0, 901, 141))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.interviews_title_label.setFont(font)
        self.interviews_title_label.setStyleSheet("QWidget {\n"
"    font: bold 32px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #A1C4E9, stop:0.3 #C2D9F0, stop:0.7 #A5B8C9, stop:1 #7A9EB9);\n"
"\n"
"\n"
"\n"
"    text-shadow: 1px 1px 3px #003366;\n"
"    border-radius: 18px;\n"
"}")
        self.interviews_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.interviews_title_label.setObjectName("interviews_title_label")
        self.pushButton_search = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_search.setGeometry(QtCore.QRect(640, 170, 151, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/search.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_search.setIcon(icon1)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_geriDon = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_geriDon.setGeometry(QtCore.QRect(40, 540, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_geriDon.setFont(font)
        self.pushButton_geriDon.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/return.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_geriDon.setIcon(icon2)
        self.pushButton_geriDon.setObjectName("pushButton_geriDon")
        self.pushButton_incoming_projects = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_incoming_projects.setGeometry(QtCore.QRect(40, 250, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_incoming_projects.setFont(font)
        self.pushButton_incoming_projects.setStyleSheet("")
        self.pushButton_incoming_projects.setObjectName("pushButton_incoming_projects")

        self.retranslateUi(Interviews)
        QtCore.QMetaObject.connectSlotsByName(Interviews)

    def retranslateUi(self, Interviews):
        _translate = QtCore.QCoreApplication.translate
        Interviews.setWindowTitle(_translate("Interviews", "Interviews"))
        self.pushButton_project_submitted.setText(_translate("Interviews", "Project Submitted"))
        item = self.interviews_table.horizontalHeaderItem(0)
        item.setText(_translate("Interviews", "Name"))
        item = self.interviews_table.horizontalHeaderItem(1)
        item.setText(_translate("Interviews", "Project Received Date"))
        item = self.interviews_table.horizontalHeaderItem(2)
        item.setText(_translate("Interviews", "Project Submission Date"))
        self.pushButton_Exit.setText(_translate("Interviews", "Exit"))
        self.interviews_title_label.setText(_translate("Interviews", "INTERVIEWS"))
        self.pushButton_search.setText(_translate("Interviews", "Search"))
        self.pushButton_geriDon.setText(_translate("Interviews", "Back To Preview-Menu"))
        self.pushButton_incoming_projects.setText(_translate("Interviews", "Incoming Projects"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interviews = QtWidgets.QWidget()
    ui = Ui_Interviews()
    ui.setupUi(Interviews)
    Interviews.show()
    sys.exit(app.exec())
