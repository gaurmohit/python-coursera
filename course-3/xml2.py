import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')

xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
total = 0
for count in counts:
   total = total + int(count.text)
print total
