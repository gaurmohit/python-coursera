largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" :
        break
    try:
        num=int(num)
    except:
        print "Invalid input"
        continue
    if num<smallest or smallest is None :
        smallest =num
    if num>largest or largest is None :
        largest =num
print "Maximum is", largest
print "Minimum is", smallest
