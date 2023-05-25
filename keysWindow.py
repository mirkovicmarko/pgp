from PySide6.QtWidgets import QMainWindow

from ui_keysWindow import Ui_KeysWindow

from windowManager import WindowManager
from generateKeysWindow import GenerateKeysWindow
from importKeysWindow import ImportKeysWindow
from allKeyringsWindow import AllKeyringsWindow


class KeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_KeysWindow()
        self.ui.setupUi(self)

        self.ui.generateButton.clicked.connect(lambda: WindowManager.openWindow(self, GenerateKeysWindow))
        self.ui.importButton.clicked.connect(lambda: WindowManager.openWindow(self, ImportKeysWindow))
        self.ui.seeAllKeyringsButton.clicked.connect(lambda: WindowManager.openWindow(self, AllKeyringsWindow))
