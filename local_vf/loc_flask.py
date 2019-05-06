from flask import Flask, render_template, request
import sqlite3


import Facade
from Place import Place
from Recherches import Recherche

from Carte import Carte

conn = sqlite3.connect(Facade.get_data_DB(),check_same_thread=False)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', name=Facade.get_name())


@app.route("/hotels")
def hotels():
    return render_template('Places.html', hotel_list=Place.get_places(conn))

@app.route("/reservations")
def reservations():
    return render_template('recherches.html',cuisine_liste=Place.get_cuisine(conn))

@app.route("/find_place", methods=['GET', 'POST'])
def find_room():
	cp = request.args.get('dept')
	cu = request.args.get('cu')
	ty = request.args.get('ty')

	room_number = Recherche.find_place(conn,cu,ty,cp)

	if room_number is  None:
		return render_template("no_place_found.html",zone=cp)
	
	Carte(cp,cu,ty).sauve(conn)

	return render_template("map.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
