import sys
import requests
import json
sys.path.append('./pizzapi')
import pizzapy
from pizzapy import *
import config

lng = "-73.989"
lat = "40.733"

mapbox_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + lng + "," + lat + ".json?types=poi,address&access_token="
result = json.loads(requests.get(mapbox_url + config.access_token).content)

first_name = 'Barack'
last_name = 'Obama'
email = ''
phone_number = '2024561111'
address = result["features"][0]["place_name"]
if address[-13:] == "United States":
	address = address[:-15]
customer = Customer(first_name, last_name, email, phone_number, address)

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
order = Order.begin_customer_order(customer, my_local_dominos)
order.add_item('P12IPAZA') # Medium (12") Handmade Pan Pizza $11.49
order.add_item('P10IGFCZ') # Small (10") Gluten Free Crust Wisconsin 6 Cheese Pizza $12.99

card = CreditCard('4100123422343234', '0115', '777', '90210')
# my_local_dominos.place_order(order, card)
print("Success")
print(result["features"][0]["place_name"][:-15])