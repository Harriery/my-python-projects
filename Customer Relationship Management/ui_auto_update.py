from PyQt6 import uic
import os

def compile_ui_files():
    ui_files = ['login.ui', 'preference_menu_admin.ui', 'preference_menu_user.ui', 'application.ui', 'admin_menu.ui', 'interviews.ui', 'mentor_interview.ui']
    for ui_file in ui_files:
        py_file = os.path.splitext(ui_file)[0] + '.py'
        with open(py_file, 'w') as file:
            uic.compileUi(ui_file, file)  # Dosya nesnesini doğru şekilde geçiyoruz
        print(f'Converting {ui_file} to {py_file}...')

if __name__ == '__main__':
    compile_ui_files()
