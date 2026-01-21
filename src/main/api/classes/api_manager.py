from src.main.api.steps.admin_steps import AdminSteps
from src.main.api.steps.user_steps import UserSteps

class ApiManager:

    def __init__(self):
        self.admin_steps = AdminSteps()
        self.user_steps = UserSteps()

    def admin_ser(self, create_user_request):
        return self.admin_steps.create_user(create_user_request)
