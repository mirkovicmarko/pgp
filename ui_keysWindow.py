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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

class Ui_KeysWindow(object):
    def setupUi(self, KeysWindow):
        if not KeysWindow.objectName():
            KeysWindow.setObjectName(u"KeysWindow")
        KeysWindow.resize(800, 600)
        self.centralwidget = QWidget(KeysWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        KeysWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeysWindow)

        QMetaObject.connectSlotsByName(KeysWindow)
    # setupUi

    def retranslateUi(self, KeysWindow):
        KeysWindow.setWindowTitle(QCoreApplication.translate("KeysWindow", u"Keys", None))
    # retranslateUi

