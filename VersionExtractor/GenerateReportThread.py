from PyQt5.QtCore import QThread, pyqtSignal
from catalog_parser import HdlWorker


class ReportThread(QThread):
    progress = pyqtSignal(int)  # сигнал который мы будем передавать прогрессбару
    hdl_file_list = []
    worker = HdlWorker()
    counter = 0

    def __init__(self,  hdl_file_list, worker):
        super().__init__()
        self.hdl_file_list = hdl_file_list
        self.worker = worker

    def run(self):
        # print("worker path in generate report function in new thread: ")
        # print(self.worker.path)
        # print("new thread")
        # print(self.hdl_file_list)
        self.worker.generate_report(self.hdl_file_list)
        self.progress.emit(100)

