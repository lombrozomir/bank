import pytest

@pytest.mark.api
class TestTransfer:

    def test_transfer_between_own_accounts(self, transfer_between_own_accounts):
        trx1, trx2 = transfer_between_own_accounts
        assert trx1.balance is not None and trx2.balance is not None
        assert trx1.balance <= 1500
        assert trx2.balance >= 500
