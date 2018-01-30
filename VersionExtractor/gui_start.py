import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *

import VersionExtractorMainWindow
from catalog_parser import HdlTasker


# pyuic5 input.ui -o output.py


class ExtractorWindow(QMainWindow, QTreeView):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # uic.loadUi("gui.ui", self)
        self.ui = VersionExtractorMainWindow.Ui_version_extractor_by_alexe1ka()  # сгенерированный класс из Designer'a
        self.ui.setupUi(self)

        # потоки для выполнения тяжелых фоновых задач
        self.tasker = HdlTasker()
        self.thread = QThread()
        self.tasker.moveToThread(self.thread)
        self.thread.start()

        self.file_path = ""  # текущий каталог
        self.files = []  # список файлов в текущем каталоге
        self.hdl_files_list = []  # список найденных hdl файлов

        self.ui.progressBar.moveToThread(self.thread)

        model = QFileSystemModel()
        model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)  # в treeView - только каталоги
        model.setRootPath(QtCore.QDir.currentPath())
        self.ui.catalogTreeView.setModel(model)

        # скрытие параметров директори
        self.ui.catalogTreeView.setColumnHidden(1, True)
        self.ui.catalogTreeView.setColumnHidden(2, True)
        self.ui.catalogTreeView.setColumnHidden(3, True)

        # регистрация эвентов для кнопок
        # self.ui.startSearchingButton.clicked.connect(self.start_search_hdl_button_click)
        self.ui.startSearchingButton.clicked.connect(self.start_search_hdl_button_click)
        self.ui.generateReportButton.clicked.connect(self.generate_report_button_click)

        self.ui.catalogTreeView.clicked.connect(self.click_on_dir)

    @pyqtSlot()
    def start_search_hdl_button_click(self):
        extension = []  # кортеж с разрешениями файлов
        pattern = self.ui.selectFileExtension.currentText()
        if pattern == "*.v":
            extension = ["*.v"]
        elif pattern == "*.vhd":
            extension = ["*.vhd"]
        elif pattern == "*.v/ *.vhd":
            extension = ["*.v", "*.vhd"]
        self.hdl_files_list = self.tasker.find(self.file_path, extension)
        hdl_list_model = QStandardItemModel()
        for f in self.hdl_files_list:
            item = QStandardItem(f)
            hdl_list_model.appendRow(item)
        self.ui.foundHdlFilesListView.setModel(hdl_list_model)
        self.ui.count_files_label.setText("Found " + str(len(self.hdl_files_list)) + " files")

    @pyqtSlot()
    def generate_report_button_click(self):
        self.tasker.generate_report(self.hdl_files_list)

    def click_on_dir(self, signal):
        self.file_path = self.ui.catalogTreeView.model().filePath(signal)

        self.files = [f for f in os.listdir(self.file_path) if
                      os.path.isfile(os.path.join(self.file_path, f))]  # список файлов в file_path

        list_model = QStandardItemModel()
        # TODO если диск пустой - вылетает
        for f in self.files:
            item = QStandardItem(f)
            list_model.appendRow(item)
        self.ui.currentCatalogFilesList.setModel(list_model)


if __name__ == "__main__":
    import sys

    # pyqt_plugins = os.path.join(os.path.dirname(PyQt5.__file__), "..", "..", "..", "Library", "plugins")
    # QApplication.addLibraryPath(pyqt_plugins)

    app = QtWidgets.QApplication(sys.argv)
    window = ExtractorWindow()
    window.show()
    sys.exit(app.exec_())
