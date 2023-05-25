from PySide6.QtWidgets import QPushButton


class ButtonManager:
    @staticmethod
    def createButtonWithTitle(title):
        return QPushButton(title)

    @staticmethod
    def setButtonStyleSheet(button, styleSheet):
        button.setStyleSheet(styleSheet)
        