from abc import ABC, abstractmethod
from domain.entities.user import User
from typing import List

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        ...

    @abstractmethod
    def get_by_id(self, user_id) -> User:
        ...

    @abstractmethod
    def list_all(self) -> List[User]:
        ...
