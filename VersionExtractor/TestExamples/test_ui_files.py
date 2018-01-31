# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QProgressBar, QApplication
# from PyQt5.QtCore import QThread, pyqtSignal
# import sys
# # наш класс потока, в котором мы переопределим ф-йиб run , чтобы она выполняла полезную работу
# class MyThread(QThread):
#     progress = pyqtSignal(int) # сигнал который мы будем передавать прогрессбару
#     def __init__(self,k):
#         super().__init__()
#         self.k = k
#     def run(self): # наша функция(полезная работа), без всяких if pbNumber == 1:
#           for i in range(self.k * 1001):
#             sum([i * i for i in range(5000)])
#             ex = i // (self.k * 10)
#             self.progress.emit(ex)  # "Испускаем" сигнал и передаем в нем текщее значение прогесса
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.firstProgressBar = QProgressBar(self)
#         self.firstProgressBar.setGeometry(25, 25, 400, 40)
#         self.firstStep = 0
#         self.secondProgressBar = QProgressBar(self)
#         self.secondProgressBar.setGeometry(25, 100, 400, 40)
#         self.secondStep = 0
#         self.button = QPushButton("Start", self)
#         self.button.setGeometry(420, 25, 160, 40)
#         self.button.clicked.connect(self.action)
#         self.setGeometry(300, 300, 600, 165)
#     def action(self):
#         self.thread1 = MyThread(1)  # создаем первый поток
#         self.thread1.progress.connect(self.setFirstPbar)  #соединяем сигнал progress первого пока с ф-цией setFirstPbar
#         # вобще можно сразу писать
#         # self.thread1.progressed.connect(self.firstProgressBar.setValue)
#         # если вам кроме изменения прогресбара ничего больше не надо
#         self.thread2 = MyThread(2) #все тоже самое для второго
#         self.thread2.progress.connect(self.setSecondPbar)
#         self.thread1.start()
#         self.thread2.start()
#     def setFirstPbar(self, value):
#         self.firstStep = value     # делаем какиенить действия
#         self.firstProgressBar.setValue(value)  #устанавливаем значение прогрессбара1
#     def setSecondPbar(self, value):  # все тоже самоме для второго пргрессбара
#         self.secondStep = value
#         self.secondProgressBar.setValue(value)
# if __name__ == '__main__':
#     Application = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(Application.exec())
#




import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)

        extractAction = QtWidgets.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QtWidgets.QCheckBox('Shrink Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtWidgets.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        self.show()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()