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

        self.generateDeleteButton = QPushButton(self.centralwidget)
        self.generateDeleteButton.setObjectName(u"generateDeleteButton")
        sizePolicy.setHeightForWidth(self.generateDeleteButton.sizePolicy().hasHeightForWidth())
        self.generateDeleteButton.setSizePolicy(sizePolicy)
        self.generateDeleteButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.generateDeleteButton)

        self.importExportButton = QPushButton(self.centralwidget)
        self.importExportButton.setObjectName(u"importExportButton")
        sizePolicy.setHeightForWidth(self.importExportButton.sizePolicy().hasHeightForWidth())
        self.importExportButton.setSizePolicy(sizePolicy)
        self.importExportButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.importExportButton)

        self.keyringsButton = QPushButton(self.centralwidget)
        self.keyringsButton.setObjectName(u"keyringsButton")
        sizePolicy.setHeightForWidth(self.keyringsButton.sizePolicy().hasHeightForWidth())
        self.keyringsButton.setSizePolicy(sizePolicy)
        self.keyringsButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.keyringsButton)

        KeysWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeysWindow)

        QMetaObject.connectSlotsByName(KeysWindow)
    # setupUi

    def retranslateUi(self, KeysWindow):
        KeysWindow.setWindowTitle(QCoreApplication.translate("KeysWindow", u"Keys", None))
        self.titleLabel.setText(QCoreApplication.translate("KeysWindow", u"Key functions", None))
        self.generateDeleteButton.setText(QCoreApplication.translate("KeysWindow", u"GENERATE/DELETE", None))
        self.importExportButton.setText(QCoreApplication.translate("KeysWindow", u"IMPORT/EXPORT", None))
        self.keyringsButton.setText(QCoreApplication.translate("KeysWindow", u"KEYRINGS", None))
    # retranslateUi

