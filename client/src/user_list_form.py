from typing import List

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from client.ui.ui_user_list import Ui_MainWindow as Ui_UserList
from client.src.base_worker import BaseWorker, Login, Visitor

ADMIN_ID = 1

class UserList(QMainWindow, Ui_UserList):
    def __init__(self, base_worker: BaseWorker, login: Login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.base_worker = base_worker
        self.load_users()
        self.btn_reset.clicked.connect(self.reset_visitor)
        self.btn_add.clicked.connect(self.add_new_visitor)
        self.btn_delete.clicked.connect(self.delete_visitor)
        self.show()

    def delete_visitor(self):
        pass

    def reset_visitor(self) -> None    :
        self.line_login.setText('')
        self.line_password.setText('')
        # self.cb_post.setCurrentIndex(0)

    def add_new_visitor(self) -> None:
        # if not self.check_user_fields():
        #     return

        visitor = Visitor(login_email=self.line_login.text(), password=self.line_password.text())
        res = self.base_worker.add_visitor(visitor)
        self.load_users()
        print(res)

    def load_users(self):
        row = 0
        self.tw_user_list.setRowCount(0)
        visitors = self.base_worker.get_visitors()
        for visitor in visitors:
            self.tw_user_list.insertRow(row)
            self.tw_user_list.setItem(row, 0, QTableWidgetItem(str(visitor.user_id)))
            self.tw_user_list.setItem(row, 1, QTableWidgetItem(visitor.login_email))
            self.tw_user_list.resizeColumnsToContents()
            self.tw_user_list.horizontalHeader().setStretchLastSection(True)
            row += 1
