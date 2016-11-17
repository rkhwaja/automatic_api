from json import dump, load
from logging import debug
from os.path import exists
from urllib.parse import quote

from requests_oauthlib import OAuth2Session

class Automatic:
	tokenUrl = "https://accounts.automatic.com/oauth/access_token"
	tokenPath = "token.json"
	baseUrl = "https://api.automatic.com/"

	def __init__(self, clientId, clientSecret, tokenPath, scopes):
		self.clientId = clientId
		self.clientSecret = clientSecret
		self.tokenPath = tokenPath
		self.scopes = scopes # list of scopes
		if not exists(self.tokenPath):
			self.session = self.Authorize()

		debug("Already authorized")
		with open(self.tokenPath, "r") as f:
			token = load(f)

		extra = {"client_id": self.clientId, "client_secret": self.clientSecret}

		self.session = OAuth2Session(self.clientId, token=token, auto_refresh_kwargs=extra, auto_refresh_url=Automatic.tokenUrl, token_updater=self.TokenSaver)

	def Authorize(self):
		scopeString = quote(" ".join(["scope:" + scope for scope in self.scopes]))
		authorizationBaseUrl = "https://accounts.automatic.com/oauth/authorize/?response_type=code&scope=" + scopeString

		session = OAuth2Session(self.clientId)
		authorizationUrl, _ = session.authorization_url(authorizationBaseUrl)

		print("Go to the following URL and authorize the app:" + authorizationUrl)

		try:
			from pyperclip import copy
			copy(authorizationUrl)
			print("URL copied to clipboard")
		except ImportError:
			pass

		redirectResponse = input("Paste the full redirect URL here:")

		token = session.fetch_token(Automatic.tokenUrl, client_secret=self.clientSecret, authorization_response=redirectResponse, token_updater=self.TokenSaver)
		self.TokenSaver(token)

		return session

	def TokenSaver(self, token):
		with open(self.tokenPath, "w") as f:
			dump(token, f)

	def Trips(self):
		limit = 250
		allTrips = []
		page = 1
		while True:
			debug("Getting page {} items so far = {}".format(page, len(allTrips)))
			response = self.session.get(Automatic.baseUrl + "trip/", params={"limit": limit, "page": page}, timeout=60)
			trips = response.json()
			debug("Total items: {}".format(trips["_metadata"]["count"]))
			if "results" not in trips or len(trips["results"]) < limit:
				break
			debug("Got {} trips".format(len(trips["results"])))
			page += 1
			allTrips.extend(trips["results"])
		return allTrips

	def Vehicles(self):
		response = self.session.get(Automatic.baseUrl + "vehicle/", timeout=60)
		return response.json()["results"]

def Test():
	from logging import info
	from pprint import pformat

	clientId = ""
	clientSecret = ""
	scopes = ["public", "location", "vehicle:profile", "vehicle:events", "trip"]
	automatic = Automatic(clientId, clientSecret, "test.json", scopes=scopes)
	info(pformat(automatic.Vehicles()))
