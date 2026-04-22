"""Logica de negocio para el sistema CRUD."""

from __future__ import annotations

from typing import Any

from file import load_records, save_records
from validate import validate_email, validate_id, validate_name


def build_user(**kwargs: Any) -> dict[str, Any]:
    """Construye un usuario usando kwargs para demostrar flexibilidad."""
    return {
        "id": kwargs["id"],
        "nombre": kwargs["nombre"],
        "email": kwargs["email"],
    }


def get_all_users() -> list[dict[str, Any]]:
    """Obtiene todos los usuarios ordenados por id."""
    records = load_records()
    return sorted(records, key=lambda user: user["id"])


def create_user(user_id: str, name: str, email: str) -> dict[str, Any]:
    """Crea un nuevo usuario validando sus datos."""
    records = load_records()
    existing_ids = {user["id"] for user in records}
    existing_emails = {user["email"] for user in records}

    valid_id = validate_id(user_id, existing_ids)
    valid_name = validate_name(name)
    valid_email = validate_email(email)

    if valid_email in existing_emails:
        raise ValueError("El email ya existe.")

    user = build_user(id=valid_id, nombre=valid_name, email=valid_email)
    records.append(user)
    save_records(records)
    return user


def find_user_index(records: list[dict[str, Any]], user_id: int) -> int:
    """Busca la posicion de un usuario por id."""
    for index, user in enumerate(records):
        if user["id"] == user_id:
            return index
    raise ValueError("Usuario no encontrado.")


def update_user(user_id: str, *args: str) -> dict[str, Any]:
    """Actualiza nombre y email usando args para recibir valores dinamicos."""
    if len(args) != 2:
        raise ValueError("Debes enviar nombre y email para actualizar.")

    name, email = args
    records = load_records()

    try:
        valid_id = int(user_id)
    except ValueError as error:
        raise ValueError("El id debe ser un numero entero.") from error

    index = find_user_index(records, valid_id)
    valid_name = validate_name(name)
    valid_email = validate_email(email)

    other_emails = {
        user["email"] for user in records if user["id"] != valid_id
    }
    if valid_email in other_emails:
        raise ValueError("El email ya pertenece a otro usuario.")

    records[index]["nombre"] = valid_name
    records[index]["email"] = valid_email
    save_records(records)
    return records[index]


def delete_user(user_id: str) -> dict[str, Any]:
    """Elimina un usuario por id."""
    records = load_records()

    try:
        valid_id = int(user_id)
    except ValueError as error:
        raise ValueError("El id debe ser un numero entero.") from error

    index = find_user_index(records, valid_id)
    deleted_user = records.pop(index)
    save_records(records)
    return deleted_user


def search_users_by_name(term: str) -> list[dict[str, Any]]:
    """Busca usuarios por coincidencia parcial de nombre."""
    term = term.strip().lower()
    records = get_all_users()

    # List comprehension usada para filtrar coincidencias reales.
    return [user for user in records if term in user["nombre"].lower()]