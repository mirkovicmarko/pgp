from PySide6.QtWidgets import QMainWindow

from ui_generateDeleteKeysWindow import Ui_GenerateDeleteKeysWindow

class GenerateDeleteKeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GenerateDeleteKeysWindow()
        self.ui.setupUi(self)
