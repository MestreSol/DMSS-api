from domain.repositories.user_repository import UserRepository
from domain.repositories.role_repository import RoleRepository

class AssignRole:
    def __init__(
        self,
        user_repo: UserRepository,
        role_repo: RoleRepository
    ):
        self.user_repo = user_repo
        self.role_repo = role_repo

    def execute(self, user_id, role_id):
        user = self.user_repo.get_by_id(user_id)
        role = self.role_repo.get_by_id(role_id)
        user.role_id = role.id
        self.user_repo.save(user)
        return user
