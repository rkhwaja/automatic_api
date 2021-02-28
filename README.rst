Archived project
================
The Automatic company has shutdown so this project is archived

Overview
========
Python support for the Automatic API which is documented at https://developer.automatic.com/documentation/

Usage
=====

.. code:: python

 scopes = ["public", "location", "vehicle:profile", "vehicle:events", "trip"]
 automatic = Automatic(<<clientId>>, <<clientSecret>>, <<credentialsPath>>, scopes)
 trips = automatic.Trips()
