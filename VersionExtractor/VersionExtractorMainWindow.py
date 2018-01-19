# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_compon.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VersionExtractor_by_Alexe1ka(object):
    def setupUi(self, VersionExtractor_by_Alexe1ka):
        VersionExtractor_by_Alexe1ka.setObjectName("VersionExtractor_by_Alexe1ka")
        VersionExtractor_by_Alexe1ka.resize(820, 622)
        self.centralwidget = QtWidgets.QWidget(VersionExtractor_by_Alexe1ka)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftCatalogView = QtWidgets.QVBoxLayout()
        self.leftCatalogView.setObjectName("leftCatalogView")
        self.catalogTreeView = QtWidgets.QTreeView(self.centralwidget)
        self.catalogTreeView.setObjectName("catalogTreeView")
        self.leftCatalogView.addWidget(self.catalogTreeView)
        self.openCatalogButton = QtWidgets.QPushButton(self.centralwidget)
        self.openCatalogButton.setObjectName("openCatalogButton")
        self.leftCatalogView.addWidget(self.openCatalogButton)
        self.horizontalLayout_2.addLayout(self.leftCatalogView)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.currentCatalogFilesList = QtWidgets.QListView(self.centralwidget)
        self.currentCatalogFilesList.setObjectName("currentCatalogFilesList")
        self.verticalLayout_6.addWidget(self.currentCatalogFilesList)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selectFileExtension = QtWidgets.QComboBox(self.centralwidget)
        self.selectFileExtension.setObjectName("selectFileExtension")
        self.selectFileExtension.addItem("")
        self.selectFileExtension.addItem("")
        self.horizontalLayout_3.addWidget(self.selectFileExtension)
        self.startSearchingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startSearchingButton.setObjectName("startSearchingButton")
        self.horizontalLayout_3.addWidget(self.startSearchingButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.foundHdlFilesListView = QtWidgets.QListView(self.centralwidget)
        self.foundHdlFilesListView.setObjectName("foundHdlFilesListView")
        self.verticalLayout_7.addWidget(self.foundHdlFilesListView)
        self.generateReportButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateReportButton.setObjectName("generateReportButton")
        self.verticalLayout_7.addWidget(self.generateReportButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        VersionExtractor_by_Alexe1ka.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VersionExtractor_by_Alexe1ka)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        VersionExtractor_by_Alexe1ka.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VersionExtractor_by_Alexe1ka)
        self.statusbar.setObjectName("statusbar")
        VersionExtractor_by_Alexe1ka.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(VersionExtractor_by_Alexe1ka)
        QtCore.QMetaObject.connectSlotsByName(VersionExtractor_by_Alexe1ka)

    def retranslateUi(self, VersionExtractor_by_Alexe1ka):
        _translate = QtCore.QCoreApplication.translate
        VersionExtractor_by_Alexe1ka.setWindowTitle(_translate("VersionExtractor_by_Alexe1ka", "MainWindow"))
        self.openCatalogButton.setText(_translate("VersionExtractor_by_Alexe1ka", "Open catalog"))
        self.selectFileExtension.setItemText(0, _translate("VersionExtractor_by_Alexe1ka", ".v"))
        self.selectFileExtension.setItemText(1, _translate("VersionExtractor_by_Alexe1ka", ".vhdl"))
        self.startSearchingButton.setText(_translate("VersionExtractor_by_Alexe1ka", "Search hdl files"))
        self.generateReportButton.setText(_translate("VersionExtractor_by_Alexe1ka", "Generate report"))
        self.menuMenu.setTitle(_translate("VersionExtractor_by_Alexe1ka", "Menu"))
        self.menuHelp.setTitle(_translate("VersionExtractor_by_Alexe1ka", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VersionExtractor_by_Alexe1ka = QtWidgets.QMainWindow()
    ui = Ui_VersionExtractor_by_Alexe1ka()
    ui.setupUi(VersionExtractor_by_Alexe1ka)
    VersionExtractor_by_Alexe1ka.show()
    sys.exit(app.exec_())

