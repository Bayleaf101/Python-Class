score = input("Enter Score: ")
s = float(score)
if s<0 or s>1.0:
	print ('enter a valid score')
elif s >= 0.9:
	print ('A')
elif s >= 0.8:
	print ('B')
elif s >= 0.7:
	print ('B')
elif s >= 0.6:
	print ('D')
elif s < 0.6:
	print ('D')
