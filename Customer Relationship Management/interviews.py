# Form implementation generated from reading ui file 'interviews.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Interviews(object):
    def setupUi(self, Interviews):
        Interviews.setObjectName("Interviews")
        Interviews.resize(1024, 860)
        Interviews.setMinimumSize(QtCore.QSize(1024, 860))
        Interviews.setMaximumSize(QtCore.QSize(1024, 860))
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
        self.interviews_submit_button = QtWidgets.QPushButton(parent=Interviews)
        self.interviews_submit_button.setGeometry(QtCore.QRect(670, 300, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.interviews_submit_button.setFont(font)
        self.interviews_submit_button.setStyleSheet("")
        self.interviews_submit_button.setObjectName("interviews_submit_button")
        self.interviews_search_line = QtWidgets.QLineEdit(parent=Interviews)
        self.interviews_search_line.setGeometry(QtCore.QRect(90, 210, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.interviews_search_line.setFont(font)
        self.interviews_search_line.setStyleSheet("")
        self.interviews_search_line.setFrame(True)
        self.interviews_search_line.setPlaceholderText("  Search")
        self.interviews_search_line.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.interviews_search_line.setObjectName("interviews_search_line")
        self.interviews_table = QtWidgets.QTableWidget(parent=Interviews)
        self.interviews_table.setGeometry(QtCore.QRect(40, 370, 961, 321))
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
        self.interviews_table.horizontalHeader().setDefaultSectionSize(300)
        self.interviews_table.horizontalHeader().setStretchLastSection(True)
        self.interviews_table.verticalHeader().setMinimumSectionSize(24)
        self.pushButton_Exit = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_Exit.setGeometry(QtCore.QRect(800, 733, 145, 51))
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
        self.interviews_title_label.setGeometry(QtCore.QRect(-20, 0, 1101, 171))
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
        self.interviews_search_button = QtWidgets.QPushButton(parent=Interviews)
        self.interviews_search_button.setGeometry(QtCore.QRect(760, 210, 175, 44))
        self.interviews_search_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/search.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.interviews_search_button.setIcon(icon1)
        self.interviews_search_button.setObjectName("interviews_search_button")
        self.pushButton_geriDon = QtWidgets.QPushButton(parent=Interviews)
        self.pushButton_geriDon.setGeometry(QtCore.QRect(90, 740, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_geriDon.setFont(font)
        self.pushButton_geriDon.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/return.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_geriDon.setIcon(icon2)
        self.pushButton_geriDon.setObjectName("pushButton_geriDon")

        self.retranslateUi(Interviews)
        QtCore.QMetaObject.connectSlotsByName(Interviews)

    def retranslateUi(self, Interviews):
        _translate = QtCore.QCoreApplication.translate
        Interviews.setWindowTitle(_translate("Interviews", "Interviews"))
        self.interviews_submit_button.setText(_translate("Interviews", "Project Submitted"))
        item = self.interviews_table.horizontalHeaderItem(0)
        item.setText(_translate("Interviews", "Name"))
        item = self.interviews_table.horizontalHeaderItem(1)
        item.setText(_translate("Interviews", "Project Received Date"))
        item = self.interviews_table.horizontalHeaderItem(2)
        item.setText(_translate("Interviews", "Project Submission Date"))
        self.pushButton_Exit.setText(_translate("Interviews", "Exit"))
        self.interviews_title_label.setText(_translate("Interviews", "INTERVIEWS"))
        self.pushButton_geriDon.setText(_translate("Interviews", "Back To Preview-Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interviews = QtWidgets.QWidget()
    ui = Ui_Interviews()
    ui.setupUi(Interviews)
    Interviews.show()
    sys.exit(app.exec())
