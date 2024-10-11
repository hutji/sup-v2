from users.data.repositories.real.role_repository import RoleRepository
from users.domain.interactors.role_interactor import RoleInteractor


def get_role_repository():
    return RoleRepository


def get_role_interactor(role_name: str):
    return RoleInteractor(role_name=role_name, role_repository=get_role_repository())
