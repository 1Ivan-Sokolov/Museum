import requests

class BaseWorker:
    def __init__(self, server_url: str):
        self.server_url=server_url
        self.end_points = {
            'get_visitor': self.server_url + 'visitor/'
        }


