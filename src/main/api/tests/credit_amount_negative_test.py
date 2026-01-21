import pytest


@pytest.mark.api
class TestCreditAmountNegative:
    def test_credit_amount_greater_than_max(self, api_manager, credit_user_request, credit_user_account):
        api_manager.user_steps.credit_request_invalid(credit_user_request, credit_user_account.id, 15001, 12)


