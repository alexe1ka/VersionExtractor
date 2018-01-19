import VersionExtractorMainWindow
from PyQt5 import QtCore, uic, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


# pyuic5 input.ui -o output.py


class ExtractorWindow(QMainWindow, QTreeView):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # uic.loadUi("gui.ui", self)
        self.ui = VersionExtractorMainWindow.Ui_version_extractor_by_alexe1ka()  # устанавливаем в ui мой нарисованный интерфейс из qtDesigner'a,сгенерированный в python
        self.ui.setupUi(self)

        model = QFileSystemModel()
        model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)  # в treeView - только каталоги
        # model.setFilter(QtCore.QDir.Files)  # фильтр на "только файлы"
        model.setRootPath(QtCore.QDir.currentPath())
        self.ui.catalogTreeView.setModel(model)
        # скрытие параметров директори
        self.ui.catalogTreeView.setColumnHidden(1, True)
        self.ui.catalogTreeView.setColumnHidden(2, True)
        self.ui.catalogTreeView.setColumnHidden(3, True)

        # self.ui.openCatalogBtn.clicked(self.ui.catalogsTreeView.currentIndex())

        # index = self.ui.catalogsTreeView.selectedIndexes()
        # self.ui.currentCatalogFiles.conn
        # print(index)

        # index = self.ui.catalogsTreeView.currentIndex()
        # print(index)
        # files_model = QFileSystemModel()
        # files_model.data(index)
        # files_model.setFilter(QtCore.QDir.Files ) #| QtCore.QDir.NoDotAndDotDot
        # self.ui.currentFilesTreeView.setModel(files_model)
        # self.ui.currentFilesTreeView.setColumnHidden(1, True)
        # self.ui.currentFilesTreeView.setColumnHidden(2, True)
        # self.ui.currentFilesTreeView.setColumnHidden(3, True)

        # self.ui.currentCatalogFiles.setModel()


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
