print("Sistema Iniciado")

# Crear algoritmo que lea 3 numeros, los almanece en uns lista y los ordende de mayor a menor.
# Manejo de funciones, listas, menu interactivo y manejo de errores

from colorama import Fore, Style, Back, init
init(autoreset=True)

from menu import show_menu, handle_option

print(Back.GREEN + "===================================================")
print(Back.GREEN  + "=========== Manejo de Lista y Errores =============")
print(Back.GREEN  + "==================== By Caja ======================")
print(Back.GREEN  + "===================================================\n")

while True:
  try:
    show_menu()
    option = input('Seleccione una opción: ') 
    handle_option(option) 

    if option == '4': 
      print(Fore.GREEN + Style.BRIGHT + '=========================================================================')
      print(Fore.GREEN + Style.BRIGHT + '=================== Gracias por usar el sistema. ========================')
      print(Fore.GREEN + Style.BRIGHT + '=========================================================================\n')
      break
  except Exception as e:
    print(Fore.RED + Style.BRIGHT + f'Error inesperado: {e}')
"""
try:
    #Algoritmo a ejecutar
    print("Ingrese 3 numeros para ordenarlo de mayor a menor")
 
except ValueError: #TypeError, IndexError, ValueError
    print("Error")
"""