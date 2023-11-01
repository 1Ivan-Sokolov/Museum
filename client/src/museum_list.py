from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from client.ui.ui_museum_list import Ui_MainWindow as Ui_MainForm
from client.src.base_worker import BaseWorker, Visitor, Login

class MuseumList(QMainWindow, Ui_MainForm):
    def __init__(self, base_worker: BaseWorker, login: Login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.base_worker = base_worker

    def search(self):
        pass

    def get_museum(self):
        pass
