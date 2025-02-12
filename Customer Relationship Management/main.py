import sys
from PyQt6.QtWidgets import *
from login import Ui_LoginWindow
from preference_menu_admin import Ui_preference_menu_admin
from preference_menu_user import Ui_Preference_menu_user
from application import Ui_Applications
from admin_menu import Ui_AdminMenu
from interviews import Ui_Interviews
from mentor_interview import Ui_MentorInterview


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()  # Login arayüzünü (.ui dosyasından çevrilen Python kodunu) çağırır.
        self.ui.setupUi(self)  # Arayüzü pencereye uygula

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = LoginWindow()
    pencere.show()
    uygulama.exec()