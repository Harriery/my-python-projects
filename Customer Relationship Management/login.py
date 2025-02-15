from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(500, 600)
        LoginWindow.setMinimumSize(QtCore.QSize(500, 600))
        LoginWindow.setMaximumSize(QtCore.QSize(500, 600))
        LoginWindow.setStyleSheet("QWidget {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #7CCBA2, stop:1 #5FAFD3);\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #2196F3;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #1976D2;\n"
"    padding: 10px 20px;\n"
"    font-size: 22px;\n"
"    color: white;\n"
"    box-shadow: 0 4px #1976D2;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
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
"}\n"
"")
        self.pushButton_login = QtWidgets.QPushButton(parent=LoginWindow)
        self.pushButton_login.setGeometry(QtCore.QRect(140, 390, 231, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_cikis = QtWidgets.QPushButton(parent=LoginWindow)
        self.pushButton_cikis.setGeometry(QtCore.QRect(169, 500, 169, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_cikis.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/exit.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cikis.setIcon(icon)
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.label_2 = QtWidgets.QLabel(parent=LoginWindow)
        self.label_2.setGeometry(QtCore.QRect(77, 279, 345, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QWidget {\n"
"    font: bold 18px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #C2D9F0, stop:1 #85B1CF);\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=LoginWindow)
        self.label.setGeometry(QtCore.QRect(80, 190, 345, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget {\n"
"    font: bold 18px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #C2D9F0, stop:1 #85B1CF);\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_userName = QtWidgets.QLineEdit(parent=LoginWindow)
        self.lineEdit_userName.setGeometry(QtCore.QRect(83, 220, 341, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_userName.sizePolicy().hasHeightForWidth())
        self.lineEdit_userName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setStyleSheet("color: black;")
        self.lineEdit_userName.setText("")
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=LoginWindow)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 310, 341, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setStyleSheet("color: black;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_3 = QtWidgets.QLabel(parent=LoginWindow)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 511, 151))
        self.label_3.setStyleSheet("QWidget {\n"
"    font: bold 22px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #C2D9F0, stop:1 #85B1CF);\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.pushButton_login.setText(_translate("LoginWindow", "Login"))
        self.pushButton_cikis.setText(_translate("LoginWindow", "Exit"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.label.setText(_translate("LoginWindow", "User Name"))
        self.label_3.setText(_translate("LoginWindow", "CUSTOMER RELATIONSHIP MANAGEMENT (CRM)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
