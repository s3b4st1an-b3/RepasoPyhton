"""Funciones de validacion para los datos del sistema."""

from __future__ import annotations

import re


EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def validate_id(user_id: str, existing_ids: set[int]) -> int:
    """Valida que el ID sea numerico y no exista."""
    try:
        value = int(user_id)
    except ValueError as error:
        raise ValueError("El id debe ser un numero entero.") from error

    if value <= 0:
        raise ValueError("El id debe ser mayor que cero.")

    if value in existing_ids:
        raise ValueError("El id ya existe.")

    return value


def validate_name(name: str) -> str:
    """Valida que el nombre tenga contenido."""
    clean_name = name.strip()
    if len(clean_name) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres.")
    return clean_name.title()


def validate_email(email: str) -> str:
    """Valida el formato basico del email."""
    clean_email = email.strip().lower()
    if not re.match(EMAIL_PATTERN, clean_email):
        raise ValueError("El email no tiene un formato valido.")
    return clean_email