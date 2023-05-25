from PySide6.QtWidgets import QMainWindow

from ui_generateKeysWindow import Ui_GenerateKeysWindow

from windowManager import WindowManager
from keyPassWindow import KeyPassWindow


class GenerateKeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GenerateKeysWindow()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(lambda: WindowManager.windowClosed(self, GenerateKeysWindow))
        self.ui.generateButton.clicked.connect(lambda: WindowManager.openWindow(self, KeyPassWindow))
