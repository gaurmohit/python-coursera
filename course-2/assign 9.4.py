name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = {}
line = []
largcount = None
largadd = None
for add in handle :
    if line == ' ': continue
    if not add.startswith('From '): continue
    add = add.rstrip()
    line = add.split()
    words[line[1]] = words.get(line[1],0)+1
for name,count in words.items():
    if largcount is None or count > largcount:
        largadd = name
        largcount = count
print largadd,largcount
