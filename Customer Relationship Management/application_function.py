from PyQt6.QtWidgets import *
import gdown
import pandas as pd
import sys
from application import Ui_Applications

def download_and_read_Application():
    try:
        # Google Drive'dan dosya indirme
        url = 'https://drive.google.com/uc?id=19hfIbsIJ1f54aSwPPTNGIOAis26mibMk'  # Dosya ID'si ile doğru bağlantı
        output = 'Basvurular.xlsx'
        gdown.download(url, output, quiet=False)

        # Excel dosyasını okuma
        download_users = pd.read_excel(output)
        # print(download_users.head())
        return download_users  # Veriyi geri döndür
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None
    
downloaded_data3 = download_and_read_Application()


class Application_Window(QMainWindow):
    def __init__(self, user_type = "user"):
        super().__init__()
        self.ui = Ui_Applications()
        self.ui.setupUi(self)
        self.user_type=user_type

        print("Application_Window yüklendi.")
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_Exit.clicked.connect(self.exit)
        print("pushButton_Exit bağlandı.")

        self.ui.pushButton_geriDon.clicked.connect(self.back_to_preference)
        print("pushButton_geriDon bağlandı.")

        self.ui.applications_all_button.clicked.connect(self.load_all_applications)
        print("applications_all_button bağlandı.")

        self.ui.applications_defined_button.clicked.connect(self.load_defined_mentor_meetings)
        print("applications_defined_button bağlandı.")

        self.ui.applications_undefined_button.clicked.connect(self.load_undefined_mentor_meetings)
        print("applications_undefined_button bağlandı.")

        self.ui.applications_search_button.clicked.connect(self.search_application)
        print("applications_search_button bağlandı.")





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




    def load_all_applications(self):
        
        file_path = "Basvurular.xlsx"  # İndirilen dosyanın adı

        try:
            # Dosyayı indir
            download_and_read_Application()

            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # Tabloyu temizle
            self.ui.applications_table.setRowCount(0)
            


            # Verileri tabloya ekle
            for row_index, row_data in df.iterrows():
                self.ui.applications_table.insertRow(row_index)
                self.ui.applications_table.setItem(row_index, 0, QTableWidgetItem(str(row_data['Zaman damgası'])))  
                self.ui.applications_table.setItem(row_index, 1, QTableWidgetItem(str(row_data['Adınız Soyadınız'])))  
                self.ui.applications_table.setItem(row_index, 2, QTableWidgetItem(str(row_data['Mail adresiniz'])))  
                self.ui.applications_table.setItem(row_index, 3, QTableWidgetItem(str(row_data['Telefon Numaranız'])))  
                self.ui.applications_table.setItem(row_index, 4, QTableWidgetItem(str(row_data['Posta Kodunuz'])))  
                self.ui.applications_table.setItem(row_index, 5, QTableWidgetItem(str(row_data['Yaşadığınız Eyalet'])))  
                self.ui.applications_table.setItem(row_index, 6, QTableWidgetItem(str(row_data['Şu anki durumunuz'])))  
            print(f"✅ {len(df)} Application kaydı başarıyla yüklendi!")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")


    def load_defined_mentor_meetings(self):
    
        file_path = "Basvurular.xlsx"  # Excel dosyasının adı

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # 'Mentor görüşmesi' sütununda 'OK' olan verileri filtrele
            filtered_df = df[df["Mentor gorusmesi"].astype(str).str.strip().eq("OK")]

            # Eğer sonuç boşsa tabloyu temizle
            self.ui.applications_table.setRowCount(0)
            self.ui.applications_table.setRowCount(len(filtered_df))

            if filtered_df.empty:
                print("⚠️ 'OK' olan Mentor görüşmesi bulunamadı!")
                return

            # Tabloyu temizleyip filtrelenen verileri ekleyelim
            for row_index in range(len(filtered_df)):
                self.ui.applications_table.setItem(row_index, 0, QTableWidgetItem(str(filtered_df.iloc[row_index]['Zaman damgası'])))  
                self.ui.applications_table.setItem(row_index, 1, QTableWidgetItem(str(filtered_df.iloc[row_index]['Adınız Soyadınız'])))  
                self.ui.applications_table.setItem(row_index, 2, QTableWidgetItem(str(filtered_df.iloc[row_index]['Mail adresiniz'])))  
                self.ui.applications_table.setItem(row_index, 3, QTableWidgetItem(str(filtered_df.iloc[row_index]['Telefon Numaranız'])))  
                self.ui.applications_table.setItem(row_index, 4, QTableWidgetItem(str(filtered_df.iloc[row_index]['Posta Kodunuz'])))  
                self.ui.applications_table.setItem(row_index, 5, QTableWidgetItem(str(filtered_df.iloc[row_index]['Yaşadığınız Eyalet'])))  
                self.ui.applications_table.setItem(row_index, 6, QTableWidgetItem(str(filtered_df.iloc[row_index]['Şu anki durumunuz'])))  

            print(f"✅ 'OK' olan {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")
    def load_undefined_mentor_meetings(self):
    
        file_path = "Basvurular.xlsx"  # Excel dosyasının adı

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # 'Mentor görüşmesi' sütununda 'ATANMADI' olan verileri filtrele
            filtered_df = df[df["Mentor gorusmesi"].astype(str).str.strip().eq("ATANMADI")]

            # Eğer sonuç boşsa tabloyu temizle
            self.ui.applications_table.setRowCount(0)
            self.ui.applications_table.setRowCount(len(filtered_df))


            if filtered_df.empty:
                print("⚠️ 'ATANMADI' olan Mentor görüşmesi bulunamadı!")
                return
            

            # Tabloyu temizleyip filtrelenen verileri ekleyelim
            for row_index in range(len(filtered_df)):
                self.ui.applications_table.setItem(row_index, 0, QTableWidgetItem(str(filtered_df.iloc[row_index]['Zaman damgası'])))  
                self.ui.applications_table.setItem(row_index, 1, QTableWidgetItem(str(filtered_df.iloc[row_index]['Adınız Soyadınız'])))  
                self.ui.applications_table.setItem(row_index, 2, QTableWidgetItem(str(filtered_df.iloc[row_index]['Mail adresiniz'])))  
                self.ui.applications_table.setItem(row_index, 3, QTableWidgetItem(str(filtered_df.iloc[row_index]['Telefon Numaranız'])))  
                self.ui.applications_table.setItem(row_index, 4, QTableWidgetItem(str(filtered_df.iloc[row_index]['Posta Kodunuz'])))  
                self.ui.applications_table.setItem(row_index, 5, QTableWidgetItem(str(filtered_df.iloc[row_index]['Yaşadığınız Eyalet'])))  
                self.ui.applications_table.setItem(row_index, 6, QTableWidgetItem(str(filtered_df.iloc[row_index]['Şu anki durumunuz'])))  

            print(f"✅ 'ATANMADI' olan {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")


    def search_application(self):
   
        file_path = "Basvurular.xlsx"  # Excel dosya adı
        search_text = self.ui.applications_search_line.text().strip().lower()  # Kullanıcı girişini al

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # Sadece eşleşen verileri al
            filtered_df = df[df['Adınız Soyadınız'].astype(str).str.lower().str.contains(search_text, regex=False, na=False)]

            # Önce tabloyu temizle
            self.ui.applications_table.clearContents()
            self.ui.applications_table.setRowCount(len(filtered_df))

            # ✅ Doğru sütun isimleriyle sıralı şekilde ekle
            for row_index in range(len(filtered_df)):
                self.ui.applications_table.setItem(row_index, 0, QTableWidgetItem(str(filtered_df.iloc[row_index]['Zaman damgası'])))  
                self.ui.applications_table.setItem(row_index, 1, QTableWidgetItem(str(filtered_df.iloc[row_index]['Adınız Soyadınız'])))  
                self.ui.applications_table.setItem(row_index, 2, QTableWidgetItem(str(filtered_df.iloc[row_index]['Mail adresiniz'])))  
                self.ui.applications_table.setItem(row_index, 3, QTableWidgetItem(str(filtered_df.iloc[row_index]['Telefon Numaranız'])))  
                self.ui.applications_table.setItem(row_index, 4, QTableWidgetItem(str(filtered_df.iloc[row_index]['Yaşadığınız Eyalet'])))  
                self.ui.applications_table.setItem(row_index, 5, QTableWidgetItem(str(filtered_df.iloc[row_index]['Şu anki durumunuz'])))  

            print(f"✅ '{search_text}' ile ilgili {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")
    