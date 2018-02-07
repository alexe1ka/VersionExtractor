from PyQt5.QtCore import QThread, pyqtSignal
from catalog_parser import HdlTasker


class MyThread(QThread):
    progress = pyqtSignal(int)  # сигнал который мы будем передавать прогрессбару

    def __init__(self, k, hdl_file_list):
        super().__init__()
        self.k = k
        self.hdl_file_list = hdl_file_list
        self.tasker = HdlTasker()

    def run(self):
        print(self.hdl_file_list)
        self.tasker.generate_report(self.hdl_files_list)
        # for i in range(self.k * 1001):
        #     sum([i * i for i in range(100000)])
        #     ex = i // (self.k * 10)
        #     self.progress.emit(ex)
