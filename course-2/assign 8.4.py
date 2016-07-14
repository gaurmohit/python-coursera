fname = raw_input("Enter file name: ")
if fname=='a':
    fname='romeo.txt'
fh = open(fname)
lst = list()
lt = []
for line in fh:
    lst =line.split()
    for i in range(len(lst)):
        if not lst[i] in lt:
            lt.append(lst[i])
        if lst[i]=="\n":
            break
        i=i+1
lt.sort()
print lt
    
