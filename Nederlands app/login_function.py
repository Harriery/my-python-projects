from PyQt6.QtWidgets import * 
from login import Ui_Inloggen
from voorkeurpagina_function import VoorkeurWindow
import database

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Inloggen()
        self.ui.setupUi(self)

        # Giriş butonuna tıklanınca loggen_user fonksiyonunu çalıştır
        self.ui.pushButton_inloggen.clicked.connect(self.loggen_user)

    def loggen_user(self):
        username = self.ui.lineEdit_gebruikersNaam.text()
        passwoord = self.ui.lineEdit_wachtwoord.text()

        if database.check_username(username):
            if database.check_password(username, passwoord):
                print("Giriş başarılı!")
                self.open_voorkeurpagina(username)  # Voorkeurpagina'yı aç ve kullanıcı adını ilet
            else: 
                print("Şifre hatalı")
        else:
             print("Kullanıcı adı hatalı!")

    def open_voorkeurpagina(self, username):  # username parametresini ekle
        print("Voorkeurpagina açılıyor...")  
        self.voorkeur_pagina = VoorkeurWindow(username)  # username parametresini ilet
        self.voorkeur_pagina.show()  
        self.close() 