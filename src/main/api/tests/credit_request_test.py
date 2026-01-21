import pytest

@pytest.mark.api
class TestCreditRequest:

    def test_credit_request(self, api_manager, credit_user_request, credit_user_account):
        resp = api_manager.user_steps.credit_request(credit_user_request, account_id=credit_user_account.id, amount=5000, term_months=12)
        assert resp.creditId is not None
        assert resp.amount == 5000
