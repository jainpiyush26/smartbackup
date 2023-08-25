#!/usr/bin/env python
# std imports
import os
import tempfile
import re
import sys
import yaml
from PySide2 import QtCore, QtGui, QtWidgets

# internal imports
from smartbackup.base import SmartBackupBase


class ConfigureAppUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.base = SmartBackupBase()
        # Do the basic setups
        self.default_setups()

    def default_setups(self):
        # set the title of the window
        self.setWindowTitle(self.base.configure_window_title)


class ConfigureApp(object):
    def run():
        """_summary_"""
        app = QtWidgets.QApplication(sys.argv)
        window = ConfigureAppUi()
        window.show()
        app.exec_()
