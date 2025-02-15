from PyQt6.QtWidgets import *
import sys
from preference_menu_user import Ui_Preference_menu_user 
from application import Ui_Applications
from mentor_interview import Ui_MentorInterview
from interviews import Ui_Interviews



class UserPreferenceMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Preference_menu_user()
        self.ui.setupUi(self)

    
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_applications.clicked.connect(self.open_applications)
        print("pushButton_applications bağlandı.")
        
        self.ui.pushButton_mentorMeeting.clicked.connect(self.open_mentor_interview)
        print("pushButton_mentorMeeting bağlandı.")
        
        self.ui.pushButton_interviews.clicked.connect(self.open_interviews)
        print("pushButton_interviews bağlandı.")
        

        # Yeni pencereleri saklamak için değişkenler
        self.applications_window = None
        self.mentor_interview_window = None
        self.interviews_window = None
        

    def open_applications(self):
        """Applications ekranını açar"""
        self.applications_window = QMainWindow()  # Applications penceresini başlat
        self.applications_ui = Ui_Applications()  # Applications UI'sini yükle
        self.applications_ui.setupUi(self.applications_window)  # UI'yi pencereye uygula
        self.applications_window.show()  # Applications ekranını göster
        self.close()

    def open_mentor_interview(self):
        self.mentor_interview_window = QMainWindow()
        self.mentor_interview_ui = Ui_MentorInterview()
        self.mentor_interview_ui.setupUi(self.mentor_interview_window)
        self.mentor_interview_window.show()
        self.close()

    def open_interviews(self):
        """Interviews ekranını açar"""
        self.interviews_window = QMainWindow()  # Interviews penceresini başlat
        self.interviews_ui = Ui_Interviews()  # Interviews UI'sini yükle
        self.interviews_ui.setupUi(self.interviews_window)  # UI'yi pencereye uygula
        self.interviews_window.show()  # Interviews ekranını göster
        self.close()
