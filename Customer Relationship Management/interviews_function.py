from PyQt6.QtWidgets import *
import gdown
import pandas as pd
import sys
from interviews import Ui_Interviews
from datetime import datetime
from PyQt6.QtWidgets import QTableWidgetItem



def download_and_read_Interviews():
    try:
        # Google Drive'dan dosya indirme
        url = 'https://drive.google.com/uc?id=1w0p6qyMyORpJggeJr5Gwrovl_jffnoN8'  # Dosya ID'si ile doğru bağlantı
        output = 'Mulakatlar.xlsx'
        gdown.download(url, output, quiet=False)

        # Excel dosyasını okuma
        download_users = pd.read_excel(output)
        # print(download_users.head())
        return download_users  # Veriyi geri döndür
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None
    
downloaded_data3 = download_and_read_Interviews()
if downloaded_data3 is not None:
    print(downloaded_data3['Adınız Soyadınız'])

class Interview_Window(QMainWindow):
    def __init__(self, user_type = "user"):
        super().__init__()
        self.ui = Ui_Interviews()
        self.ui.setupUi(self)
        self.user_type=user_type

        self.ui.pushButton_Exit.clicked.connect(self.exit)
        print("pushButton_Exit bağlandı.")

        self.ui.pushButton_geriDon.clicked.connect(self.back_to_preference)
        print("pushButton_geriDon bağlandı.")

        self.ui.pushButton_incoming_projects.clicked.connect(self.load_incoming_projects)
        print("pushButton_incoming_projects bağlandı.")

        self.ui.pushButton_project_submitted.clicked.connect(self.load_project_submitted)
        print("pushButton_project_submitted bağlandı.")

        self.ui.pushButton_search.clicked.connect(self.search_interviews)
        print("pushButton_search bağlandı.")

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

    def exit(self):
       """Pencereyi kapatır ve uygulamadan çıkar."""
       try:
           self.close()  # Mevcut pencereyi kapat
           print("Pencere başarıyla kapatıldı.")
       except Exception as e:
           print(f"Pencere kapatılırken hata oluştu: {e}")



    def load_incoming_projects(self):
        file_path = "Mulakatlar.xlsx"
        try:
            df = pd.read_excel(file_path, engine="openpyxl")

            # Boş satırları temizle, sadece dolu olanları al
            filtered_df = df.dropna(subset=["Projenin gelis tarihi"])  

            # Tabloyu tamamen temizle
            self.ui.interviews_table.clearContents()  
            self.ui.interviews_table.setRowCount(0)  

            for row_index, row in filtered_df.iterrows():
                self.ui.interviews_table.insertRow(row_index)  # Yeni satır ekle
    
                # Tarihleri düzgün formatla (YYYY-MM-DD)
                try:
                    received_date = datetime.strptime(str(row["Projenin gelis tarihi"]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                except ValueError:
                    received_date = str(row["Projenin gelis tarihi"])  # Eğer format farklıysa olduğu gibi al
                
                try:
                    submission_date = datetime.strptime(str(row["Proje gonderilis tarihi"]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                except ValueError:
                    submission_date = str(row["Proje gonderilis tarihi"])
    
                # Verileri tabloya ekle
                self.ui.interviews_table.setItem(row_index, 0, QTableWidgetItem(str(row["Adınız Soyadınız"])))  
                self.ui.interviews_table.setItem(row_index, 1, QTableWidgetItem(received_date))  
                self.ui.interviews_table.setItem(row_index, 2, QTableWidgetItem(submission_date)) 

            print(f"✅ {len(filtered_df)} kayıt tabloya düzgünce eklendi.")
        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}") 



    
    def load_project_submitted(self):
        file_path = "Mulakatlar.xlsx"  # Excel dosyasının adı
        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # 'Proje gonderilis tarihi' sütunu boş olmayan satırları filtrele
            filtered_df = df.dropna(subset=["Proje gonderilis tarihi"])

            # Tabloyu tamamen temizle
            self.ui.interviews_table.clearContents()  
            self.ui.interviews_table.setRowCount(0)  

            # Verileri tabloya ekleyelim
            for row_index, row in filtered_df.iterrows():
                self.ui.interviews_table.insertRow(row_index)  # Yeni satır ekle

                # Tarihleri düzgün formatla (YYYY-MM-DD)
                try:
                    received_date = datetime.strptime(str(row["Projenin gelis tarihi"]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                except ValueError:
                    received_date = str(row["Projenin gelis tarihi"])  # Eğer format farklıysa olduğu gibi al

                try:
                    submission_date = datetime.strptime(str(row["Proje gonderilis tarihi"]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                except ValueError:
                    submission_date = str(row["Proje gonderilis tarihi"])

                # Verileri tabloya ekle
                self.ui.interviews_table.setItem(row_index, 0, QTableWidgetItem(str(row["Adınız Soyadınız"])))  
                self.ui.interviews_table.setItem(row_index, 1, QTableWidgetItem(received_date))  
                self.ui.interviews_table.setItem(row_index, 2, QTableWidgetItem(submission_date))  

            print(f"✅ 'Proje gonderilis tarihi' sütununda veri bulunan {len(filtered_df)} kayıt tabloya eklendi.")
        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}") 

    def search_interviews(self):
   
        file_path = "Mulakatlar.xlsx"  # Excel dosya adı
        search_text = self.ui.interviews_search_line.text().strip().lower()  # Kullanıcı girişini al

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # Sadece eşleşen verileri al
            filtered_df = df[df['Adınız Soyadınız'].astype(str).str.lower().str.contains(search_text, regex=False, na=False)]

            # Önce tabloyu temizle
            self.ui.interviews_table.clearContents()
            self.ui.interviews_table.setRowCount(len(filtered_df))

            # ✅ Doğru sütun isimleriyle sıralı şekilde ekle
            for row_index in range(len(filtered_df)):
                self.ui.interviews_table.setItem(row_index, 0, QTableWidgetItem(str(filtered_df.iloc[row_index]['Adınız Soyadınız'])))  
                self.ui.interviews_table.setItem(row_index, 2, QTableWidgetItem(str(filtered_df.iloc[row_index]['Proje gonderilis tarihi'])))  
                self.ui.interviews_table.setItem(row_index, 3, QTableWidgetItem(str(filtered_df.iloc[row_index]['Projenin gelis tarihi'])))  

            print(f"✅ '{search_text}' ile ilgili {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}") 