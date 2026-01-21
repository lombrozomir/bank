from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester

class CreditHistoryRequester(ValidateCrudRequester):

    def __init__(self, request_spec, response_spec):
        super().__init__(request_spec, Endpoint.CREDIT_HISTORY, response_spec)
