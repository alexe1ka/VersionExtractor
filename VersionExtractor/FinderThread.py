from PyQt5.QtCore import QThread, pyqtSignal
from catalog_parser import HdlWorker


class FinderThread(QThread):
    progress = pyqtSignal(int)  # сигнал который мы будем передавать прогрессбару
    dataReady = pyqtSignal(list)
    worker = HdlWorker()
    file_path = ""
    extension = ""
    hdl_file_list = ""

    def __init__(self, worker, file_path, extension):
        super().__init__()
        self.worker = worker
        self.file_path = file_path
        self.extension = extension

    def run(self):
        self.hdl_file_list = self.worker.find(self.file_path, self.extension)
        self.dataReady.emit(self.hdl_file_list)
        self.progress.emit(100)
