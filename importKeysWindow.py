from PySide6.QtWidgets import QMainWindow

from ui_importKeysWindow import Ui_ImportKeysWindow

class ImportKeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImportKeysWindow()
        self.ui.setupUi(self)
