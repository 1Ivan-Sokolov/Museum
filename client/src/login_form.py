import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from client.ui.ui_login_form import Ui_MainWindow as Ui_LoginForm
from client.src.base_worker import BaseWorker, Visitor, Login
from client.src.user_list_form import UserList


class LoginForm(QMainWindow, Ui_LoginForm):

    login_correct = pyqtSignal(int, int)
    main_window: QMainWindow

    def __init__(self, base_worker: BaseWorker):
        super().__init__()
        self.base_worker = base_worker

        self.setupUi(self)
        self.Button_entrer.clicked.connect(self.check_login)
        self.Button_cancel.clicked.connect(self.exit)

    def check_login(self):
        login = self.base_worker.check_login(Visitor(login_email=self.line_login.text(), password=self.line_password.text()))
        # self.start_main_window(login)
        if login:
            self.main_window = UserList(self.base_worker, login)
            self.main_window.show()
            self.close()

    def exit(self):
        self.close()
