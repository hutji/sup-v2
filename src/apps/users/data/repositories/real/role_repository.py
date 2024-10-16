from users.domain.entities.role_entity import RoleEntity
from users.data.mappers import map_role
from users.data.models.models import Role
from src.apps.users.domain.repositories.role_repository import IRoleRepository


class RoleRepository(IRoleRepository):
    def get_role_by_name(self, role_name: str) -> RoleEntity:
        try:
            role_obj = Role.objects.get(name=role_name)
            return RoleEntity.from_model(role_obj)
        except Role.DoesNotExist:
            raise ValueError
        
        #role_entity = map_role(role_obj) if role_obj else None:
        #return role_entity