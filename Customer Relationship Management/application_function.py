from PyQt6.QtWidgets import *
from mentor_interview import Ui_MentorInterview
import gdown
import pandas as pd
import sys
from preference_menu_user import Ui_Preference_menu_user
from preference_menu_admin import Ui_preference_menu_admin

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
if downloaded_data3 is not None:
    print(downloaded_data3['Telefon Numaranız'])
    print(downloaded_data3['Posta Kodunuz'])

class Application_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MentorInterview()
        self.ui.setupUi(self)

        print("Application_Window yüklendi.")
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_Exit.clicked.connect(self.exit)
        print("pushButton_Exit bağlandı.")

        self.ui.pushButton_geriDon.clicked.connect(self.geriDon)
        print("pushButton_geriDon bağlandı.")

        self.ui.applications_all_button.clicked.connect(self.all_button)
        print("applications_all_button bağlandı.")

        self.ui.applications_defined_button.clicked.connect(self.load_defined_mentor_meetings)
        print("applications_defined_button bağlandı.")

        self.ui.applications_undefined_button.clicked.connect(self.load_undefined_mentor_meetings)
        print("applications_undefined_button bağlandı.")

        self.ui.applications_search_button.clicked.connect(self.search_application)
        print("applications_search_button bağlandı.")





    def geriDon(self):
        """Ana menüye geri döner."""
        self.close()  # Mevcut pencereyi kapat
        if self.parent_window:
            self.parent_window.show() 

    










        

    def exit(self):
        """Pencereyi kapatır ve uygulamadan çıkar."""
        try:
            self.close()  # Mevcut pencereyi kapat
            print("Pencere başarıyla kapatıldı.")
        except Exception as e:
            print(f"Pencere kapatılırken hata oluştu: {e}")




    def all_button(self):
        """
        Google Sheets'ten Excel dosyasını indirip QTableWidget'e yükler.
        """
        file_path = "Basvurular.xlsx"  

        try:
            # ✅ Excel dosyasını indir ve oku
            df = download_and_read_Application()

            if df is None:
                print("⚠️ Dosya yüklenemedi!")
                return

            # ✅ İstediğimiz sütunları al
            selected_columns = [
                'Zaman damgası', 'Adınız Soyadınız', 'Mail adresiniz',
                'Telefon Numaranız', 'Posta Kodunuz', 'Yaşadığınız Eyalet', 'Şu anki durumunuz'
            ]
            
            df = df[selected_columns]  # Sadece gerekli sütunları al
            
            # 📌 QTableWidget'i temizle
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # ✅ Verileri tabloya ekle
            for row_index, row_data in df.iterrows():
                self.ui.tableWidget.insertRow(row_index)  # Yeni satır ekle
                self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(row_data['Zaman damgası'])))
                self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(row_data['Adınız Soyadınız'])))
                self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(row_data['Mail adresiniz'])))
                self.ui.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(row_data['Telefon Numaranız'])))
                self.ui.tableWidget.setItem(row_index, 4, QTableWidgetItem(str(row_data['Posta Kodunuz'])))
                self.ui.tableWidget.setItem(row_index, 5, QTableWidgetItem(str(row_data['Yaşadığınız Eyalet'])))
                self.ui.tableWidget.setItem(row_index, 6, QTableWidgetItem(str(row_data['Şu anki durumunuz'])))

            print(f"✅ {len(df)} Application kaydı başarıyla yüklendi!")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")


    def load_defined_mentor_meetings(self):
    
        file_path = "Basvurular.xlsx"  # Excel dosyasının adı

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # 'Mentor görüşmesi' sütununda 'OK' olan verileri filtrele
            filtered_df = df[df["Mentor görüşmesi"].astype(str).str.strip().eq("OK")]

            # Eğer sonuç boşsa tabloyu temizle
            self.ui.tableWidget_butunGorusmeler.setRowCount(0)

            if filtered_df.empty:
                print("⚠️ 'OK' olan Mentor görüşmesi bulunamadı!")
                return

            # Tabloyu temizleyip filtrelenen verileri ekleyelim
            for row_index, row_data in filtered_df.iterrows():
                self.ui.tableWidget_butunGorusmeler.insertRow(row_index)
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(row_data.get("Zaman damgası", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(row_data.get("Adınız Soyadınız", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(row_data.get("Mail adresiniz", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(row_data.get("Telefon Numaranız", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 4, QTableWidgetItem(str(row_data.get("Posta Kodunuz", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 5, QTableWidgetItem(str(row_data.get("Yaşadığınız Eyalet", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 6, QTableWidgetItem(str(row_data.get("Şu anki durumunuz", ""))))

            print(f"✅ 'OK' olan {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")
    def load_undefined_mentor_meetings(self):
    
        file_path = "Basvurular.xlsx"  # Excel dosyasının adı

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # 'Mentor görüşmesi' sütununda 'ATANMADI' olan verileri filtrele
            filtered_df = df[df["Mentor görüşmesi"].astype(str).str.strip().eq("ATANMADI")]

            # Eğer sonuç boşsa tabloyu temizle
            self.ui.tableWidget_butunGorusmeler.setRowCount(0)

            if filtered_df.empty:
                print("⚠️ 'ATANMADI' olan Mentor görüşmesi bulunamadı!")
                return

            # Tabloyu temizleyip filtrelenen verileri ekleyelim
            for row_index, row_data in filtered_df.iterrows():
                self.ui.tableWidget_butunGorusmeler.insertRow(row_index)
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(row_data.get("Zaman damgası", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(row_data.get("Adınız Soyadınız", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(row_data.get("Mail adresiniz", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(row_data.get("Telefon Numaranız", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 4, QTableWidgetItem(str(row_data.get("Posta Kodunuz", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 5, QTableWidgetItem(str(row_data.get("Yaşadığınız Eyalet", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 6, QTableWidgetItem(str(row_data.get("Şu anki durumunuz", ""))))

            print(f"✅ 'ATANMADI' olan {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")


    def search_application(self):
   
        file_path = "Basvurular.xlsx"  # Excel dosyasının adı
        search_text = self.ui.applications_search_line.text().strip().lower()  # Kullanıcı girişini al

        if not search_text:
            print("⚠️ Lütfen aramak için bir isim girin.")
            return

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # 'Adınız Soyadınız' sütununda, search_text içeren kayıtları filtrele
            filtered_df = df[df["Adınız Soyadınız"].astype(str).str.lower().str.contains(search_text, regex=False, na=False)]

            # Eğer sonuç boşsa tabloyu temizle
            self.ui.tableWidget_butunGorusmeler.setRowCount(0)

            if filtered_df.empty:
                print(f"⚠️ '{search_text}' ismine uygun kayıt bulunamadı!")
                return

            # Tabloyu temizleyip filtrelenen verileri ekleyelim
            for row_index, row_data in filtered_df.iterrows():
                self.ui.tableWidget_butunGorusmeler.insertRow(row_index)
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(row_data.get("Zaman damgası", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(row_data.get("Adınız Soyadınız", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(row_data.get("Mail adresiniz", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(row_data.get("Telefon Numaranız", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 4, QTableWidgetItem(str(row_data.get("Posta Kodunuz", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 5, QTableWidgetItem(str(row_data.get("Yaşadığınız Eyalet", ""))))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 6, QTableWidgetItem(str(row_data.get("Şu anki durumunuz", ""))))

            print(f"✅ '{search_text}' ile eşleşen {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")

    