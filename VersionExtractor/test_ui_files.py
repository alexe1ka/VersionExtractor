from PyQt5 import QtCore, uic, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import sys


app = QtWidgets.QApplication(sys.argv)
window = QWidget()
window = uic.loadUi("gui_compon.ui")
window.show()
sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ExtractorWindow()
    window.show()
    sys.exit(app.exec_())