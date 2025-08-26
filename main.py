import sys
from PyQt5.QtWidgets import QApplication
from app.main_window import ModernPdfReader

def main():
    app = QApplication(sys.argv)
    win = ModernPdfReader()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()