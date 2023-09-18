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


class ConfigureAppUi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.base = SmartBackupBase()
        self.settings = self.base.settings
        # Do the basic setups
        self.default_setups()
        # Adding the UI elements
        self.add_ui_elements()
        # Adding the call events
        self.add_element_events()

    def default_setups(self):
        """Sets up default bits like window title, size etc"""
        # set the title of the window
        self.setWindowTitle(self.base.configure_window_title)
        _height = int(self.settings.value("WindowSize/width", 750))
        _width = int(self.settings.value("WindowSize/height", 450))
        self.resize(_height, _width)

    def add_ui_elements(self) -> None:
        """Adds all the necessary UI elements"""
        # Add table view

        # Add path entries
        self.addbtn = QtWidgets.QPushButton("Add", self)
        self.removebtn = QtWidgets.QPushButton("Remove", self)
        self.hbtnbox = QtWidgets.QVBoxLayout()
        self.hbtnbox.addWidget(self.addbtn)
        self.hbtnbox.addWidget(self.removebtn)
        # Add sync status view
        # Add push buttons
        self.savebtn = QtWidgets.QPushButton("Save and Exit", self)
        self.closebtn = QtWidgets.QPushButton("Exit", self)
        self.btnhbox = QtWidgets.QHBoxLayout()
        self.btnhbox.addWidget(self.savebtn)
        self.btnhbox.addWidget(self.closebtn)
        # Adding the line edit
        self.dbpath_label = QtWidgets.QLabel("DB Path", self)
        self.dbpath = QtWidgets.QLineEdit(self)
        self.dbpath.setReadOnly(True)
        self.dbbox = QtWidgets.QHBoxLayout()
        self.dbbox.addWidget(self.dbpath_label)
        self.dbbox.addWidget(self.dbpath)
        # Setting up the main layout
        self.mainlayout = QtWidgets.QVBoxLayout()
        self.mainlayout.addLayout(self.hbtnbox)
        self.mainlayout.addLayout(self.dbbox)
        self.mainlayout.addLayout(self.btnhbox)
        self.setLayout(self.mainlayout)

    def add_element_events(self) -> None:
        # Events when calling the buttons
        self.closebtn.clicked.connect(self.close)

    def close(self) -> bool:
        # Setting the height and the width
        print("Calling close??")
        self.settings.beginGroup("WindowSize")
        self.settings.setValue("height", self.height())
        self.settings.setValue("width", self.width())
        self.settings.endGroup()
        return super().close()


class ConfigureApp(object):
    @classmethod
    def run(cls):
        """_summary_"""
        app = QtWidgets.QApplication(sys.argv)
        window = ConfigureAppUi()
        window.show()
        app.exec_()
