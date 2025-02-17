from PyQt6.QtWidgets import *
import gdown
import pandas as pd
import sys
from login_functions import validate_user
from admin_menu import Ui_AdminMenu
from main import *

def download_and_read_admins():
    try:
        # Google Drive'dan dosya indirme
        #urlBasvurular = 'https://drive.google.com/uc?id=19hfIbsIJ1f54aSwPPTNGIOAis26mibMk'  # Dosya ID'si ile doğru bağlantı
        outputBasvurular = 'Basvurular.xlsx'
        #urlUsers = 'https://drive.google.com/uc?id=1SatXOBosige730jIOoR8UAeXQG4UA8Ph'  # Dosya ID'si ile doğru bağlantı
        outputUsers = 'users.xlsx'
       # gdown.download(urlBasvurular, outputBasvurular, quiet=False)
       # gdown.download(urlUsers, outputUsers, quiet=False)

        # Excel dosyasını okuma
        download_users = pd.read_excel(outputUsers)
        download_basvurular = pd.read_excel(outputBasvurular)
        # print(download_users.head())
        return download_users, download_basvurular  # Veriyi geri döndür
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
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
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem("admin_email"))  # Giriş yapan adminin e-posta adresini kullan
        except Exception as e:
            print(f"Hata oluştu: {e}")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()  # Giriş penceresini başlat
    login_window.show()
    sys.exit(app.exec())

