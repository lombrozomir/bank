from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester

class CreateAccountRequester(ValidateCrudRequester):

    def __init__(self, request_spec, response_spec):
        super().__init__(request_spec, Endpoint.ACCOUNT_CREATE, response_spec)
