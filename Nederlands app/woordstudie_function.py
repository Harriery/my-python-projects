from PyQt6.QtWidgets import * 
from woordstudie import Ui_Woordstudie
import database

class WoordstudieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Woordstudie()
        self.ui.setupUi(self)

        # İlk yükleme
        self.load_word_types()  # Önce kelime türlerini yükle

        # ComboBox seçimlerini takip et
        self.ui.comboBox_woordtype.currentIndexChanged.connect(self.update_words_based_on_type)
        self.ui.comboBox_woordselecteer.currentIndexChanged.connect(self.update_variations_based_on_word)

    def load_word_types(self):
        """Kelime türlerini yükler"""
        word_types = database.get_word_types()
        print("Veritabanından gelen kelime türleri:", word_types)  # Eklendi
        if word_types:
            self.ui.comboBox_woordtype.clear()
            for types in word_types:
                print(f"ComboBox'a ekleniyor: ID={types[0]}, İsim={types[1]}")  # Eklendi
                self.ui.comboBox_woordtype.addItem(types[1], types[0])
            print("ComboBox öğe sayısı:", self.ui.comboBox_woordtype.count())  # Eklendi


    def update_words_based_on_type(self):
        selected_type_id = self.ui.comboBox_woordtype.currentData()  # Seçili kelime türü ID'sini al
        print("Seçili tür ID:", selected_type_id)  # ID'nin int olup olmadığını kontrol et
    
        words = database.get_words_by_type(selected_type_id)  
        print("Gelen Kelimeler:", words)  # Burada liste mi, int mi, kontrol et
    
        if isinstance(words, list):  # Eğer bir liste döndüyse işleme devam et
            self.ui.comboBox_woordselecteer.clear()
            for word in words:
                if isinstance(word, tuple) and len(word) > 1:
                    self.ui.comboBox_woordselecteer.addItem(word[1])  # word[1] string olmalı
        else:
            print("Beklenmeyen veri tipi:", type(words))  # Hataları yakalamak için


    def update_variations_based_on_word(self):
        """Seçilen kelimeye göre varyasyonları günceller"""
        selected_word_id = self.ui.comboBox_woordselecteer.currentData()  # Seçili kelimenin ID'sini al
        if selected_word_id is None:
            return
        
        word_variations = database.get_word_variations_by_word(selected_word_id)  # Seçili kelimeye göre varyasyonları al
        self.ui.comboBox_verwanteVormen.clear()
        for variation in word_variations:
            self.ui.comboBox_verwanteVormen.addItem(variation[1])  # Sadece isim ekle
