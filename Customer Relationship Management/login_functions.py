from PyQt6.QtWidgets import *
from login import Ui_LoginWindow
import gdown
import pandas as pd
import sys
from preference_menu_admin_function import AdminPreferenceMenuWindow #Admin menusu UI
from preference_menu_user_function import UserPreferenceMenuWindow#Kullanici menusu UI


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


ui = Ui_LoginWindow()

def show_message(title, message, icon):
    """Mesaj kutusu gösterme fonksiyonu"""
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(icon)
    msg.exec()

logged_in_user_data = None

def validate_user(window):
    global logged_in_user_data
    username = window.ui.lineEdit_userName.text()
    password = window.ui.lineEdit_password.text()
    
    if username in downloaded_data['kullanici'].values:
        index = downloaded_data[downloaded_data['kullanici'] == username].index[0]
        
        if password == downloaded_data.loc[index, 'parola']:
            user_role = downloaded_data.loc[index, 'yetki']
            logged_in_user_data = downloaded_data.loc[index]
            print("Başarıyla giriş yapılmıştır")
            # Giriş başarılı, rolü belirle ve uygun menüyü aç.
            if user_role == "admin":
                open_admin_menu(window)
                show_message("Login Successful", "You are logged in as Administrator.", QMessageBox.Icon.Information)
            elif user_role == "user":
                open_user_menu(window)
                show_message("Login Successful", "You are logged in as a user.", QMessageBox.Icon.Information)
            else:
                show_message("Unknown Authorization", "Authorization error, invalid user role", QMessageBox.Icon.Critical)
                print("Hatalı şifre")
            print(logged_in_user_data)
            return logged_in_user_data
        else:
            show_message("Incorrect Password", "The entered password is incorrect.", QMessageBox.Icon.Critical)
    else:
        show_message("User Not Found", "The entered username could not be found.", QMessageBox.Icon.Critical)
        print("Kullanıcı bulunamadı")
    return None

admin_window=None#Global degiskene eklemiyor\kaybolmuyor
user_window=None

def open_admin_menu(current_window):
    global admin_window#global degiskenine ekleniyor ve pyton da kaybolmuyor
    admin_window = AdminPreferenceMenuWindow()
    admin_window.show()
    current_window.close()


def open_user_menu(current_window):
    global user_window
    user_window = UserPreferenceMenuWindow()
    user_window.show()
    current_window.close()