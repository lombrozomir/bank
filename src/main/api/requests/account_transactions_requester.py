from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester

class AccountTransactionsRequester(ValidateCrudRequester):

    def __init__(self, request_spec, response_spec):
        super().__init__(request_spec, Endpoint.ACCOUNT_TRANSACTIONS, response_spec)

    def get_by_account_id(self, account_id: int):
        return self.get(path_suffix=f'/{account_id}')
