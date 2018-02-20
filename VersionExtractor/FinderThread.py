from PyQt5.QtCore import QThread, pyqtSignal
from catalog_parser import HdlWorker


class FinderThread(QThread):
    progress = pyqtSignal(int)  # сигнал который мы будем передавать прогрессбару
    worker = HdlWorker()
    counter = 0

    def __init__(self,  hdl_file_list, worker):
        super().__init__()
        self.worker = worker

    def run(self):

        self.progress.emit(100)