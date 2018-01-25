from PyQt5.QtCore import QThread


class WorkerThread(QThread):
    def __init__(self) -> None:
        super().__init__(self)

    def run(self) -> None:
        super().run()
