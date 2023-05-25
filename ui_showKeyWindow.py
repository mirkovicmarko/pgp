# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showKeyWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ShowKeyWindow(object):
    def setupUi(self, ShowKeyWindow):
        if not ShowKeyWindow.objectName():
            ShowKeyWindow.setObjectName(u"ShowKeyWindow")
        ShowKeyWindow.resize(800, 600)
        ShowKeyWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"color: white;\n"
"font-size: 12pt;")
        self.centralwidget = QWidget(ShowKeyWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.userlabel = QLabel(self.centralwidget)
        self.userlabel.setObjectName(u"userlabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userlabel.sizePolicy().hasHeightForWidth())
        self.userlabel.setSizePolicy(sizePolicy)
        self.userlabel.setStyleSheet(u"background-color: rgb(74, 74, 74);\n"
"font-size: 20pt;")
        self.userlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.userlabel)

        self.keyLabel = QLabel(self.centralwidget)
        self.keyLabel.setObjectName(u"keyLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.keyLabel.sizePolicy().hasHeightForWidth())
        self.keyLabel.setSizePolicy(sizePolicy1)
        self.keyLabel.setStyleSheet(u"font-size: 20pt;")
        self.keyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.keyLabel)

        self.buttonsHorizontalLayout = QHBoxLayout()
        self.buttonsHorizontalLayout.setObjectName(u"buttonsHorizontalLayout")
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonsHorizontalLayout.addWidget(self.deleteButton)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")

        self.buttonsHorizontalLayout.addWidget(self.exportButton)


        self.verticalLayout.addLayout(self.buttonsHorizontalLayout)

        ShowKeyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShowKeyWindow)

        QMetaObject.connectSlotsByName(ShowKeyWindow)
    # setupUi

    def retranslateUi(self, ShowKeyWindow):
        ShowKeyWindow.setWindowTitle(QCoreApplication.translate("ShowKeyWindow", u"Show key", None))
        self.userlabel.setText(QCoreApplication.translate("ShowKeyWindow", u"user", None))
        self.keyLabel.setText(QCoreApplication.translate("ShowKeyWindow", u"key", None))
        self.deleteButton.setText(QCoreApplication.translate("ShowKeyWindow", u"Delete", None))
        self.exportButton.setText(QCoreApplication.translate("ShowKeyWindow", u"Export", None))
    # retranslateUi

