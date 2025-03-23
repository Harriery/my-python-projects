from PyQt6.QtWidgets import * 
from voorkeurenpagina import Ui_voorkeurenpagina
from woordstudie import Ui_Woordstudie

class VoorkeurWindow(QMainWindow):
    def __init__(self, username):  # username parametresini ekle
        super().__init__()
        self.ui = Ui_voorkeurenpagina()
        self.ui.setupUi(self)

         # Kullanıcı adını etikete yaz
        self.username = username
        self.ui.label_welkom_userName.setText(f"{self.username}")
        
        # Buton bağlantılarını yap
        self.ui.pushButton_woordstudie.clicked.connect(self.open_woordstudiepagina)
        print("Buton bağlantısı yapıldı!")  # Debug mesajı
        self.ui.pushButton_grammatica.clicked.connect(self.open_grammatica_pagina)
        self.ui.pushButton_maakQuiz.clicked.connect(self.open_maakQuiz_pagina)
        self.ui.pushButton_voortgangBekijken.clicked.connect(self.open_voortgangBekijken_pagina)

        self.open_window = []

    def open_woordstudiepagina(self):
        print("Woordstudie butonuna tıklandı")
        self.woordstudie_window = QMainWindow()  # Yeni pencere oluştur
        ui_woordstudie = Ui_Woordstudie()  # Ui_Woordstudie nesnesi oluştur
        ui_woordstudie.setupUi(self.woordstudie_window)  # Pencereye UI'yi uygula
        self.woordstudie_window.show()  # Pencereyi göster
        print("Woordstudie penceresi açıldı!")
        self.hide() 

        # Pencereyi açık tutmak için sakla
        #self.open_window.append(woordstudie_window)
    def open_grammatica_pagina(self):
        print("Woordstudie butonuna tiklanildi")
    
    def open_maakQuiz_pagina(self):
        print("Woordstudie butonuna tiklanildi")
    
    def open_voortgangBekijken_pagina(self):
        print("Woordstudie butonuna tiklanildi")