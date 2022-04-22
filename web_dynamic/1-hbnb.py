#!/usr/bin/python3
''' Starts a Flash Web Application '''
import uuid
from os import environ
from models import storage
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
        ''' Close DB session '''
            storage.close()


            @app.route('/1-hbnb', strict_slashes=False)
            def hbnb():
                    ''' HBNB is alive! '''
                        states = storage.all(State).values()
                            states = sorted(states, key=lambda k: k.name)
                                st_ct = []

                                    for state in states:
                                                st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

                                                    amenities = storage.all(Amenity).values()
                                                        amenities = sorted(amenities, key=lambda k: k.name)

                                                            places = storage.all(Place).values()
                                                                places = sorted(places, key=lambda k: k.name)

                                                                    return render_template('1-hbnb.html',
