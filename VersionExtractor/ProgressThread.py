from PyQt5.QtCore import QThread, pyqtSignal


class MyThread(QThread):
    progress = pyqtSignal(int)  # сигнал который мы будем передавать прогрессбару

    def __init__(self, k):
        super().__init__()
        self.k = k

    def run(self):
        self.tasker.generate_report(self.hdl_files_list)
        for i in range(self.k * 1001):
            sum([i * i for i in range(5000)])
            ex = i // (self.k * 10)
            self.progress.emit(ex)
