# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generateDeleteKeysWindow.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_GenerateDeleteKeysWindow(object):
    def setupUi(self, GenerateDeleteKeysWindow):
        if not GenerateDeleteKeysWindow.objectName():
            GenerateDeleteKeysWindow.setObjectName(u"GenerateDeleteKeysWindow")
        GenerateDeleteKeysWindow.resize(800, 600)
        GenerateDeleteKeysWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"color: white;\n"
"font-size: 12pt;")
        self.centralwidget = QWidget(GenerateDeleteKeysWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.generateKeyButton = QPushButton(self.centralwidget)
        self.generateKeyButton.setObjectName(u"generateKeyButton")
        sizePolicy.setHeightForWidth(self.generateKeyButton.sizePolicy().hasHeightForWidth())
        self.generateKeyButton.setSizePolicy(sizePolicy)
        self.generateKeyButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.generateKeyButton)

        self.deleteKeyButton = QPushButton(self.centralwidget)
        self.deleteKeyButton.setObjectName(u"deleteKeyButton")
        sizePolicy.setHeightForWidth(self.deleteKeyButton.sizePolicy().hasHeightForWidth())
        self.deleteKeyButton.setSizePolicy(sizePolicy)
        self.deleteKeyButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.deleteKeyButton)

        GenerateDeleteKeysWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateDeleteKeysWindow)

        QMetaObject.connectSlotsByName(GenerateDeleteKeysWindow)
    # setupUi

    def retranslateUi(self, GenerateDeleteKeysWindow):
        GenerateDeleteKeysWindow.setWindowTitle(QCoreApplication.translate("GenerateDeleteKeysWindow", u"Generate and delete keys", None))
        self.titleLabel.setText(QCoreApplication.translate("GenerateDeleteKeysWindow", u"Here you can generate and delete your keys", None))
        self.generateKeyButton.setText(QCoreApplication.translate("GenerateDeleteKeysWindow", u"Generate key", None))
        self.deleteKeyButton.setText(QCoreApplication.translate("GenerateDeleteKeysWindow", u"Delete key", None))
    # retranslateUi

