from PyQt5.QtCore import QThread, pyqtSignal
from catalog_parser import HdlWorker


class MyThread(QThread):
    progress = pyqtSignal(int)  # сигнал который мы будем передавать прогрессбару
    hdl_file_list = []
    worker = HdlWorker()
    counter = 0

    def __init__(self, k, hdl_file_list, worker):
        super().__init__()
        self.k = k
        self.hdl_file_list = hdl_file_list
        self.worker = HdlWorker(worker)

    def run(self):
        print("hello,new thread")
        print(self.hdl_file_list)
        self.worker.generate_report(self.hdl_file_list)
        self.progress.emit(100)
        # while self.counter < 100:
        #     self.ui.progressBar.setValue(self.worker.current_counter * 100 / len(self.hdl_files_list))

            # for i in range(self.k * 1001):
            #     sum([i * i for i in range(100000)])
            #     ex = i // (self.k * 10)
            #     self.progress.emit(ex)
