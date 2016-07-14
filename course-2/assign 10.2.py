name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hr = []
lst = []
hrscount = {}
for time in handle:
    if time == ' ': continue
    if not time.startswith('From ') : continue
    time = time.rstrip()
    lst = time.split()
    hr = lst[5].split(':')
    hrscount[hr[0]] = hrscount.get(hr[0],0)+1
for h,c in sorted(hrscount.items()):
    print h,c
