import sys
import requests
import json
sys.path.append('./pizzapi')
import pizzapy
from pizzapy import *
from tweeter_bot import *
import config
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/pizza", methods = ["POST"])
def pizza():

    if request.method == "POST":

        text, cord, id_str, screen_name = champion_tweets()
        tweet_link = 'https://twitter.com/' + screen_name + '/status/' + id_str
        lng = str(cord[0])
        lat = str(cord[1])

        mapbox_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + lng + "," + lat + ".json?types=poi,address&access_token="
        result = json.loads(requests.get(mapbox_url + config.access_token).content)

        first_name = 'ShareMate'
        last_name = 'App'
        email = ''
        phone_number = '2024561111'
        address = result["features"][0]["place_name"]
        if address[-13:] == "United States":
            address = address[:-15]
        customer = Customer(first_name, last_name, email, phone_number, address)

        my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
        order = Order.begin_customer_order(customer, my_local_dominos)

        list_of_order = [];
        for i in range (0, int(request.form["amount"])):
            list_of_order.append(order.add_item('P10IGFCZ'))
        card = CreditCard('4100123422343234', '0115', '777', '90210')
		# my_local_dominos.place_order(order, card)

        res = {'Tweet': {'text': text, 'link': tweet_link}, 'Geolocation': cord, 'Address': address, 'Local Dominos': my_local_dominos, 'Total Order': list_of_order}

        # When Dominos locations are closed
        # res = {'Tweet': {'text': text, 'link': tweet_link}, 'Geolocation': cord, 'Address': address}
    return render_template("success.html", result=res)

@app.route("/complete")
def complete():
    return render_template("complete.html")

if __name__ == "__main__":
    app.run()
