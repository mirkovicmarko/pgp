from PySide6.QtWidgets import QMainWindow

from ui_generateDeleteKeysWindow import Ui_GenerateDeleteKeysWindow

from windowManager import WindowManager
from generateKeyWindow import GenerateKeyWindow


class GenerateDeleteKeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GenerateDeleteKeysWindow()
        self.ui.setupUi(self)

        self.ui.generateKeyButton.clicked.connect(lambda: WindowManager.openWindow(self, GenerateKeyWindow))
