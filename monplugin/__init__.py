from typing import Any

from PyQt5.QtWidgets import QAction, QMessageBox

import qgis


def classFactory(iface):
    return MinimalPlugin(iface)


class MinimalPlugin:

    def __init__(self, iface: Any):
        a: str = 4
        print(a)
        self.iface = iface

    def initGui(self) -> int:
        self.action = QAction('Go!', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        QMessageBox.information(None, 'Minimal plugin', 'Do something useful here')
        QMessageBox.information(None, 'Minimal plugin', 'or here')
        QMessageBox.information(None, 'Minimal plugin', 'and maybe here also')


print(qgis)
