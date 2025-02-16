from PyQt6.QtWidgets import *
from mentor_interview import Ui_MentorInterview
import gdown
import pandas as pd
import sys
from preference_menu_user import Ui_Preference_menu_user
from preference_menu_admin import Ui_preference_menu_admin

def download_and_read_Mentor():
    try:
        # Google Drive'dan dosya indirme
        url = 'https://drive.google.com/uc?id=1khXTdzyx6RGCfDrzEVbpbxqmcDwId1yl'  # Dosya ID'si ile doğru bağlantı
        output = 'Mentor.xlsx'
        gdown.download(url, output, quiet=False)

        # Excel dosyasını okuma
        download_users = pd.read_excel(output)
        # print(download_users.head())
        return download_users  # Veriyi geri döndür
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None
    
downloaded_data2 = download_and_read_Mentor()
if downloaded_data2 is not None:
    print(downloaded_data2['Yorum'])
    print(downloaded_data2['Mentor'])
    
class MentorInterviewsWindow(QMainWindow):
    def __init__(self,user_type="user"):
        super().__init__()
        self.ui = Ui_MentorInterview()
        self.ui.setupUi(self)
        self.user_type=user_type
        self.load_comment_options()

    

        print("MentorInterviewsWindow yüklendi.")
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_Exit.clicked.connect(self.exit)
        print("pushButton_Exit bağlandı.")

        self.ui.pushButton_geriDon.clicked.connect(self.back_to_preference)
        print("pushButton_geriDon bağlandı.")

        self.ui.pushButton_tumGorusmeler.clicked.connect(self.load_all_interviews)
        print("pushButton_tumGorusmeler bağlandı.")

        self.ui.interviews_search_button.clicked.connect(self.search_interviews)
        print("interviews_search_button bağlandı.")









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
        
        file_path = "Mentor.xlsx"  # İndirilen dosyanın adı

        try:
            # Dosyayı indir
            download_and_read_Mentor()

            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # Tabloyu temizle
            self.ui.tableWidget_butunGorusmeler.setRowCount(0)

            # Verileri tabloya ekle
            for row_index, row_data in df.iterrows():
                self.ui.tableWidget_butunGorusmeler.insertRow(row_index)
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(row_data['Gorusme Tarihi'])))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(row_data['Ad soyad'])))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(row_data['Mentor'])))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(row_data['IT Bilgisi'])))  # IT Deneyimi
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 4, QTableWidgetItem(str(row_data['Yogunluk'])))
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 5, QTableWidgetItem(str(row_data['Yorum'])))

        except Exception as e:
            print(f"Hata oluştu: {e}")


    def search_interviews(self):
        file_path = "Mentor.xlsx"  # Excel dosya adı
        search_text = self.ui.applications_search_line.text().strip().lower()  # Kullanıcı girişini al

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")

            # Sadece eşleşen verileri al
            filtered_df = df[df['Ad soyad'].astype(str).str.lower().str.contains(search_text, regex=False, na=False)]

            # Önce tabloyu temizle
            self.ui.tableWidget_butunGorusmeler.clearContents()
            self.ui.tableWidget_butunGorusmeler.setRowCount(len(filtered_df))

            # Filtrelenen verileri tabloya ekle
            for row_index, row_data in enumerate(filtered_df.itertuples(index=False), start=0):
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(row_data[0])))  # Gorusme Tarihi
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(row_data[1])))  # Ad soyad
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(row_data[2])))  # Mentor
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(row_data[3])))  # IT Bilgisi
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 4, QTableWidgetItem(str(row_data[4])))  # Yogunluk
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 5, QTableWidgetItem(str(row_data[5])))  # Yorum

        except Exception as e:
            print(f"Hata oluştu: {e}")
    
    def load_comment_options(self):
    
        file_path = "Mentor.xlsx"  

        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path, engine="openpyxl")
            
            # 'Yorum' sütunundaki eşsiz değerleri al
            unique_comments = df['Yorum'].dropna().unique()

            # Mevcut öğeleri temizle
            self.ui.comboBox_.clear()
            self.ui.comboBox_.addItem("Select an option...")  # Varsayılan değer

            # Her bir yorum seçeneğini ekleyelim
            for comment in unique_comments:
                self.ui.comboBox_.addItem(str(comment))

            # ComboBox seçim değiştiğinde tabloyu güncelle
            self.ui.comboBox_.currentTextChanged.connect(self.filter_by_comment)

        except Exception as e:
            print(f"Hata oluştu: {e}")

    def filter_by_comment(self):
        file_path = "Mentor.xlsx"
        selected_comment = self.ui.comboBox_.currentText().strip()  # Seçilen filtreyi al

        try:
            df = pd.read_excel(file_path, engine="openpyxl")

            # Yorum sütununun tamamını string'e çevir ve boşlukları temizle
            df["Yorum"] = df["Yorum"].astype(str).str.strip()

            # Tabloyu önce temizle
            self.ui.tableWidget_butunGorusmeler.setRowCount(0)

            # Eğer "Select an option..." seçiliyse hiçbir işlem yapma
            if selected_comment == "Select an option...":
                return
            
            # Seçilen yoruma göre filtreleme yap
            filtered_df = df[df["Yorum"].str.lower() == selected_comment.lower()]

            # Eğer sonuç boşsa tabloyu temizle ve durdur
            if filtered_df.empty:
                print(f"⚠️ '{selected_comment}' filtresi için hiçbir kayıt bulunamadı!")
                return

            # Tabloyu temizleyip filtrelenen verileri ekleyelim
            for row_index in range(len(filtered_df)):
                self.ui.tableWidget_butunGorusmeler.insertRow(row_index)
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 0, QTableWidgetItem(str(filtered_df.iloc[row_index]['Gorusme Tarihi'])))  
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 1, QTableWidgetItem(str(filtered_df.iloc[row_index]['Ad soyad'])))  
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 2, QTableWidgetItem(str(filtered_df.iloc[row_index]['Mentor'])))  
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 3, QTableWidgetItem(str(filtered_df.iloc[row_index]['IT Bilgisi'])))  
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 4, QTableWidgetItem(str(filtered_df.iloc[row_index]['Yogunluk'])))  
                self.ui.tableWidget_butunGorusmeler.setItem(row_index, 5, QTableWidgetItem(str(filtered_df.iloc[row_index]['Yorum'])))  

            print(f"✅ '{selected_comment}' filtresine göre {len(filtered_df)} kayıt bulundu ve tabloya yansıtıldı.")

        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")





