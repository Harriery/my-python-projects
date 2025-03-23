from PyQt6.QtWidgets import * 
from login_function import LoginWindow

import sys
from PyQt6.QtWidgets import QApplication
from login_function import LoginWindow  # LoginWindow'u içe aktar

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())