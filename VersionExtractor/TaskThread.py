from PyQt5.QtCore import QThread
import os


class TaskThread(QThread):
    def __init__(self, current_dir):
        QThread.__init__(self)
        self.current_dir = current_dir
        self.files = []

    def run(self):
        self.files = [f for f in os.listdir(self.current_dir) if
                      os.path.isfile(os.path.join(self.current_dir, f))]
        self.sleep(2)
