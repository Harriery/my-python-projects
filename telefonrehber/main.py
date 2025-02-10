from PyQt6.QtWidgets import *
from _form import FormWindow

uygulama= QApplication([])
pencere = FormWindow()
pencere.show()
uygulama.exec()