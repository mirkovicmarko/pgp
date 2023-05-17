# This Python file uses the following encoding: utf-8

import PySide6.QtCore as QtCore

# Utility class for window management. Pass in the parent and the window you want to open.
# The parent will disappear upon window opening, and reappear upon window closure.
class WindowManager:
    openedWindows = {}

    @classmethod
    def openWindow(classRef, parent, window):
        if(parent.winId() not in classRef.openedWindows.keys()):
            classRef.openedWindows[parent.winId()] = {}

        if(window in classRef.openedWindows[parent.winId()].keys()):
            return

        newWindowObject = window()
        classRef.openedWindows[parent.winId()][window] = newWindowObject
        # Destroy the object on closure
        newWindowObject.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # Cleanup on closure
        newWindowObject.destroyed.connect(lambda: WindowManager.windowClosed(parent, window))
        parent.hide()
        newWindowObject.show()

    @classmethod
    def windowClosed(classRef, parent, window):
        del classRef.openedWindows[parent.winId()][window]
        parent.show()
