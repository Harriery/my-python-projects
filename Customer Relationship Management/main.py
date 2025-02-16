import sys
from PyQt6.QtWidgets import *
from login import Ui_LoginWindow
from preference_menu_admin import Ui_preference_menu_admin
from preference_menu_admin_function import AdminPreferenceMenuWindow
from preference_menu_user import Ui_Preference_menu_user
from application import Ui_Applications
from admin_menu import Ui_AdminMenu
from interviews import Ui_Interviews
from mentor_interview import Ui_MentorInterview
from mentor_interviews_function import MentorInterviewsWindow



# Kullanıcı menüsü sınıfı
class UserPreferenceMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Preference_menu_user()
        self.ui.setupUi(self)

        # Butonlara tıklanınca ilgili fonksiyonları çağır
        self.ui.pushButton_interviews.clicked.connect(self.open_interviews)
        self.ui.pushButton_applications.clicked.connect(self.open_applications)

    def open_interviews(self):
        print("Interviews butonuna basıldı.")
        self.interviews_window = QMainWindow()  # Yeni pencere oluştur
        ui = Ui_Interviews()  # Interview UI'sini yükle
        ui.setupUi(self.interviews_window)  # Pencereye UI'yi uygula
        self.interviews_window.show()  # Pencereyi göster

    def open_applications(self):
        print("Applications butonuna basıldı.")
        self.applications_window = QMainWindow()  # Yeni pencere oluştur
        ui = Ui_Applications()  # Applications UI'sini yükle
        ui.setupUi(self.applications_window)  # Pencereye UI'yi uygula
        self.applications_window.show()  # Pencereyi göster


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
        from login_functions import validate_user  # Döngüsel import hatası almamak için burada import ettik.
        validate_user(self)  # Mevcut pencereyi parametre olarak gönderiyoruz.

    def close_application(self):
        """Exit butonuna basıldığında uygulamayı kapatır."""
        self.close()  # Mevcut pencereyi kapat


def open_admin_menu():
    global login_window, admin_window
    login_window.close()  # Giriş ekranını kapat
    admin_window = AdminPreferenceMenuWindow()  # Admin menüsünü başlat
    admin_window.show()  # Admin menüsünü göster


def open_user_menu():
    global login_window, user_window
    login_window.close()  # Giriş ekranını kapat
    user_window = UserPreferenceMenuWindow()  # Kullanıcı menüsünü başlat
    user_window.show()  # Kullanıcı menüsünü göster


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login_window = LoginWindow()  # Giriş penceresini başlat
    login_window.show()

    sys.exit(app.exec())
