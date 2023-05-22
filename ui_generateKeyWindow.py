# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generateKeyWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGroupBox,
    QLabel, QMainWindow, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_GenerateKeyWindow(object):
    def setupUi(self, GenerateKeyWindow):
        if not GenerateKeyWindow.objectName():
            GenerateKeyWindow.setObjectName(u"GenerateKeyWindow")
        GenerateKeyWindow.setEnabled(True)
        GenerateKeyWindow.resize(800, 600)
        GenerateKeyWindow.setLayoutDirection(Qt.LeftToRight)
        GenerateKeyWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"color: white;\n"
"font-size: 12pt;")
        GenerateKeyWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(GenerateKeyWindow)
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
        self.verticalLayout_4 = QVBoxLayout(self.nameGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nameTextEdit = QTextEdit(self.nameGroupBox)
        self.nameTextEdit.setObjectName(u"nameTextEdit")
        self.nameTextEdit.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout_4.addWidget(self.nameTextEdit)


        self.verticalLayout_5.addWidget(self.nameGroupBox)

        self.emailGroupBox = QGroupBox(self.centralwidget)
        self.emailGroupBox.setObjectName(u"emailGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.emailGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.emailTextEdit = QTextEdit(self.emailGroupBox)
        self.emailTextEdit.setObjectName(u"emailTextEdit")
        self.emailTextEdit.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout_3.addWidget(self.emailTextEdit)


        self.verticalLayout_5.addWidget(self.emailGroupBox)

        self.asymmetricKeyAlgGroupBox = QGroupBox(self.centralwidget)
        self.asymmetricKeyAlgGroupBox.setObjectName(u"asymmetricKeyAlgGroupBox")
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

        self.saveDontSaveDialogButtonBox = QDialogButtonBox(self.centralwidget)
        self.saveDontSaveDialogButtonBox.setObjectName(u"saveDontSaveDialogButtonBox")
        self.saveDontSaveDialogButtonBox.setStyleSheet(u"background-color: rgb(74, 74, 74);")
        self.saveDontSaveDialogButtonBox.setStandardButtons(QDialogButtonBox.Discard|QDialogButtonBox.Save)
        self.saveDontSaveDialogButtonBox.setCenterButtons(True)

        self.verticalLayout_5.addWidget(self.saveDontSaveDialogButtonBox)

        GenerateKeyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateKeyWindow)

        QMetaObject.connectSlotsByName(GenerateKeyWindow)
    # setupUi

    def retranslateUi(self, GenerateKeyWindow):
        GenerateKeyWindow.setWindowTitle(QCoreApplication.translate("GenerateKeyWindow", u"Generate key", None))
#if QT_CONFIG(tooltip)
        GenerateKeyWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.titleLabel.setText(QCoreApplication.translate("GenerateKeyWindow", u"Please fill the following form to generate your keys", None))
        self.nameGroupBox.setTitle(QCoreApplication.translate("GenerateKeyWindow", u"Name:", None))
        self.emailGroupBox.setTitle(QCoreApplication.translate("GenerateKeyWindow", u"E-mail:", None))
        self.asymmetricKeyAlgGroupBox.setTitle(QCoreApplication.translate("GenerateKeyWindow", u"Asymmetric key algorithm:", None))
        self.rsaRadioButton.setText(QCoreApplication.translate("GenerateKeyWindow", u"RSA", None))
        self.dsaRadioButton.setText(QCoreApplication.translate("GenerateKeyWindow", u"DSA", None))
        self.keyLengthGroupBox.setTitle(QCoreApplication.translate("GenerateKeyWindow", u"Key length:", None))
        self.len1024radioButton.setText(QCoreApplication.translate("GenerateKeyWindow", u"1024", None))
        self.len2048radioButton.setText(QCoreApplication.translate("GenerateKeyWindow", u"2048", None))
    # retranslateUi

