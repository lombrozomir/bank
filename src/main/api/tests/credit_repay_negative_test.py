import pytest


@pytest.mark.api
class TestCreditRepayNegative:
    def test_repay_more_than_debt(self, api_manager, active_credit):
        credit_user_request, credit_user_account, credit = active_credit
        api_manager.user_steps.credit_repay_invalid(credit_user_request, credit.creditId, credit_user_account.id, 999999)


