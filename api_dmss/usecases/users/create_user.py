from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class CreateUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, username: str, email: str, password: str) -> User:
        # validações, políticas de negócio...
        user = User(username=username, email=email, password=password)
        self.repo.save(user)
        return user
