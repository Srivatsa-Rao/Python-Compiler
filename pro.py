#!/usr/bin/python
import json
import urllib
url=""
response=urlib.urlopen(url)
data=json.loads(response.read())
print data
