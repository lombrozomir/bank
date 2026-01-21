import pytest

@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(self, api_manager, active_credit):
        credit_user_request, credit_user_account, credit = active_credit
        assert credit.creditId is not None
        api_manager.user_steps.deposit(credit_user_request, account_id=credit_user_account.id, amount=5000)
        repay = api_manager.user_steps.credit_repay(credit_user_request, credit_id=credit.creditId, account_id=credit_user_account.id, amount=5000)
        assert repay.creditId == credit.creditId
        assert repay.amountDeposited == 5000
