from PyQt6.QtWidgets import *
from login import Ui_LoginWindow
import gdown
import pandas as pd



def download_and_read_users():
    try:
        # Google Drive'dan dosya indirme
        url = 'https://drive.google.com/uc?id=1SatXOBosige730jIOoR8UAeXQG4UA8Ph'  # Dosya ID'si ile doğru bağlantı
        output = 'users.xlsx'
        gdown.download(url, output, quiet=False)

        # Excel dosyasını okuma
        download_users = pd.read_excel(output)
        # print(download_users.head())
        return download_users  # Veriyi geri döndür
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

downloaded_data = download_and_read_users()
print(downloaded_data['kullanici'])
print(downloaded_data['yetki'])

ui = Ui_LoginWindow()

def validate_user(window):
    username = window.ui.lineEdit_userName.text()
    password = window.ui.lineEdit_password.text()
    if username in downloaded_data['kullanici'].values:
        index = downloaded_data[downloaded_data['kullanici'] == username].index[0]
        if password == downloaded_data.loc[index, 'parola']:
            print("Barasiyla giris yapilmistir")
        else:
            print("Hatali Sifre")
    else:
        print("Kullanici Bulunamadi")
    user_role = downloaded_data.loc[index, 'yetki']
    if user_role == "admin":
        print("Admin Yetkisi ile giris yapti")
    elif user_role == "user":
        print("Kullanici user yetkisi ile giris yapti.")
    else:
        print("Bilinmeyen yetki..!")
    