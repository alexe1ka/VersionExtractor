from PyQt5 import QtCore, uic, QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import VersionExtractorMainWindow

import ui


class ExtractorWindow(QMainWindow,QTreeView):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # uic.loadUi("gui.ui", self)
        self.ui = VersionExtractorMainWindow.Ui_VersionExtractor_by_Alexe1ka()
        self.ui.setupUi(self)

        model = QFileSystemModel()
        model.setRootPath(QtCore.QDir.currentPath())
        self.ui.catalogsTreeView.setModel(model)




# app = QtWidgets.QApplication(sys.argv)
# window = QWidget()
# window = uic.loadUi("gui.ui")
# window.show()
# sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ExtractorWindow()
    window.show()
    sys.exit(app.exec_())
