
from colorama import Fore, Style, Back, init 
init(autoreset=True) 

def validate_customer(customers, id, email):
  for c in customers:
    if c.id == id:
      print(Fore.RED + Style.BRIGHT + 'Error: El ID del cliente ya existe. Por favor, ingrese un ID único.')
      return False
    if c.email == email:
      print(Fore.RED + Style.BRIGHT + 'Error: El email del cliente ya existe. Por favor, ingrese un email único.')
      return False
  return True