from PySide6.QtWidgets import QMainWindow

from ui_keysWindow import Ui_KeysWindow

class KeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_KeysWindow()
        self.ui.setupUi(self)
