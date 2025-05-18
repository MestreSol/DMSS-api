from domain.entities.role import Role
from domain.repositories.role_repository import RoleRepository
from api_dmss.adapters.persistence.models.role_model import RoleModel

class DjangoORMRoleRepository(RoleRepository):
    def save(self, role: Role) -> None:
        RoleModel.objects.update_or_create(
            id=role.id,
            defaults={"name": role.name}
        )

    def get_by_id(self, role_id) -> Role:
        o = RoleModel.objects.get(id=role_id)
        return Role(name=o.name, role_id=o.id)

    def list_all(self):
        return [
            Role(name=o.name, role_id=o.id)
            for o in RoleModel.objects.all()
        ]
