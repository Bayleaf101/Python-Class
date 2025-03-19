hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate per Hour:")
r = float(rate)

if h <= 40:
	pay = float(h*r)
	print ('pay')
else: 
	pay = float (40*r+(h-40)*(r*1.5))
	print ('pay')