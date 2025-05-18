from uuid import UUID, uuid4

class Role:
    def __init__(self, name: str, role_id: Optional[UUID] = None):
        self.id = role_id or uuid4()
        self.name = name
