from PySide6.QtWidgets import QPushButton


class ButtonManager:
    @staticmethod
    def createButtonWithTitle(title):
        return QPushButton(title)

    @staticmethod
    def setButtonStileSheet(button, stileSheet):
        button.setStileSheet(stileSheet)
        