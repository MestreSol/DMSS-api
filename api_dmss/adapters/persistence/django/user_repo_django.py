from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from adapters.persistence.models.user_model import UserModel

class DjangoORMUserRepository(UserRepository):
    def save(self, user: User) -> None:
        UserModel.objects.update_or_create(
            id=user.id,
            defaults={
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "role_id": user.role_id,
            }
        )

    def get_by_id(self, user_id) -> User:
        o = UserModel.objects.get(id=user_id)
        return User(
            username=o.username,
            email=o.email,
            role_id=o.role_id,
            user_id=o.id
        )

    def list_all(self):
        return [
            User(
                username=o.username,
                email=o.email,
                role_id=o.role_id,
                user_id=o.id
            )
            for o in UserModel.objects.all()
        ]
