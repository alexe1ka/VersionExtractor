# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_compon.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_version_extractor_by_alexe1ka(object):
    def setupUi(self, version_extractor_by_alexe1ka):
        version_extractor_by_alexe1ka.setObjectName("version_extractor_by_alexe1ka")
        version_extractor_by_alexe1ka.resize(820, 601)
        version_extractor_by_alexe1ka.setMinimumSize(QtCore.QSize(820, 601))
        self.central_widget = QtWidgets.QWidget(version_extractor_by_alexe1ka)
        self.central_widget.setMinimumSize(QtCore.QSize(820, 581))
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftCatalogLayout = QtWidgets.QVBoxLayout()
        self.leftCatalogLayout.setObjectName("leftCatalogLayout")
        self.catalogTreeView = QtWidgets.QTreeView(self.central_widget)
        self.catalogTreeView.setObjectName("catalogTreeView")
        self.leftCatalogLayout.addWidget(self.catalogTreeView)
        self.progressBar = QtWidgets.QProgressBar(self.central_widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.leftCatalogLayout.addWidget(self.progressBar)
        self.count_files_label = QtWidgets.QLabel(self.central_widget)
        self.count_files_label.setText("")
        self.count_files_label.setObjectName("count_files_label")
        self.leftCatalogLayout.addWidget(self.count_files_label)
        self.horizontalLayout_2.addLayout(self.leftCatalogLayout)
        self.central_catalog_files_layout = QtWidgets.QVBoxLayout()
        self.central_catalog_files_layout.setObjectName("central_catalog_files_layout")
        self.currentCatalogFilesList = QtWidgets.QListView(self.central_widget)
        self.currentCatalogFilesList.setObjectName("currentCatalogFilesList")
        self.central_catalog_files_layout.addWidget(self.currentCatalogFilesList)
        self.central_button_layout = QtWidgets.QHBoxLayout()
        self.central_button_layout.setObjectName("central_button_layout")
        self.selectFileExtension = QtWidgets.QComboBox(self.central_widget)
        self.selectFileExtension.setObjectName("selectFileExtension")
        self.selectFileExtension.addItem("")
        self.selectFileExtension.addItem("")
        self.selectFileExtension.addItem("")
        self.central_button_layout.addWidget(self.selectFileExtension)
        self.startSearchingButton = QtWidgets.QPushButton(self.central_widget)
        self.startSearchingButton.setObjectName("startSearchingButton")
        self.central_button_layout.addWidget(self.startSearchingButton)
        self.central_catalog_files_layout.addLayout(self.central_button_layout)
        self.horizontalLayout_2.addLayout(self.central_catalog_files_layout)
        self.right_result_layoyt = QtWidgets.QVBoxLayout()
        self.right_result_layoyt.setObjectName("right_result_layoyt")
        self.foundHdlFilesListView = QtWidgets.QListView(self.central_widget)
        self.foundHdlFilesListView.setObjectName("foundHdlFilesListView")
        self.right_result_layoyt.addWidget(self.foundHdlFilesListView)
        self.generateReportButton = QtWidgets.QPushButton(self.central_widget)
        self.generateReportButton.setObjectName("generateReportButton")
        self.right_result_layoyt.addWidget(self.generateReportButton)
        self.horizontalLayout_2.addLayout(self.right_result_layoyt)
        version_extractor_by_alexe1ka.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(version_extractor_by_alexe1ka)
        self.statusbar.setObjectName("statusbar")
        version_extractor_by_alexe1ka.setStatusBar(self.statusbar)

        self.retranslateUi(version_extractor_by_alexe1ka)
        QtCore.QMetaObject.connectSlotsByName(version_extractor_by_alexe1ka)

    def retranslateUi(self, version_extractor_by_alexe1ka):
        _translate = QtCore.QCoreApplication.translate
        version_extractor_by_alexe1ka.setWindowTitle(_translate("version_extractor_by_alexe1ka", "VersionExtractor"))
        self.selectFileExtension.setItemText(0, _translate("version_extractor_by_alexe1ka", "*.v"))
        self.selectFileExtension.setItemText(1, _translate("version_extractor_by_alexe1ka", "*.vhd"))
        self.selectFileExtension.setItemText(2, _translate("version_extractor_by_alexe1ka", "*.v/ *.vhd"))
        self.startSearchingButton.setText(_translate("version_extractor_by_alexe1ka", "Search hdl files"))
        self.generateReportButton.setText(_translate("version_extractor_by_alexe1ka", "Generate report"))

