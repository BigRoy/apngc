import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QStyleFactory

from .constants import PACKAGE
from .ui import ApngConverter


def start():
    # need this for some reason, otherwise QUiLoader freezes app
    test = QUiLoader()

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("windows"))

    # ICON
    icon_path = os.path.join(PACKAGE, "ui", "icons", "app.png")
    icon = QIcon(icon_path)
    app.setWindowIcon(icon)

    window = ApngConverter()
    window.show()
    sys.exit(app.exec())
