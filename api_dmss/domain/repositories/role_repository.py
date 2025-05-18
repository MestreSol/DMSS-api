from abc import ABC, abstractmethod
from domain.entities.role import Role
from typing import List

class RoleRepository(ABC):
    @abstractmethod
    def save(self, role: Role) -> None:
        ...

    @abstractmethod
    def get_by_id(self, role_id) -> Role:
        ...

    @abstractmethod
    def list_all(self) -> List[Role]:
        ...
