# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '!MyGui.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 241, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.catalogsTreeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.catalogsTreeView.setGeometry(QtCore.QRect(0, 0, 241, 471))
        self.catalogsTreeView.setObjectName("catalogsTreeView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setGeometry(QtCore.QRect(260, 0, 261, 471))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 259, 469))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.currentCatalogFiles = QtWidgets.QListView(self.scrollAreaWidgetContents_2)
        self.currentCatalogFiles.setGeometry(QtCore.QRect(0, 0, 261, 471))
        self.currentCatalogFiles.setObjectName("currentCatalogFiles")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_3.setGeometry(QtCore.QRect(530, 0, 251, 471))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 249, 469))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.foundHdlFiles = QtWidgets.QListView(self.scrollAreaWidgetContents_3)
        self.foundHdlFiles.setGeometry(QtCore.QRect(0, 0, 256, 471))
        self.foundHdlFiles.setObjectName("foundHdlFiles")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.openCatalogBtn = QtWidgets.QPushButton(self.frame)
        self.openCatalogBtn.setGeometry(QtCore.QRect(90, 490, 75, 23))
        self.openCatalogBtn.setObjectName("openCatalogBtn")
        self.startSearchBtn = QtWidgets.QPushButton(self.frame)
        self.startSearchBtn.setGeometry(QtCore.QRect(390, 490, 111, 23))
        self.startSearchBtn.setObjectName("startSearchBtn")
        self.generateReportBtn = QtWidgets.QPushButton(self.frame)
        self.generateReportBtn.setGeometry(QtCore.QRect(600, 490, 111, 23))
        self.generateReportBtn.setObjectName("generateReportBtn")
        self.selectExtensionComboBox = QtWidgets.QComboBox(self.frame)
        self.selectExtensionComboBox.setGeometry(QtCore.QRect(280, 490, 69, 22))
        self.selectExtensionComboBox.setObjectName("selectExtensionComboBox")
        self.selectExtensionComboBox.addItem("")
        self.selectExtensionComboBox.addItem("")
        self.horizontalLayout.addWidget(self.frame)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
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
        self.openCatalogBtn.setText(_translate("VersionExtractor_by_Alexe1ka", "Open catalog"))
        self.startSearchBtn.setText(_translate("VersionExtractor_by_Alexe1ka", "Search *.hdl files"))
        self.generateReportBtn.setText(_translate("VersionExtractor_by_Alexe1ka", "Generate report"))
        self.selectExtensionComboBox.setItemText(0, _translate("VersionExtractor_by_Alexe1ka", ".vhdl"))
        self.selectExtensionComboBox.setItemText(1, _translate("VersionExtractor_by_Alexe1ka", ".v"))
        self.menuMenu.setTitle(_translate("VersionExtractor_by_Alexe1ka", "Menu"))
        self.menuHelp.setTitle(_translate("VersionExtractor_by_Alexe1ka", "Help"))

    def on_clicked(self):
        print("current item clicked")
