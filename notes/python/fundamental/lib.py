import os

# 1 os
dir(os)
os.getcwd()
os.chdir('/home/martin/AllWorkStation/Atom/learnPython/fundamental')
os.getcwd()
os.listdir()
os.makedirs("high/low")
os.mkdir("onlyhigh")
os.rename('onlyhigh', 'onlyHigh')
os.rmdir("onlyHigh")
os.removedirs("high/low")

os.stat("charming.py")
os.environ.get("HOME")
a = os.path.join(os.environ.get("HOME"), 'AllWorkStation/Atom/learnPython/fundamental')
os.path.split(a)
os.path.basename(a)
os.path.dirname(a)
os.path.exists(a)
os.path.exists("/tmp/flus")


# 2 urllib.request
import urllib.request as url
import urllib.parse
addres = "https://www.baidu.com"
url.urlopen(addres).read()
# POST
a = "http://pythonprograming.net"
values = {'s': 'basic',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = url.Request(a, data)
url.urlopen(req).read()
# GET
data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)  # The order may differ from below.

url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)

local_filename, headers = url.urlretrieve('http://python.org/')
html = open(local_filename)
html.read()

html
req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
   the_page = response.read()

# handlig exceptions
req = urllib.request.Request('http://www.pretend_server.org')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
