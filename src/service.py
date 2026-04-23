
from colorama import Fore, Style, Back, init 
init(autoreset=True) 

from validate import validate_customer 
customers = []


class Customer:
  def __init__(self, id, name, email, phone):
    self.id = id
    self.name = name
    self.email = email
    self.phone = phone


def register_customer(id, name, email, phone):
  if validate_customer(customers, id, email): 
    new_customer = Customer(id, name, email, phone)
    customers.append(new_customer)
    return True
  return False

def view_customer(id):
  for customer in customers:
    if customer.id == id:
      return customer
  return None


def view_all_customers():
  return customers