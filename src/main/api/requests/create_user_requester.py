from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester

class CreateUserRequester(ValidateCrudRequester):

    def __init__(self, request_spec, response_spec):
        super().__init__(request_spec, Endpoint.ADMIN_CREATE_USER, response_spec)
