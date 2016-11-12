# Overview
Python support for the Automatic API which is documented at https://developer.automatic.com/documentation/

# Usage
```
scopes = ["public", "location", "vehicle:profile", "vehicle:events", "trip"]
automatic = Automatic(AutomaticSource.clientId, AutomaticSource.clientSecret, self.credentialsPath, scopes)
trips = automatic.Trips()
```
