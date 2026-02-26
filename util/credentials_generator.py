import random

from datetime import datetime #выбрана библиотека дата+время для исключения повторений в поле электронная почта и пароль
from util.constants import Domains

class Credentials:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class CredentialsGenerator:
    @staticmethod
    def generate():
        index = int(random.random() * 10)
        number = int(datetime.now().timestamp())
        name = f'arina{number}'
        email = name + Domains.DOMAINS[index]
        password = number
        return Credentials(name, email, password)
