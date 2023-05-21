from PySide6.QtWidgets import QMainWindow

from ui_importExportKeysWindow import Ui_ImportExportKeysWindow

class ImportExportKeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImportExportKeysWindow()
        self.ui.setupUi(self)
