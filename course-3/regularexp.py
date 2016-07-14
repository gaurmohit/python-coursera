import re

fname = raw_input('enter file name : ')
fhan = open(fname)
y = []
x = []
for line in fhan :
   y = re.findall('([0-9]+)',line)
   if len(y) >=1 : 
      for i in y : x.append(int(i))
print sum(x)

