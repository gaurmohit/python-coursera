import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')

xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)
comment = tree.findall('comments/comment')
total = 0
for item in comment:
   total = total + int(item.find('count').text)
print total
