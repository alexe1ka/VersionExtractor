import VersionExtractorMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import QThread
import os
import catalog_parser
import json2html
import TaskThread


# pyuic5 input.ui -o output.py


class ExtractorWindow(QMainWindow, QTreeView):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # uic.loadUi("gui.ui", self)
        self.ui = VersionExtractorMainWindow.Ui_version_extractor_by_alexe1ka()  # сгенерированный класс из Designer'a
        self.ui.setupUi(self)

        self.file_path = ""  # текущий каталог
        self.files = []  # список файлов в текущем каталоге
        self.hdl_files_list = []  # список найденных hdl файлов

        model = QFileSystemModel()
        model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)  # в treeView - только каталоги
        # model.setFilter(QtCore.QDir.Files)  # фильтр на "только файлы"
        model.setRootPath(QtCore.QDir.currentPath())
        self.ui.catalogTreeView.setModel(model)

        # скрытие параметров директори
        self.ui.catalogTreeView.setColumnHidden(1, True)
        self.ui.catalogTreeView.setColumnHidden(2, True)
        self.ui.catalogTreeView.setColumnHidden(3, True)

        # регистрация эвентов для кнопок

        self.ui.startSearchingButton.clicked.connect(self.start_search_hdl_button_click)
        self.ui.generateReportButton.clicked.connect(self.generate_report_button_click)

        self.ui.catalogTreeView.clicked.connect(self.click_on_dir)

    @pyqtSlot()
    def start_search_hdl_button_click(self):
        print("start search hdl files")
        pattern = self.ui.selectFileExtension.currentText()
        # TODO паттерн для v AND vhd не работает
        # if str(pattern) == "*.v/ *.vhd":
        #     new_pattern = "*.v*d"
        #     print("pattern for all hdl files: " + new_pattern)
        self.hdl_files_list = catalog_parser.find(pattern, self.file_path)
        hdl_list_model = QStandardItemModel()
        for f in self.hdl_files_list:
            item = QStandardItem(f)
            hdl_list_model.appendRow(item)
        self.ui.foundHdlFilesListView.setModel(hdl_list_model)

    @pyqtSlot()
    def generate_report_button_click(self):
        report_data = []
        for file in self.hdl_files_list:
            report_data.append(catalog_parser.file_parser(file))
        catalog_parser.generate_report(json2html.json2html.convert(report_data))
        print(report_data)

    def click_on_dir(self, signal):
        self.file_path = self.ui.catalogTreeView.model().filePath(signal)

        self.files = [f for f in os.listdir(self.file_path) if os.path.isfile(os.path.join(self.file_path, f))]  # список файлов в file_path

        list_model = QStandardItemModel()
        # TODO если диск пустой - вылетает
        for f in self.files:
            item = QStandardItem(f)
            list_model.appendRow(item)
        self.ui.currentCatalogFilesList.setModel(list_model)


if __name__ == "__main__":
    import sys
    import PyQt5

    # pyqt_plugins = os.path.join(os.path.dirname(PyQt5.__file__), "..", "..", "..", "Library", "plugins")
    # QApplication.addLibraryPath(pyqt_plugins)

    app = QtWidgets.QApplication(sys.argv)
    window = ExtractorWindow()
    window.show()
    sys.exit(app.exec_())
