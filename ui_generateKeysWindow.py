# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generateKeysWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QRadioButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_GenerateKeysWindow(object):
    def setupUi(self, GenerateKeysWindow):
        if not GenerateKeysWindow.objectName():
            GenerateKeysWindow.setObjectName(u"GenerateKeysWindow")
        GenerateKeysWindow.setEnabled(True)
        GenerateKeysWindow.resize(800, 600)
        GenerateKeysWindow.setLayoutDirection(Qt.LeftToRight)
        GenerateKeysWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                         "color: white;\n"
                                         "font-size: 12pt;")
        GenerateKeysWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(GenerateKeysWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setLayoutDirection(Qt.LeftToRight)
        self.titleLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                      "color: white;\n"
                                      "font-size: 26pt;")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.titleLabel)

        self.nameGroupBox = QGroupBox(self.centralwidget)
        self.nameGroupBox.setObjectName(u"nameGroupBox")
        sizePolicy.setHeightForWidth(self.nameGroupBox.sizePolicy().hasHeightForWidth())
        self.nameGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.nameGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit = QLineEdit(self.nameGroupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.verticalLayout_5.addWidget(self.nameGroupBox)

        self.emailGroupBox = QGroupBox(self.centralwidget)
        self.emailGroupBox.setObjectName(u"emailGroupBox")
        sizePolicy.setHeightForWidth(self.emailGroupBox.sizePolicy().hasHeightForWidth())
        self.emailGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.emailGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_2 = QLineEdit(self.emailGroupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout_3.addWidget(self.lineEdit_2)

        self.verticalLayout_5.addWidget(self.emailGroupBox)

        self.asymmetricKeyAlgGroupBox = QGroupBox(self.centralwidget)
        self.asymmetricKeyAlgGroupBox.setObjectName(u"asymmetricKeyAlgGroupBox")
        sizePolicy.setHeightForWidth(self.asymmetricKeyAlgGroupBox.sizePolicy().hasHeightForWidth())
        self.asymmetricKeyAlgGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.asymmetricKeyAlgGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rsaRadioButton = QRadioButton(self.asymmetricKeyAlgGroupBox)
        self.rsaRadioButton.setObjectName(u"rsaRadioButton")
        self.rsaRadioButton.setChecked(True)
        self.rsaRadioButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.rsaRadioButton)

        self.dsaRadioButton = QRadioButton(self.asymmetricKeyAlgGroupBox)
        self.dsaRadioButton.setObjectName(u"dsaRadioButton")

        self.verticalLayout.addWidget(self.dsaRadioButton)

        self.verticalLayout_5.addWidget(self.asymmetricKeyAlgGroupBox)

        self.keyLengthGroupBox = QGroupBox(self.centralwidget)
        self.keyLengthGroupBox.setObjectName(u"keyLengthGroupBox")
        sizePolicy.setHeightForWidth(self.keyLengthGroupBox.sizePolicy().hasHeightForWidth())
        self.keyLengthGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.keyLengthGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.len1024radioButton = QRadioButton(self.keyLengthGroupBox)
        self.len1024radioButton.setObjectName(u"len1024radioButton")
        self.len1024radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.len1024radioButton)

        self.len2048radioButton = QRadioButton(self.keyLengthGroupBox)
        self.len2048radioButton.setObjectName(u"len2048radioButton")
        self.len2048radioButton.setChecked(False)

        self.verticalLayout_2.addWidget(self.len2048radioButton)

        self.verticalLayout_5.addWidget(self.keyLengthGroupBox)

        self.cancelGenerateLayout = QHBoxLayout()
        self.cancelGenerateLayout.setObjectName(u"cancelGenerateLayout")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.cancelGenerateLayout.addWidget(self.cancelButton)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy)
        self.generateButton.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.cancelGenerateLayout.addWidget(self.generateButton)

        self.verticalLayout_5.addLayout(self.cancelGenerateLayout)

        GenerateKeysWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateKeysWindow)

        QMetaObject.connectSlotsByName(GenerateKeysWindow)

    # setupUi

    def retranslateUi(self, GenerateKeysWindow):
        GenerateKeysWindow.setWindowTitle(QCoreApplication.translate("GenerateKeysWindow", u"Generate key", None))
        # if QT_CONFIG(tooltip)
        GenerateKeysWindow.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.titleLabel.setText(
            QCoreApplication.translate("GenerateKeysWindow", u"Please fill the following form to generate your keys",
                                       None))
        self.nameGroupBox.setTitle(QCoreApplication.translate("GenerateKeysWindow", u"Name:", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("GenerateKeysWindow", u"Enter your name here...", None))
        self.emailGroupBox.setTitle(QCoreApplication.translate("GenerateKeysWindow", u"E-mail:", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("GenerateKeysWindow", u"Enter your e-mail here..", None))
        self.asymmetricKeyAlgGroupBox.setTitle(
            QCoreApplication.translate("GenerateKeysWindow", u"Asymmetric key algorithm:", None))
        self.rsaRadioButton.setText(QCoreApplication.translate("GenerateKeysWindow", u"RSA", None))
        self.dsaRadioButton.setText(QCoreApplication.translate("GenerateKeysWindow", u"DSA + ElGamal", None))
        self.keyLengthGroupBox.setTitle(QCoreApplication.translate("GenerateKeysWindow", u"Key length:", None))
        self.len1024radioButton.setText(QCoreApplication.translate("GenerateKeysWindow", u"1024", None))
        self.len2048radioButton.setText(QCoreApplication.translate("GenerateKeysWindow", u"2048", None))
        self.cancelButton.setText(QCoreApplication.translate("GenerateKeysWindow", u"Cancel", None))
        self.generateButton.setText(QCoreApplication.translate("GenerateKeysWindow", u"Generate", None))
    # retranslateUi
