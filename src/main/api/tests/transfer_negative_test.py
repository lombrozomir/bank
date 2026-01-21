import pytest


@pytest.mark.api
class TestTransferNegative:
    def test_transfer_less_than_min(self, api_manager, create_user_request, user_two_accounts):
        a1, a2 = user_two_accounts
        api_manager.user_steps.deposit(create_user_request, account_id=a1.id, amount=2000)
        api_manager.user_steps.transfer_invalid(create_user_request, a1.id, a2.id, 499)

    def test_transfer_greater_than_max(self, api_manager, create_user_request, user_two_accounts):
        a1, a2 = user_two_accounts
        api_manager.user_steps.deposit(create_user_request, account_id=a1.id, amount=9000)
        api_manager.user_steps.transfer_invalid(create_user_request, a1.id, a2.id, 10001)


