
from colorama import Fore, Style, Back, init 
init(autoreset=True)
from service import register_customer, view_customer, view_all_customers # Importamos las funciones del archivo service.py


def show_menu():
  print(Fore.GREEN + Style.BRIGHT + '============================== Menú Principal ==============================')
  print(Fore.GREEN + Style.BRIGHT + '1. Registrar cliente')
  print(Fore.GREEN + Style.BRIGHT + '2. Ver cliente por ID')
  print(Fore.GREEN + Style.BRIGHT + '3. Ver todos los clientes')
  print(Fore.GREEN + Style.BRIGHT + '4. Salir')
  print(Fore.GREEN + Style.BRIGHT + '==========================================================================\n')


def handle_option(option):
  
  if option == '1':
    try:
      print(Fore.BLUE + '\nRegistrando un nuevo cliente.')
      id = input('Ingrese el ID del cliente: ')
      name = input('Ingrese el nombre del cliente: ')
      email = input('Ingrese el email del cliente: ')
      phone = input('Ingrese el teléfono del cliente: ')

      if register_customer(id, name, email, phone): 
        print(Fore.BLUE + Style.BRIGHT + 'Cliente registrado exitosamente.\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Error al registrar el cliente.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al registrar el cliente: {e}\n')


  elif option == '2':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nBuscando cliente por ID.')
      id = input('Ingrese el ID del cliente : ')
      customer = view_customer(id)

      if customer: 
        print(Fore.BLUE + Style.BRIGHT + f'Cliente encontrado: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Cliente no encontrado.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al buscar el cliente: {e}\n')

  
  elif option == '3':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nMostrando todos los clientes.')
      customers = view_all_customers()

      if customers: 
        for customer in customers:
          print(Fore.BLUE + Style.BRIGHT + f'Cliente: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'No hay clientes registrados.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al mostrar los clientes: {e}\n')

  
  elif option == '4':
    print(Fore.BLUE + Style.BRIGHT + 'Saliendo del programa...\n')

  else:
    print(Fore.RED + Style.BRIGHT + 'Opción no válida. Por favor, seleccione una opción del menú.\n')