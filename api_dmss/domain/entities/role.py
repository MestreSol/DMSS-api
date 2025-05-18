from typing import Optional
from uuid import UUID

# ...existing code...
class Role:
    def __init__(self, name: str, role_id: Optional[UUID] = None):
        self.name = name
        self.role_id = role_id