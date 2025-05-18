from typing import List, Optional
from api_dmss.core.domain.entities.user import User

class UserRepository:
    def __init__(self):
        self._users: List[User] = []

    def add(self, user: User) -> None:
        self._users.append(user)

    def get_by_id(self, user_id: str) -> Optional[User]:
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def get_all(self) -> List[User]:
        return list(self._users)

    def remove(self, user_id: str) -> bool:
        for i, user in enumerate(self._users):
            if user.id == user_id:
                del self._users[i]
                return True
        return False
