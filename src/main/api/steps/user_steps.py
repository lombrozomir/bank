import allure
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.account_deposit_request import DepositRequest
from src.main.api.models.account_transfer_request import TransferRequest
from src.main.api.models.credit_history_response import CreditHistoryResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.models.create_account_responce import CreateAccountResponse
from src.main.api.models.account_transactions_response import AccountTransactionsResponse
from src.main.api.requests.account_transactions_requester import AccountTransactionsRequester
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.credit_history_requester import CreditHistoryRequester
from src.main.api.requests.credit_repay_requester import CreditRepayRequester
from src.main.api.requests.credit_request_requester import CreditRequestRequester
from src.main.api.requests.deposit_requester import DepositRequester
from src.main.api.requests.transfer_requester import TransferRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.responce_spec import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps

class UserSteps(BaseSteps):

    @allure.step('Create account')
    def create_account(self, create_user_request):
        return CreateAccountRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_created()).post(None)

    @allure.step('Deposit')
    def deposit(self, create_user_request, account_id: int, amount: float):
        req = DepositRequest(accountId=account_id, amount=amount)
        return DepositRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_ok()).post(req)

    @allure.step('Deposit invalid')
    def deposit_invalid(self, create_user_request, account_id: int, amount: float):
        req = DepositRequest(accountId=account_id, amount=amount)
        return ValidateCrudRequester(RequestSpecs.auth_headers(create_user_request.username, create_user_request.password), Endpoint.ACCOUNT_DEPOSIT, ResponseSpecs.request_unprocessable()).post(req)

    @allure.step('Transfer')
    def transfer(self, create_user_request, from_account_id: int, to_account_id: int, amount: float):
        req = TransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=amount)
        return TransferRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_ok()).post(req)

    @allure.step('Transfer invalid')
    def transfer_invalid(self, create_user_request, from_account_id: int, to_account_id: int, amount: float):
        req = TransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=amount)
        return ValidateCrudRequester(RequestSpecs.auth_headers(create_user_request.username, create_user_request.password), Endpoint.ACCOUNT_TRANSFER, ResponseSpecs.request_unprocessable()).post(req)

    @allure.step('Get transactions')
    def transactions(self, create_user_request, account_id: int) -> AccountTransactionsResponse:
        return AccountTransactionsRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_ok()).get_by_account_id(account_id)

    @allure.step('Credit request')
    def credit_request(self, create_user_request, account_id: int, amount: float, term_months: int) -> CreditRequestResponse:
        req = CreditRequest(accountId=account_id, amount=amount, termMonths=term_months)
        return CreditRequestRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_created()).post(req)

    @allure.step('Credit request forbidden')
    def credit_request_forbidden(self, create_user_request, account_id: int, amount: float, term_months: int):
        req = CreditRequest(accountId=account_id, amount=amount, termMonths=term_months)
        return ValidateCrudRequester(RequestSpecs.auth_headers(create_user_request.username, create_user_request.password), Endpoint.CREDIT_REQUEST, ResponseSpecs.request_forbidden()).post(req)

    @allure.step('Credit request invalid')
    def credit_request_invalid(self, create_user_request, account_id: int, amount: float, term_months: int):
        req = CreditRequest(accountId=account_id, amount=amount, termMonths=term_months)
        return ValidateCrudRequester(RequestSpecs.auth_headers(create_user_request.username, create_user_request.password), Endpoint.CREDIT_REQUEST, ResponseSpecs.request_unprocessable()).post(req)

    @allure.step('Credit repay')
    def credit_repay(self, create_user_request, credit_id: int, account_id: int, amount: float) -> CreditRepayResponse:
        req = CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=amount)
        return CreditRepayRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_ok()).post(req)

    @allure.step('Credit repay invalid')
    def credit_repay_invalid(self, create_user_request, credit_id: int, account_id: int, amount: float):
        req = CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=amount)
        return ValidateCrudRequester(RequestSpecs.auth_headers(create_user_request.username, create_user_request.password), Endpoint.CREDIT_REPAY, ResponseSpecs.request_unprocessable()).post(req)

    @allure.step('Credit history')
    def credit_history(self, create_user_request) -> CreditHistoryResponse:
        return CreditHistoryRequester(request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password), response_spec=ResponseSpecs.request_ok()).get()
