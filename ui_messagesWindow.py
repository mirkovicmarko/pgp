# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messagesWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

class Ui_MessagesWindow(object):
    def setupUi(self, MessagesWindow):
        if not MessagesWindow.objectName():
            MessagesWindow.setObjectName(u"MessagesWindow")
        MessagesWindow.resize(800, 600)
        self.centralwidget = QWidget(MessagesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MessagesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MessagesWindow)

        QMetaObject.connectSlotsByName(MessagesWindow)
    # setupUi

    def retranslateUi(self, MessagesWindow):
        MessagesWindow.setWindowTitle(QCoreApplication.translate("MessagesWindow", u"Messages", None))
    # retranslateUi

