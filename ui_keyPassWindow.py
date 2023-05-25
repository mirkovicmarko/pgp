# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyPassWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_KeyPassWindow(object):
    def setupUi(self, KeyPassWindow):
        if not KeyPassWindow.objectName():
            KeyPassWindow.setObjectName(u"KeyPassWindow")
        KeyPassWindow.resize(400, 300)
        KeyPassWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                    "color: white;\n"
                                    "font-size: 12pt;")
        self.centralwidget = QWidget(KeyPassWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                      "color: white;\n"
                                      "font-size: 20pt;")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.passphaseGroupBox = QGroupBox(self.centralwidget)
        self.passphaseGroupBox.setObjectName(u"passphaseGroupBox")
        sizePolicy.setHeightForWidth(self.passphaseGroupBox.sizePolicy().hasHeightForWidth())
        self.passphaseGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.passphaseGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.passphaseLineEdit = QLineEdit(self.passphaseGroupBox)
        self.passphaseLineEdit.setObjectName(u"passphaseLineEdit")
        self.passphaseLineEdit.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout_2.addWidget(self.passphaseLineEdit)

        self.verticalLayout.addWidget(self.passphaseGroupBox)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy1)
        self.okButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout.addWidget(self.okButton)

        KeyPassWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeyPassWindow)

        QMetaObject.connectSlotsByName(KeyPassWindow)

    # setupUi

    def retranslateUi(self, KeyPassWindow):
        KeyPassWindow.setWindowTitle(QCoreApplication.translate("KeyPassWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("KeyPassWindow", u"Please enter the passphase below", None))
        self.passphaseGroupBox.setTitle(QCoreApplication.translate("KeyPassWindow", u"Passphrase:", None))
        self.passphaseLineEdit.setPlaceholderText(
            QCoreApplication.translate("KeyPassWindow", u"Enter your passphase here...", None))
        self.okButton.setText(QCoreApplication.translate("KeyPassWindow", u"OK", None))
    # retranslateUi
