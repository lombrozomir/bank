import pytest


@pytest.mark.api
class TestDepositNegative:
    def test_deposit_less_than_min(self, api_manager, create_user_request, user_account):
        api_manager.user_steps.deposit_invalid(create_user_request, user_account.id, 999)

    def test_deposit_greater_than_max(self, api_manager, create_user_request, user_account):
        api_manager.user_steps.deposit_invalid(create_user_request, user_account.id, 9001)


