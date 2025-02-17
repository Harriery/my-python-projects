from PyQt6.QtWidgets import *
import sys
from preference_menu_admin import Ui_preference_menu_admin 
from application import Ui_Applications
from mentor_interview import Ui_MentorInterview
from interviews import Ui_Interviews
from admin_menu import Ui_AdminMenu
from mentor_interviews_function import MentorInterviewsWindow
from application_function import Application_Window
from interviews_function import Interview_Window


class AdminPreferenceMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_preference_menu_admin()
        self.ui.setupUi(self)

        print("AdminPreferenceMenuWindow yüklendi.")
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_applications_2.clicked.connect(self.open_application)
        print("pushButton_applications_2 bağlandı.")
        
        self.ui.pushButton_mentorMeeting.clicked.connect(self.open_mentor_interview)
        print("pushButton_mentorMeeting bağlandı.")
        
        self.ui.pushButton_interviews.clicked.connect(self.open_interviews)
        print("pushButton_interviews bağlandı.")
        
        self.ui.pushButton_adminMenu.clicked.connect(self.open_admin_menu)
        print("pushButton_adminMenu bağlandı.")

        self.ui.pushButton_Exit.clicked.connect(self.exit)
        


        # Yeni pencereleri saklamak için değişkenler
        self.applications_window = None
        self.mentor_interview_window = None
        self.interviews_window = None
        self.admin_menu_window = None

    def exit(self):
       """Pencereyi kapatır ve uygulamadan çıkar."""
       try:
           self.close()  # Mevcut pencereyi kapat
           print("Pencere başarıyla kapatıldı.")
       except Exception as e:
           print(f"Pencere kapatılırken hata oluştu: {e}")

    def open_application(self):
        print("Application butonuna basıldı Admin olarak açılıyor).")
        self.application_window = Application_Window(user_type="admin")  # User olduğunu belirtiyoruz
        self.application_window.show()
        self.close()

    def open_mentor_interview(self):
        print("Mentor Interview butonuna basıldı.")
        self.mentor_interview_window = MentorInterviewsWindow(user_type="admin")
        self.mentor_interview_window.show()
        self.close()  # Mevcut pencereyi kapat

    def open_interviews(self):
        print("Interviews butonuna basıldı.")
        self.interviews_window =Interview_Window(user_type="admin")
        self.interviews_window.show()
        self.close()

    def open_admin_menu(self):
        print("Admin Menu butonuna basıldı.")
        self.admin_menu_window = QMainWindow()
        ui = Ui_AdminMenu()
        ui.setupUi(self.admin_menu_window)
        self.admin_menu_window.show()
        self.close()
