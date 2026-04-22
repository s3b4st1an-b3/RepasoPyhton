"""Integraciones externas del sistema."""

from __future__ import annotations

try:
    import pandas as pd
except ImportError:  # pragma: no cover - depende del entorno
    pd = None


def users_to_dataframe(users: list[dict]) -> pd.DataFrame:
    """Convierte la lista de usuarios en un DataFrame."""
    if pd is None:
        raise RuntimeError(
            "La libreria pandas no esta instalada. Ejecuta: pip install -r requirements.txt"
        )

    dataframe = pd.DataFrame(users)
    if dataframe.empty:
        return pd.DataFrame(columns=["id", "nombre", "email"])
    return dataframe[["id", "nombre", "email"]]