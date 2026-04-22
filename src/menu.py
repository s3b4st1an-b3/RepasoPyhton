"""Menu interactivo del sistema CRUD."""

from __future__ import annotations

from integration import users_to_dataframe
from service import (
    create_user,
    delete_user,
    get_all_users,
    search_users_by_name,
    update_user,
)


def show_menu() -> None:
    """Despliega el menu principal del sistema."""
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Buscar usuario por nombre")
        print("6. Salir")

        option = input("Selecciona una opcion: ").strip()

        try:
            if option == "1":
                handle_create()
            elif option == "2":
                handle_list()
            elif option == "3":
                handle_update()
            elif option == "4":
                handle_delete()
            elif option == "5":
                handle_search()
            elif option == "6":
                print("Hasta pronto.")
                break
            else:
                print("Opcion invalida. Intenta nuevamente.")
        except ValueError as error:
            print(f"Error: {error}")
        except RuntimeError as error:
            print(f"Error del sistema: {error}")
        except Exception as error:
            print(f"Ocurrio un error inesperado: {error}")


def handle_create() -> None:
    user_id = input("Ingresa el id: ")
    name = input("Ingresa el nombre: ")
    email = input("Ingresa el email: ")
    user = create_user(user_id, name, email)
    print(f"Usuario creado correctamente: {user}")


def handle_list() -> None:
    """Lista los usuarios en formato DataFrame."""
    users = get_all_users()
    dataframe = users_to_dataframe(users)
    print("\nUsuarios registrados:")
    print(dataframe.to_string(index=False))


def handle_update() -> None:
    user_id = input("Ingresa el id del usuario a actualizar: ")
    name = input("Ingresa el nuevo nombre: ")
    email = input("Ingresa el nuevo email: ")
    user = update_user(user_id, name, email)
    print(f"Usuario actualizado correctamente: {user}")


def handle_delete() -> None:
    user_id = input("Ingresa el id del usuario a eliminar: ")
    deleted_user = delete_user(user_id)
    print(f"Usuario eliminado correctamente: {deleted_user}")


def handle_search() -> None:
    term = input("Ingresa el nombre a buscar: ")
    users = search_users_by_name(term)
    dataframe = users_to_dataframe(users)
    print("\nResultado de busqueda:")
    print(dataframe.to_string(index=False))