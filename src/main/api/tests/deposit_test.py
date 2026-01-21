import pytest

@pytest.mark.api
class TestDeposit:

    def test_deposit(self, api_manager, create_user_request, user_account):
        api_manager.user_steps.deposit(create_user_request, account_id=user_account.id, amount=1000)
        trx = api_manager.user_steps.transactions(create_user_request, account_id=user_account.id)
        assert trx.balance is not None
        assert trx.balance >= 1000
