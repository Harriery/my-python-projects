from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_preference_menu_admin(object):
    def setupUi(self, preference_menu_admin):
        preference_menu_admin.setObjectName("preference_menu_admin")
        preference_menu_admin.resize(850, 640)
        preference_menu_admin.setMinimumSize(QtCore.QSize(850, 640))
        preference_menu_admin.setMaximumSize(QtCore.QSize(850, 640))
        preference_menu_admin.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"    stop:0 #77C5B5, stop:1 #6A9BB4);\n"
"}\n"
"\n"
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
        self.preference_title_label = QtWidgets.QLabel(parent=preference_menu_admin)
        self.preference_title_label.setGeometry(QtCore.QRect(0, 0, 861, 141))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.preference_title_label.setFont(font)
        self.preference_title_label.setStyleSheet("QWidget {\n"
"    font: bold 32px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"    stop:0 #9ABDE3, stop:0.5 #C3D9F0, stop:1 #6E8BB9);\n"
"\n"
"\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.preference_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.preference_title_label.setObjectName("preference_title_label")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=preference_menu_admin)
        self.pushButton_Exit.setGeometry(QtCore.QRect(600, 560, 145, 51))
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
        self.pushButton_adminMenu = QtWidgets.QPushButton(parent=preference_menu_admin)
        self.pushButton_adminMenu.setGeometry(QtCore.QRect(480, 219, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_adminMenu.setFont(font)
        self.pushButton_adminMenu.setObjectName("pushButton_adminMenu")
        self.pushButton_mentorMeeting = QtWidgets.QPushButton(parent=preference_menu_admin)
        self.pushButton_mentorMeeting.setGeometry(QtCore.QRect(90, 220, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_mentorMeeting.setFont(font)
        self.pushButton_mentorMeeting.setObjectName("pushButton_mentorMeeting")
        self.pushButton_interviews = QtWidgets.QPushButton(parent=preference_menu_admin)
        self.pushButton_interviews.setGeometry(QtCore.QRect(480, 390, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_interviews.setFont(font)
        self.pushButton_interviews.setObjectName("pushButton_interviews")
        self.pushButton_applications_2 = QtWidgets.QPushButton(parent=preference_menu_admin)
        self.pushButton_applications_2.setGeometry(QtCore.QRect(90, 390, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_applications_2.setFont(font)
        self.pushButton_applications_2.setObjectName("pushButton_applications_2")

        self.retranslateUi(preference_menu_admin)
        QtCore.QMetaObject.connectSlotsByName(preference_menu_admin)

    def retranslateUi(self, preference_menu_admin):
        _translate = QtCore.QCoreApplication.translate
        preference_menu_admin.setWindowTitle(_translate("preference_menu_admin", "Preference Menu (Admin)"))
        self.preference_title_label.setText(_translate("preference_menu_admin", "PREFERENCE MENU (ADMIN)"))
        self.pushButton_Exit.setText(_translate("preference_menu_admin", "Exit"))
        self.pushButton_adminMenu.setText(_translate("preference_menu_admin", "Admin Menu"))
        self.pushButton_mentorMeeting.setText(_translate("preference_menu_admin", "Mentor Meeting"))
        self.pushButton_interviews.setText(_translate("preference_menu_admin", "Interviews"))
        self.pushButton_applications_2.setText(_translate("preference_menu_admin", "Applications"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    preference_menu_admin = QtWidgets.QWidget()
    ui = Ui_preference_menu_admin()
    ui.setupUi(preference_menu_admin)
    preference_menu_admin.show()
    sys.exit(app.exec())
