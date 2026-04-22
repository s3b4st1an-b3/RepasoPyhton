"""Pruebas basicas del sistema."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from file import save_records
from service import create_user, delete_user, get_all_users

try:
    import integration
    from integration import users_to_dataframe

    PANDAS_AVAILABLE = integration.pd is not None
except ImportError:
    PANDAS_AVAILABLE = False


class CrudTests(unittest.TestCase):
    """Pruebas para validar operaciones CRUD basicas."""

    def setUp(self) -> None:
        save_records([])

    def test_create_user(self) -> None:
        create_user("1", "ana", "ana@email.com")
        users = get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]["nombre"], "Ana")

    def test_delete_user(self) -> None:
        create_user("1", "luis", "luis@email.com")
        deleted = delete_user("1")
        users = get_all_users()

        self.assertEqual(deleted["id"], 1)
        self.assertEqual(users, [])

    @unittest.skipUnless(PANDAS_AVAILABLE, "pandas no esta instalado en el entorno")
    def test_dataframe_columns(self) -> None:
        create_user("1", "maria", "maria@email.com")
        dataframe = users_to_dataframe(get_all_users())

        self.assertListEqual(list(dataframe.columns), ["id", "nombre", "email"])


if __name__ == "__main__":
    unittest.main()