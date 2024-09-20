import urllib.request
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/India')
html = response.read()
print(html[:100])
