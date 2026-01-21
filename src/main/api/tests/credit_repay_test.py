import pytest

@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(self, api_manager, credit_user_request, credit_user_account):
        credit = api_manager.user_steps.credit_request(credit_user_request, account_id=credit_user_account.id, amount=5000, term_months=12)
        assert credit.creditId is not None
        api_manager.user_steps.deposit(credit_user_request, account_id=credit_user_account.id, amount=5000)
        repay = api_manager.user_steps.credit_repay(credit_user_request, credit_id=credit.creditId, account_id=credit_user_account.id, amount=5000)
        assert repay.creditId == credit.creditId
        assert repay.amountDeposited == 5000
