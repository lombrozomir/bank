import pytest

@pytest.mark.api
class TestCreditNegative:
    def test_credit_request_forbidden_for_role_user(self, api_manager, create_user_request, user_account):
        api_manager.user_steps.credit_request_forbidden(create_user_request, user_account.id, 5000, 12)

    def test_second_credit_forbidden(self, api_manager, active_credit):
        credit_user_request, credit_user_account, credit = active_credit
        api_manager.user_steps.credit_request_forbidden(credit_user_request, credit_user_account.id, 5000, 12)


