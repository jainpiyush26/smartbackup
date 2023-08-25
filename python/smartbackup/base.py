#!/usr/bin/env python


class SmartBackupBase(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartBackupBase, cls).__new__(cls)
        cls._instance

    @property
    def configure_window_title(self):
        return "Smart Backup Configurator"
