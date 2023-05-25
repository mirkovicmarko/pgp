from PySide6.QtWidgets import QMainWindow

from ui_keyPassWindow import Ui_KeyPassWindow


class KeyPassWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_KeyPassWindow()
        self.ui.setupUi(self)
