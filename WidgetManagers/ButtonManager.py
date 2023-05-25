from PySide6.QtWidgets import QPushButton


class ButtonManager:
    @staticmethod
    def createButtonWithTitle(self, title):
        return QPushButton(title)

    @staticmethod
    def setButtonStileSheet(self, button, stileSheet):
        button.setStileSheet(stileSheet)
        