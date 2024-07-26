import requests

class Person:
    def __init__(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name
        self.obtive_data = False

    def get_data(self):
        response = requests.get('https://127.0.0.1:8000/api')
        if response.ok:
            self.obtive_data = True
            return 'CONECTED_SUCCESS'
        else: 
            self.obtive_data = False
            return 'False 404'