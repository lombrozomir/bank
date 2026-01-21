from dataclasses import dataclass
from enum import Enum
from typing import Type
from src.main.api.models.base_model import BaseModel
from src.main.api.models.account_transactions_response import AccountTransactionsResponse
from src.main.api.models.create_account_responce import CreateAccountResponse
from src.main.api.models.create_user_responce import CreateUserResponse
from src.main.api.models.credit_history_response import CreditHistoryResponse
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.models.login_user_responce import LoginUserResponse

@dataclass(frozen=True)
class EndpointData:
    url: str
    response_model: Type[BaseModel]

class Endpoint(Enum):
    AUTH_LOGIN = EndpointData('/auth/token/login', LoginUserResponse)
    ADMIN_CREATE_USER = EndpointData('/admin/create', CreateUserResponse)
    ADMIN_DELETE_USER = EndpointData('/admin/users', BaseModel)
    ACCOUNT_CREATE = EndpointData('/account/create', CreateAccountResponse)
    ACCOUNT_DEPOSIT = EndpointData('/account/deposit', BaseModel)
    ACCOUNT_TRANSFER = EndpointData('/account/transfer', BaseModel)
    ACCOUNT_TRANSACTIONS = EndpointData('/account/transactions', AccountTransactionsResponse)
    CREDIT_REQUEST = EndpointData('/credit/request', CreditRequestResponse)
    CREDIT_REPAY = EndpointData('/credit/repay', CreditRepayResponse)
    CREDIT_HISTORY = EndpointData('/credit/history', CreditHistoryResponse)
