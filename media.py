import requests
import json

class MediaGrabber:

	places = {"tokyo": (35.6895, 139.6917), "san francisco": (37.7833, 122.4167), "facebook": (37.484666, 122.150129)}

	def __init__(self):
		pass

	def get_pics(self, lat, lng, count=5):
		"""
		Returns a list of media (picture urls) from a given area.
		"""
		url = "https://api.instagram.com/v1/media/search"
		params = {"client_id": "9a5510f048e34950bda6c0f2c87f695b", "lat": lat, "lng": lng, "count": count}
		data = requests.get(url, params=params).json()

		out_data = []
		for elem in data["data"]:
			caption = ''
			if elem["caption"]:
				caption = elem["caption"]["text"].encode('ascii', 'ignore')
			out = {
			       "image_link": elem["images"]["standard_resolution"]["url"].encode('ascii', 'ignore'),
			       "caption": 'CAPTION: ' + caption,
			       "username": 'USER: ' + elem["user"]["username"]
			       } # CHECK THIS FOR EMOTICON SHIT
			out_data.append(out)
		return out_data
