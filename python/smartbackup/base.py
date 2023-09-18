#!/usr/bin/env python
from PySide2 import QtCore


class SmartBackupBase(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartBackupBase, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        QtCore.QCoreApplication.setApplicationName("smartbackup")
        QtCore.QCoreApplication.setOrganizationName("PJain")

    @property
    def configure_window_title(self):
        return "Smart Backup Configurator"

    @property
    def settings(self):
        settings = QtCore.QSettings(
            "{0}.ini".format("smartbackup"), QtCore.QSettings.IniFormat
        )
        return settings

    @property
    def databasename(self):
        return "smartbackup_db.db"
