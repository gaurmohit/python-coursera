import json
import urllib

url = raw_input('Enter :')
jsonin = urllib.urlopen(url).read()

info = json.loads(jsonin)
total = 0

for elem in range(len(info['comments'])):
    total = total + info['comments'][elem]['count']
print total
