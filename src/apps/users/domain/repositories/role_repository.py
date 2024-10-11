import abc
from users.data.entities.role_entity import RoleEntity


class IRoleRepository(abc.ABC):
    @abc.abstractmethod
    def get_role_by_name(self, role_name: str) -> RoleEntity:
        raise NotImplementedError