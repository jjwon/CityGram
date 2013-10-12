from flask import render_template, request
from app import app
from media import MediaGrabber

lat, lng = MediaGrabber.places["facebook"]

def default_location():
    pass

@app.route('/', methods = ['GET', 'POST'])
def index():
    global lat, lng
    hello = MediaGrabber()
    if request.method == 'POST':
        lat = request.form["lat"]
        lng = request.form["lng"]
        print lat, lng
    # lat, lng = 35.684699, 139.761196
    data = hello.get_pics(lat, lng)

    return render_template("index.html", data = data)

@app.route('/map')
def map():
    return render_template("map.html")