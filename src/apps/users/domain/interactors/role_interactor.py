from dataclasses import asdict

from src.apps.users.domain.repositories.role_repository import IRoleRepository


class RoleInteractor:
    def __init__(self, role_name: str, role_repository: IRoleRepository):
        self.role_name = role_name
        self._role_repository = role_repository

    def get_role_by_name(self):
        return asdict(self._role_repository.get_role_by_name(self.role_name))
