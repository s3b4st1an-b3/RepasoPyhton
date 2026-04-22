"""Funciones para manejo de persistencia en archivos JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "records.json"


def ensure_data_file() -> None:
    """Crea el archivo de datos si no existe."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_records() -> list[dict[str, Any]]:
    """Carga los registros desde el archivo JSON."""
    ensure_data_file()
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_records(records: list[dict[str, Any]]) -> None:
    """Guarda los registros en el archivo JSON."""
    ensure_data_file()
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)
    except OSError as error:
        raise RuntimeError("No fue posible guardar los datos.") from error