from PySide6.QtWidgets import QMainWindow, QPushButton

from WidgetManagers.ButtonManager import ButtonManager
from WidgetManagers.LayoutManager import LayoutManager
from ui_allKeyringsWindow import Ui_AllKeyringsWindow


class AllKeyringsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AllKeyringsWindow()
        self.ui.setupUi(self)

        publicB = 3
        privateB = 1

        for i in range(0, publicB):
            button = ButtonManager.createButtonWithTitle("Button" + str(i))
            LayoutManager.addButtonToLayout(button, self.ui.publicVerticalLayout)

        for i in range(0, privateB):
            button = ButtonManager.createButtonWithTitle("Button" + str(i))
            LayoutManager.addButtonToLayout(button, self.ui.privateVerticalLayout)
