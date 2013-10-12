from flask import render_template, request
from app import app
from media import MediaGrabber

lat, lng = MediaGrabber.places["facebook"]


@app.route('/')
def index():
    lat, lng = MediaGrabber.places["facebook"]
    yolo = MediaGrabber()
    data = yolo.get_pics(lat, lng)
    return render_template("index.html", data=data)

@app.route('/stream', methods = ['GET', 'POST'])
def stream():
    global lat, lng
    hello = MediaGrabber()
    if request.method == 'POST':
        lat = request.form["lat"]
        lng = request.form["lng"]
        print lat, lng
    # lat, lng = 35.684699, 139.761196
    data = hello.get_pics(lat, lng)

    if len(data) == 0:
        return render_template("error.html")

    return render_template("stream.html", data = data)

@app.route('/map')
def map():
    return render_template("map.html")