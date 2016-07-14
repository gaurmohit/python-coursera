hrs = raw_input("Enter Hours:")
h = float(hrs)
rate=float(raw_input("enter rate:"))
if h<=40:
    pay=h*rate
else :
    pay=40*rate
    h=h-40
    rate=rate*1.5
    pay=pay+(h*rate)
print pay
