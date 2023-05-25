from PySide6.QtWidgets import QPushButton


class ButtonManager:
    def createButtonWithTitle(self, title):
        return QPushButton(title)

    def setButtonStileSheet(self, button, stileSheet):
        button.setStileSheet(stileSheet)
        