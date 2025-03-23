from PyQt6.QtWidgets import * 
from woordstudie import Ui_Woordstudie
import database

class WoordstudieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Woordstudie()
        self.ui.setupUi(self)

    def load_words(self):
        words = database.get_words()
        if words:
            for word in words:
                self.ui.comboBox_woordselecteer.addItem(word[1])

    def load_word_types(self):
        word_types = database.get_word_types()
        if word_types:
            for types in word_types:
                self.ui.comboBox_woordtype.addItem(types[1])
    
    def load_word_variations(self):
        word_variations = database.get_word_variations()
        if word_variations:
            for variation in word_variations:
                self.ui.comboBox_verwanteVormen.addItem(variation[1])

        

        

