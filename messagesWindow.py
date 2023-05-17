from PySide6.QtWidgets import QMainWindow

from ui_messagesWindow import Ui_MessagesWindow

class MessagesWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MessagesWindow()
        self.ui.setupUi(self)
