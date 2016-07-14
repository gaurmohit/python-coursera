import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter Count: '))
pos = int(raw_input('Enter Position: '))
i = 0
while i<count:
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)
  # Retrieve all of the anchor tags
  tags = soup('a')
  url =  tags[pos-1].get('href', None)
  name = re.findall('_by_([a-zA-Z]+)',url)
  i = i+1
print name[0]

