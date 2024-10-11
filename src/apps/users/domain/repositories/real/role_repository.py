from users.data.entities.role_entity import RoleEntity
from users.data.models.models import Role
from users.domain.repositories.role_repository import IRoleRepository


class RoleRepository(IRoleRepository):
    def get_role_by_name(self, role_name: str) -> RoleEntity:
        try:
            role_obj = Role.objects.get(name=role_name)
        except DatabaseError:
            raise Exception
