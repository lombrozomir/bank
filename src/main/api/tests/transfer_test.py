import pytest

@pytest.mark.api
class TestTransfer:

    def test_transfer_between_own_accounts(self, api_manager, create_user_request, user_two_accounts):
        a1, a2 = user_two_accounts
        api_manager.user_steps.deposit(create_user_request, account_id=a1.id, amount=2000)
        api_manager.user_steps.transfer(create_user_request, from_account_id=a1.id, to_account_id=a2.id, amount=500)
        trx1 = api_manager.user_steps.transactions(create_user_request, account_id=a1.id)
        trx2 = api_manager.user_steps.transactions(create_user_request, account_id=a2.id)
        assert trx1.balance is not None and trx2.balance is not None
        assert trx1.balance <= 1500
        assert trx2.balance >= 500
