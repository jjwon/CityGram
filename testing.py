import requests
import json

places = {"tokyo": (35.6895, 139.6917), "san francisco": (37.7833, 122.4167)}

class MediaGrabber:

	def __init__(self):
		pass

	"""
	get_pics returns a list of media from a given area.
	"""

	def get_pics(self, lat, lng):

		url = "https://api.instagram.com/v1/media/search"
		params = {"client_id": "9a5510f048e34950bda6c0f2c87f695b", "lat": lat, "lng": lng, "count": 5}
		data = requests.get(url, params=params).json()

		return data["data"]


def main():

	hello = MediaGrabber()
	lat, lng = places["tokyo"]
	# lat, lng = 35.684699, 139.761196
	data = hello.get_pics(lat, lng)

	with open("data.txt", 'w') as outfile:
		json.dump(data, outfile, sort_keys=False, indent=4, separators=(',', ': '))




if __name__ == "__main__":
	main()