import sys
sys.path.append('./pizzapi')
import pizzapy
from pizzapy import *

first_name = 'Barack'
last_name = 'Obama'
email = ''
phone_number = '2024561111'
address = '700 Pennsylvania Avenue NW, Washington, DC, 20408'
customer = Customer(first_name, last_name, email, phone_number, address)

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
order = Order.begin_customer_order(customer, my_local_dominos)
order.add_item('P12IPAZA') # Medium (12") Handmade Pan Pizza $11.49
order.add_item('P10IGFCZ') # Small (10") Gluten Free Crust Wisconsin 6 Cheese Pizza $12.99

card = CreditCard('4100123422343234', '0115', '777', '90210')
# my_local_dominos.place_order(order, card)
print("Success")
