from typing import Optional
import requests
from requests import Response
from src.main.api.foundation.http_requester import HttpRequester
from src.main.api.models.base_model import BaseModel

class CrudRequester(HttpRequester):

    def post(self, model: Optional[BaseModel]) -> Response:
        body = model.model_dump() if model is not None else ''
        base_url = self.request_spec.get('base_url')
        headers = self.request_spec.get('headers', self.request_spec)
        response = requests.post(url=f'{base_url}{self.endpoint.value.url}', headers=headers, json=body)
        if self.response_spec:
            self.response_spec(response)
        return response

    def delete(self, user_id: int) -> Response:
        base_url = self.request_spec.get('base_url')
        headers = self.request_spec.get('headers', self.request_spec)
        response = requests.delete(url=f'{base_url}{self.endpoint.value.url}/{user_id}', headers=headers)
        if self.response_spec:
            self.response_spec(response)
        return response

    def get(self, path_suffix: str='') -> Response:
        base_url = self.request_spec.get('base_url')
        headers = self.request_spec.get('headers', self.request_spec)
        response = requests.get(url=f'{base_url}{self.endpoint.value.url}{path_suffix}', headers=headers)
        if self.response_spec:
            self.response_spec(response)
        return response
