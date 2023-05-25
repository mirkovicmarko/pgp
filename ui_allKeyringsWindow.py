# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allKeyringsWindow.ui'
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
                               QScrollArea, QSizePolicy, QVBoxLayout, QWidget)


class Ui_AllKeyringsWindow(object):
    def setupUi(self, AllKeyringsWindow):
        if not AllKeyringsWindow.objectName():
            AllKeyringsWindow.setObjectName(u"AllKeyringsWindow")
        AllKeyringsWindow.resize(800, 600)
        AllKeyringsWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                        "color: white;\n"
                                        "font-size: 12pt;")
        self.centralwidget = QWidget(AllKeyringsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                      "color: white;\n"
                                      "font-size: 26pt;")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.publicScrollArea = QScrollArea(self.centralwidget)
        self.publicScrollArea.setObjectName(u"publicScrollArea")
        self.publicScrollArea.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                            "color: white;\n"
                                            "font-size: 20pt;")
        self.publicScrollArea.setWidgetResizable(True)
        self.publicScrollAreaWidgetContents = QWidget()
        self.publicScrollAreaWidgetContents.setObjectName(u"publicScrollAreaWidgetContents")
        self.publicScrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 533))
        self.publicVerticalLayout = QVBoxLayout(self.publicScrollAreaWidgetContents)
        self.publicVerticalLayout.setObjectName(u"publicVerticalLayout")
        self.publicTitleLabel = QLabel(self.publicScrollAreaWidgetContents)
        self.publicTitleLabel.setObjectName(u"publicTitleLabel")
        self.publicTitleLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                            "color: white;\n"
                                            "font-size: 20pt;")
        self.publicTitleLabel.setAlignment(Qt.AlignCenter)

        self.publicVerticalLayout.addWidget(self.publicTitleLabel)

        self.publicScrollArea.setWidget(self.publicScrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.publicScrollArea)

        self.privateScrollArea = QScrollArea(self.centralwidget)
        self.privateScrollArea.setObjectName(u"privateScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.privateScrollArea.sizePolicy().hasHeightForWidth())
        self.privateScrollArea.setSizePolicy(sizePolicy)
        self.privateScrollArea.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                             "color: white;\n"
                                             "font-size: 20pt;")
        self.privateScrollArea.setWidgetResizable(True)
        self.privateScrollAreaWidgetContents = QWidget()
        self.privateScrollAreaWidgetContents.setObjectName(u"privateScrollAreaWidgetContents")
        self.privateScrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 533))
        self.privateVerticalLayout = QVBoxLayout(self.privateScrollAreaWidgetContents)
        self.privateVerticalLayout.setObjectName(u"privateVerticalLayout")
        self.privateTitleLabel = QLabel(self.privateScrollAreaWidgetContents)
        self.privateTitleLabel.setObjectName(u"privateTitleLabel")
        self.privateTitleLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
                                             "color: white;\n"
                                             "font-size: 20pt;")
        self.privateTitleLabel.setAlignment(Qt.AlignCenter)

        self.privateVerticalLayout.addWidget(self.privateTitleLabel)

        self.privateScrollArea.setWidget(self.privateScrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.privateScrollArea)

        self.verticalLayout.addLayout(self.horizontalLayout)

        AllKeyringsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AllKeyringsWindow)

        QMetaObject.connectSlotsByName(AllKeyringsWindow)

    # setupUi

    def retranslateUi(self, AllKeyringsWindow):
        AllKeyringsWindow.setWindowTitle(QCoreApplication.translate("AllKeyringsWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("AllKeyringsWindow", u"All keyrings", None))
        self.publicTitleLabel.setText(QCoreApplication.translate("AllKeyringsWindow", u"Public keyrings", None))
        self.privateTitleLabel.setText(QCoreApplication.translate("AllKeyringsWindow", u"Private keyrings", None))
    # retranslateUi
