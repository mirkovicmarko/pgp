from PySide6.QtWidgets import QMainWindow

from ui_allKeyringsWindow import Ui_AllKeyringsWindow

class AllKeyringsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AllKeyringsWindow()
        self.ui.setupUi(self)
