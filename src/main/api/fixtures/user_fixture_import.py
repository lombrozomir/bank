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
