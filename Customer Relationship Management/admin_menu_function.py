from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import pandas as pd
import gdown
import sys
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from login_functions import validate_user, logged_in_user_data
from admin_menu import Ui_AdminMenu
from main import *

# Load environment variables
load_dotenv()

def download_and_read_admins():
    try:
        # Google Drive'dan dosya indirme
        urlBasvurular = 'https://drive.google.com/uc?id=19hfIbsIJ1f54aSwPPTNGIOAis26mibMk'  # Dosya ID'si ile doğru bağlantı
        outputBasvurular = 'Basvurular.xlsx'
        urlUsers = 'https://drive.google.com/uc?id=1SatXOBosige730jIOoR8UAeXQG4UA8Ph'  # Dosya ID'si ile doğru bağlantı
        outputUsers = 'users.xlsx'
        gdown.download(urlBasvurular, outputBasvurular, quiet=False)

        # Excel dosyasını okuma
        download_users = pd.read_excel(outputUsers)
        download_basvurular = pd.read_excel(outputBasvurular)
        # print(download_users.head())
        return download_users, download_basvurular  # Veriyi geri döndür
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

def get_admin_email():
    if logged_in_user_data is not None:
        return logged_in_user_data['e-mail']
    return None

downloaded_data = download_and_read_admins()
if downloaded_data is not None:
    download_users, download_basvurular = downloaded_data
    

class Admin_MenuFunction(QMainWindow):
    def __init__(self, user_type="admin"):
        super().__init__()
        self.ui = Ui_AdminMenu()
        self.ui.setupUi(self)
        self.user_type = user_type

        self.ui.pushButton_geriDon.clicked.connect(self.back_to_preference)
        print("pushButton_geriDon bağlandı.")
        self.ui.pushButton_Exit.clicked.connect(self.exit)
        print("pushButton_Exit bağlandı.")
        self.ui.pushButton_event_recording.clicked.connect(self.load_all_interviews)
        self.ui.pushButton_mail.clicked.connect(self.send_email)
        print("pushButton_mail bağlandı.")
    
    def exit(self):
        print("exit butonuna basıldı!")
    
        self.close()  # Pencereyi kapat
        sys.exit(0)   # Tüm uygulamayı kapat

    def back_to_preference(self):
        from preference_menu_user_function import UserPreferenceMenuWindow  
        from preference_menu_admin_function import AdminPreferenceMenuWindow  

        self.close()  # Mevcut pencereyi kapat

        # Kullanıcı veya admin menüsüne dön
        if self.user_type == "admin":
            print("Admin menüsüne geri dönülüyor...")
            self.preference_menu = AdminPreferenceMenuWindow()
        else:
            print("User menüsüne geri dönülüyor...")
            self.preference_menu = UserPreferenceMenuWindow()

        self.preference_menu.show()

   
    def load_all_interviews(self):
        try:
            for row_index, row_data in download_basvurular.iterrows():
                self.ui.tableWidget_butunGorusmeler.insertRow(row_index)
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(row_data['Yakın zamanda başlayacak ITPH Cybersecurity veya Powerplatform Eğitimlerine Katılmak istemisiniz'])))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(row_data['Zaman damgası'])))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(row_data['Mail adresiniz'])))
                admin_email = get_admin_email()
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(admin_email)))
        except Exception as e:
            print(f"Hata oluştu: {e}")
    
    def send_email(self):
        try:
            sender_email = os.getenv('EMAIL_SENDER')
            receiver_email = os.getenv('EMAIL_RECEIVER')
            email_password = os.getenv('EMAIL_PASSWORD')
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = "VIT Project Notification"

            # Add body
            body = "VIT Project Notification"
            msg.attach(MIMEText(body, 'plain'))

            # Create SMTP session
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, email_password)
                text = msg.as_string()
                server.sendmail(sender_email, receiver_email, text)
            
            QMessageBox.information(self, "Success", "Email sent successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()  # Giriş penceresini başlat
    login_window.show()
    sys.exit(app.exec())

