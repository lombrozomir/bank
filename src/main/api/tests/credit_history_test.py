import pytest

@pytest.mark.api
class TestCreditHistory:
    def test_credit_history_contains_active_credit(self, api_manager, active_credit):
        credit_user_request, credit_user_account, credit = active_credit
        history = api_manager.user_steps.credit_history(credit_user_request)
        assert history.credits is not None
        assert any((c.creditId == credit.creditId) for c in history.credits)

