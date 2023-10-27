import requests


class Login:
    def __init__(self, visitor_id: int):
        self.visitor_id = visitor_id


class Visitor:
    def __init__(self, login_email, password, id=None, name=None,surname=None, contacts=None):
        self.id= id
        self.name = name
        self.surname = surname
        self.password = password
        self.login_email = login_email
        self.contacts = contacts


class BaseWorker:
    def __init__(self, server_url: str):
        self.server_url=server_url # http://127.0.0.1:8000
        self.end_points = {
            'check_login': self.server_url + '/visitor/check/', # '127.0.0.1:8000/visitor/check/'
            'add_visitor': self.server_url + '/visitor/',
            'delete_visitor': self.server_url + '/visitor/',
            'get_visitor': self.server_url + '/visitor/',
            'get_visitors':self.server_url + '/visitor/'
        }

    def check_login(self, visitor: "VisitorInput"):
        response = requests.get(self.end_points.get('check_login'), data=visitor.json())
        print(response.text)
        return Login(response.json())

    def add_visitor(self, visitor: "VisitorInput"):
        response = requests.post(self.end_points.get('add_visitor'), data=visitor.json())
        print(response.text)
        return response.json()

    def get_visitor(self, visitor_id):
        response = requests.get(url=self.end_points.get('get_visitor')+f'{visitor_id}')
        print(response.text)
        json = response.json()
        return Visitor(login_email=json['email'], password=json['password'])

    def get_visitors(self):
        response = requests.get(url=self.end_points.get('get_visitors'))
        print(response.text)
        json = response.json()
        return [Visitor(login_email=visitor['email'], password=visitor['password'])
                for visitor in json]

    def delete_visitor(self, visitor_id: int):
        response = requests.delete(url=self.end_points.get('delete_visitor') + f'{visitor_id}')
        return response.json()


if __name__ == "__main__":
    base_worker = BaseWorker('http://127.0.0.1:8000')
    lst = base_worker.get_visitors()
    print(lst)
