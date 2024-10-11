from users.data.entities.role_entity import RoleEntity
from users.data.models.models import Role


def map_role(role: Role) -> RoleEntity:
    return RoleEntity(name=role.name, color=role.color)
