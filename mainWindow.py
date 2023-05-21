from PySide6.QtWidgets import QMainWindow

from ui_mainWindow import Ui_MainWindow

from windowManager import WindowManager
from messagesWindow import MessagesWindow
from keysWindow import KeysWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.messagesButton.clicked.connect(lambda: WindowManager.openWindow(self, MessagesWindow))
        self.ui.keysButton.clicked.connect(lambda: WindowManager.openWindow(self, KeysWindow))
