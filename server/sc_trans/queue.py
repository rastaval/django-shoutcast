import urllib2


req = urllib2.Request('http://localhost:5000/management/queue')
response = urllib2.urlopen(req)
print response.read()
