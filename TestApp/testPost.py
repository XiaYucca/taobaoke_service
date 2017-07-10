import urllib,cookielib
import urllib2

headers = {'UserAgent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'};

values = {'name':'admin','password':123};

data = urllib.urlencode(values);

url = "http://127.0.0.1:8000/home/"

request = urllib2.Request(url=url,data=data)

res = urllib2.urlopen(request)

print res.read()
