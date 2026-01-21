import pytest

from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.credit_request import CreditRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.responce_spec import ResponseSpecs


@pytest.mark.api
class TestCreditNegative:
    def test_credit_request_forbidden_for_role_user(self, api_manager, create_user_request, user_account):
        req = CreditRequest(accountId=user_account.id, amount=5000, termMonths=12)
        ValidateCrudRequester(
            RequestSpecs.auth_headers(create_user_request.username, create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_forbidden(),
        ).post(req)

    def test_second_credit_forbidden(self, api_manager, active_credit):
        credit_user_request, credit_user_account, credit = active_credit
        req = CreditRequest(accountId=credit_user_account.id, amount=5000, termMonths=12)
        ValidateCrudRequester(
            RequestSpecs.auth_headers(credit_user_request.username, credit_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_forbidden(),
        ).post(req)


