from PySide6.QtWidgets import QMainWindow, QPushButton

from ui_allKeyringsWindow import Ui_AllKeyringsWindow


class AllKeyringsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AllKeyringsWindow()
        self.ui.setupUi(self)

        publicB = 3
        privateB = 1

        for i in range(0, publicB):
            button = self.createButton("Button" + str(i))
            self.addButton(button, self.ui.publicVerticalLayout)

        for i in range(0, privateB):
            button = self.createButton("Button" + str(i))
            self.addButton(button, self.ui.privateVerticalLayout)

    def createButton(self, title):
        return QPushButton(title)

    def addButton(self, button, layout):
        layout.addWidget(button)
