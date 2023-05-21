from PySide6.QtWidgets import QMainWindow

from ui_keysWindow import Ui_KeysWindow

from windowManager import WindowManager
from generateDeleteKeysWindow import GenerateDeleteKeysWindow
from importExportKeysWindow import ImportExportKeysWindow
from allKeyringsWindow import AllKeyringsWindow

class KeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_KeysWindow()
        self.ui.setupUi(self)

        self.ui.generateDeleteButton.clicked.connect(lambda: WindowManager.openWindow(self, GenerateDeleteKeysWindow))
        self.ui.importExportButton.clicked.connect(lambda: WindowManager.openWindow(self, ImportExportKeysWindow))
        self.ui.keyringsButton.clicked.connect(lambda: WindowManager.openWindow(self, AllKeyringsWindow))
