from PyQt6.QtWidgets import *
import sys
from preference_menu_admin import Ui_preference_menu_admin 
from application import Ui_Applications
from mentor_interview import Ui_MentorInterview
from interviews import Ui_Interviews
from admin_menu import Ui_AdminMenu


class AdminPreferenceMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_preference_menu_admin()
        self.ui.setupUi(self)

        print("AdminPreferenceMenuWindow yüklendi.")
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_applications_2.clicked.connect(self.open_applications)
        print("pushButton_applications_2 bağlandı.")
        
        self.ui.pushButton_mentorMeeting.clicked.connect(self.open_mentor_interview)
        print("pushButton_mentorMeeting bağlandı.")
        
        self.ui.pushButton_interviews.clicked.connect(self.open_interviews)
        print("pushButton_interviews bağlandı.")
        
        self.ui.pushButton_adminMenu.clicked.connect(self.open_admin_menu)
        print("pushButton_adminMenu bağlandı.")


        # Yeni pencereleri saklamak için değişkenler
        self.applications_window = None
        self.mentor_interview_window = None
        self.interviews_window = None
        self.admin_menu_window = None

    def open_applications(self):
        print("Applications butonuna basıldı.") 
        self.applications_window = QMainWindow()  # Yeni pencere oluştur
        ui = Ui_Applications()
        ui.setupUi(self.applications_window)  
        self.applications_window.show()  # Pencereyi göster
        self.close()  # Mevcut pencereyi kapat

    def open_mentor_interview(self):
        print("Mentor Interview butonuna basıldı.")
        self.mentor_interview_window = QMainWindow()
        ui = Ui_MentorInterview()
        ui.setupUi(self.mentor_interview_window)
        self.mentor_interview_window.show()
        self.close()

    def open_interviews(self):
        print("Interviews butonuna basıldı.")
        self.interviews_window = QMainWindow()
        ui = Ui_Interviews()
        ui.setupUi(self.interviews_window)
        self.interviews_window.show()
        self.close()

    def open_admin_menu(self):
        print("Admin Menu butonuna basıldı.")
        self.admin_menu_window = QMainWindow()
        ui = Ui_AdminMenu()
        ui.setupUi(self.admin_menu_window)
        self.admin_menu_window.show()
        self.close()
