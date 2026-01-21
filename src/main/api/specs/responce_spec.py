from http import HTTPStatus
from requests import Response

class ResponseSpecs:

    @staticmethod
    def request_ok():

        def confirm(response: Response):
            assert response.status_code == HTTPStatus.OK, response.text
            return response
        return confirm

    @staticmethod
    def request_created():

        def confirm(response: Response):
            assert response.status_code == HTTPStatus.CREATED, response.text
            return response
        return confirm

    @staticmethod
    def request_bad():

        def confirm(response: Response):
            assert response.status_code == HTTPStatus.BAD_REQUEST, response.text
            return response
        return confirm

    @staticmethod
    def request_forbidden():

        def confirm(response: Response):
            assert response.status_code in (HTTPStatus.FORBIDDEN, HTTPStatus.NOT_FOUND), response.text
            return response
        return confirm

    @staticmethod
    def request_conflict():

        def confirm(response: Response):
            assert response.status_code == HTTPStatus.CONFLICT, response.text
            return response
        return confirm

    @staticmethod
    def request_unprocessable():

        def confirm(response: Response):
            assert response.status_code in (HTTPStatus.UNPROCESSABLE_ENTITY, HTTPStatus.BAD_REQUEST), response.text
            return response
        return confirm
