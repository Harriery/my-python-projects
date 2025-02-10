import sys
import os
import sqlite3
from PyQt6.QtWidgets import *           # Qt araclarini kullanabilmek icin kutuphane import edilir.
from form import Ui_MainWindow          # form.py deki class olan Ui_MainWindow import edildi.

class FormWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.anaForm = Ui_MainWindow()      # bu kisimlar ezber kismi. form dosyasini bu class a baglamak icin kullaniliyor.
        self.anaForm.setupUi(self)   

        self.adSoyad = self.anaForm.txtAdSoyad
        self.telefon = self.anaForm.txtTelefon
        self.eposta = self.anaForm.txtEposta
        self.liste = self.anaForm.tblListe

        self.anaForm.btnKaydet.clicked.connect(self.kaydet)
        self.anaForm.btnListele.clicked.connect(self.listele)
        self.anaForm.btnCikis.clicked.connect(self.cikis)

    def baglan(self):                                              #db dosyasi ile baglati yapilir.     
        sqlFile = os.path.join(os.path.dirname(__file__), "rehber.db")
        # with sqlite3.connect("./rehber.db") as baglanti          --> bu sekilde de calisir os kullanmadan
        with sqlite3.connect(sqlFile) as baglanti:
            return baglanti

    def kaydet(self):
        try:
            from random import randint
            kayitNo = str(randint(111, 999))
            baglanti = self.baglan()
            sorgu = baglanti.cursor()
            sorgu.execute(f"insert into icerik values ('{kayitNo}','{self.adSoyad.text()}','{self.telefon.text()}','{self.eposta.text()}')")
            #tek satirli metin kutusu icin: text() cok satirlimetin kutusu icin: toPlainText()  int spinler icin: value()
            baglanti.commit()   #sorgu.execute calistrmak icin yazlidi.
            self.temizle()      #kayit islemi olduktan sonra bilgilerin kutucuklardan temzilenmesi icin
            self.liste.setFocus()   # en son hangi kutucukta islme yapildiysa oradaki focusu kaldirir. 

            QMessageBox.information(self, "Bildirim", "Kayit Basarili.")

        except Exception as hata:
            QMessageBox.critical(self, "Hata", "Hata Olustu:\n" + hata)


    def listele(self):
        try:
            self.liste.clear()
            sutunlar = ["No", "Ad Soyad", "Telefon","E-posta"]
            self.liste.setColumnCount(len(sutunlar))
            self.liste.setHorizontalHeaderLabels(sutunlar)
            baglanti = self.baglan()
            sorgu = baglanti.cursor()
            sorgu.execute("select * from icerik")
            kayitlar = sorgu.fetchall()
            if kayitlar:
                self.liste.setRowCount(len(kayitlar))
                kayitSay =0
                for kayit in kayitlar:
                    for i in range(len(sutunlar)):
                        self.liste.setItem(kayitSay, i ,QTableWidgetItem(str(kayit[i])))
                    kayitSay += 1
            else:
                QMessageBox.warning(self, "Uyari", "Kayit Bulunamadi")
        except Exception as hata:
            QMessageBox.critical(self, "Hata", "Hata Olustu:\n" + hata)

    def temizle(self):
        self.adSoyad.clear()
        self.telefon.clear()
        self.eposta.clear()

    def cikis(self):
        sys.exit()