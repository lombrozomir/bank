from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_responce import CreateUserResponse
from src.main.api.requests.login_user_requester import LoginUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.responce_spec import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps

class AdminSteps(BaseSteps):

    def login_user(self, login_user_request):
        return LoginUserRequester(request_spec=RequestSpecs.request_spec(), response_spec=ResponseSpecs.request_ok()).post(login_user_request)

    def create_user(self, create_user_request: CreateUserRequest):
        created = ValidateCrudRequester(RequestSpecs.auth_headers(username='admin', password='123456'), Endpoint.ADMIN_CREATE_USER, ResponseSpecs.request_ok()).post(create_user_request)
        self.created_obj.append(created)
        return created

    def create_invalid_user(self, create_user_request: CreateUserRequest):
        return ValidateCrudRequester(RequestSpecs.auth_headers(username='admin', password='123456'), Endpoint.ADMIN_CREATE_USER, ResponseSpecs.request_bad()).post(create_user_request)

    def delete_user(self, user_id: int):
        return CrudRequester(RequestSpecs.auth_headers(username='admin', password='123456'), Endpoint.ADMIN_DELETE_USER, ResponseSpecs.request_ok()).delete(user_id)
