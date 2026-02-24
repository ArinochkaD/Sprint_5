import random

from datetime import datetime #выбрана библиотека дата+время для исключения повторений в поле электронная почта и пароль
from util.constants import DOMAINS

class Credentials:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

def generate_credentials():
    index = int(random.random() * 10)
    number = int(datetime.now().timestamp())
    name = f'arina{number}'
    email = name + DOMAINS[index]
    password = number
    return Credentials(name, email, password)
