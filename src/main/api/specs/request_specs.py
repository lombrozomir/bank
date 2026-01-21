import requests
from src.main.api.configs.config import Config

class RequestSpecs:

    @staticmethod
    def base_headers():
        return {'Content-Type': 'application/json', 'accept': 'application/json'}

    @staticmethod
    def request_spec():
        return {'base_url': Config.fetch('backendUrl'), 'headers': RequestSpecs.base_headers()}

    @staticmethod
    def auth_headers(username: str, password: str):
        login_admin_response = requests.post(url=f"{Config.fetch('backendUrl')}/auth/token/login", json={'username': username, 'password': password}, headers=RequestSpecs.base_headers())
        assert login_admin_response.status_code == 200, login_admin_response.text
        token = login_admin_response.json().get('token')
        assert token, f'No token in response: {login_admin_response.json()}'
        return {'base_url': Config.fetch('backendUrl'), 'headers': {**RequestSpecs.base_headers(), 'Authorization': f'Bearer {token}'}}
__all__ = ['RequestSpecs']
