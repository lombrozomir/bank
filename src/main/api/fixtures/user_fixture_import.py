import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest

@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def credit_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    user_request.role = 'ROLE_CREDIT_SECRET'
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def user_account(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)

@pytest.fixture
def user_two_accounts(api_manager, create_user_request):
    a1 = api_manager.user_steps.create_account(create_user_request)
    a2 = api_manager.user_steps.create_account(create_user_request)
    return (a1, a2)

@pytest.fixture
def credit_user_account(api_manager, credit_user_request):
    return api_manager.user_steps.create_account(credit_user_request)


@pytest.fixture
def active_credit(api_manager, credit_user_request, credit_user_account):
    credit = api_manager.user_steps.credit_request(credit_user_request, credit_user_account.id, 5000, 12)
    return (credit_user_request, credit_user_account, credit)


@pytest.fixture
def transfer_between_own_accounts(api_manager, create_user_request, user_two_accounts):
    a1, a2 = user_two_accounts
    api_manager.user_steps.deposit(create_user_request, account_id=a1.id, amount=2000)
    api_manager.user_steps.transfer(create_user_request, from_account_id=a1.id, to_account_id=a2.id, amount=500)
    trx1 = api_manager.user_steps.transactions(create_user_request, account_id=a1.id)
    trx2 = api_manager.user_steps.transactions(create_user_request, account_id=a2.id)
    return (trx1, trx2)
