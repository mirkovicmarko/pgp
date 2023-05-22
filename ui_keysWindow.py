# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keysWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_KeysWindow(object):
    def setupUi(self, KeysWindow):
        if not KeysWindow.objectName():
            KeysWindow.setObjectName(u"KeysWindow")
        KeysWindow.resize(800, 600)
        KeysWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"color: white;\n"
"font-size: 12pt;")
        KeysWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(KeysWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMaximumSize(QSize(16777215, 40))
        self.titleLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"color: white;\n"
"font-size: 26pt;")
        self.titleLabel.setLineWidth(0)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy)
        self.generateButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.generateButton)

        self.importButton = QPushButton(self.centralwidget)
        self.importButton.setObjectName(u"importButton")
        sizePolicy.setHeightForWidth(self.importButton.sizePolicy().hasHeightForWidth())
        self.importButton.setSizePolicy(sizePolicy)
        self.importButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.importButton)

        self.seeAllKeyringsButton = QPushButton(self.centralwidget)
        self.seeAllKeyringsButton.setObjectName(u"seeAllKeyringsButton")
        sizePolicy.setHeightForWidth(self.seeAllKeyringsButton.sizePolicy().hasHeightForWidth())
        self.seeAllKeyringsButton.setSizePolicy(sizePolicy)
        self.seeAllKeyringsButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.seeAllKeyringsButton)

        KeysWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeysWindow)

        QMetaObject.connectSlotsByName(KeysWindow)
    # setupUi

    def retranslateUi(self, KeysWindow):
        KeysWindow.setWindowTitle(QCoreApplication.translate("KeysWindow", u"Keys", None))
        self.titleLabel.setText(QCoreApplication.translate("KeysWindow", u"Key functions", None))
        self.generateButton.setText(QCoreApplication.translate("KeysWindow", u"GENERATE YOUR KEYS", None))
        self.importButton.setText(QCoreApplication.translate("KeysWindow", u"IMPORT KEYS", None))
        self.seeAllKeyringsButton.setText(QCoreApplication.translate("KeysWindow", u"SEE ALL KEYRINGS", None))
    # retranslateUi

