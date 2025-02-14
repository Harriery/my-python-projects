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
        # Giriş butonuna tıklanınca `handle_login` fonksiyonunu çağır
        self.ui.pushButton_login.clicked.connect(self.handle_login)
          # Çıkış (exit) butonuna bağlantı kur
        self.ui.pushButton_cikis.clicked.connect(self.close_application)
    def handle_login(self):
        from login_funtions import validate_user  # Döngüsel import hatası almamak için burada import ettik.
        validate_user(self)  # Mevcut pencereyi parametre olarak gönderiyoruz.

    def close_application(self):
        """Exit butonuna basıldığında uygulamayı kapatır."""
        self.close()  # Mevcut pencereyi kapat

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = LoginWindow()
    pencere.show()
    uygulama.exec()