from domain.entities.role import Role
from domain.repositories.role_repository import RoleRepository

class CreateRole:
    def __init__(self, repo: RoleRepository):
        self.repo = repo

    def execute(self, name: str) -> Role:
        role = Role(name=name)
        self.repo.save(role)
        return role
