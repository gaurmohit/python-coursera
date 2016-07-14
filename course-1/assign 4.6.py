def computepay(h,r):
    if h<=40:
        p =h*r
    else:
        p =(40*r)+((h-40)*r*1.5)
    return p
try:
    hrs = float(raw_input("Enter Hours:"))
    ra = float(raw_input("Enter Rate:"))
except:
    print "error, enter numeric value only"
    quit()
pay = computepay(hrs,ra)
print pay
