# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.db import models

# from apps.users.managers import CustomUserManager
# from validators.validators import (
#     ColorValidator,
#     CustomValidator,
#     LettersAndSymbolsValidator,
#     LettersOnlyValidator,
# )


class Role(models.Model):
    """Модель роли пользователя."""

    name = models.CharField(
        max_length=20,
        # validators=[LettersOnlyValidator.get_regex_validator()],
        verbose_name="Название",
        help_text="Введите название роли до 20 символов(допускаются только буквы кириллицы и латиницы.)",
    )
    color = models.CharField(
        max_length=6,
        # validators=[ColorValidator.get_regex_validator()],
        verbose_name="Цвет",
        help_text="Введите цвет в формате 6 цифр.",
    )

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Permissions(models.Model):
    """Модель прав пользователя."""

    name = models.CharField(
        max_length=20,
        # validators=[LettersOnlyValidator.get_regex_validator()],
        verbose_name="Название",
    )
    code = models.IntegerField(verbose_name="Код")
    description = models.TextField(
        max_length=500, null=True, blank=True, verbose_name="Описание"
    )

    class Meta:
        verbose_name = "право"
        verbose_name_plural = "права"
        ordering = ["-id"]

    def __str__(self):
        return self.name
