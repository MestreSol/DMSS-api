from uuid import UUID, uuid4
from typing import Optional

class User:
    def __init__(
        self,
        username: str,
        email: str,
        role_id: Optional[UUID] = None,
        user_id: Optional[UUID] = None
    ):
        self.id = user_id or uuid4()
        self.username = username
        self.email = email
        self.role_id = role_id
