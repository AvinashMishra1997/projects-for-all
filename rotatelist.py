from sys import exit



def rotatelist(l , n):
	if n >= len(l):
		m = n%len(l)
		x = len(l)-m
		listt = l[-m:]+l[:x]
		print (listt)
	elif n < len(l):
		x = len(l)-n
		listt = l[-n:]+l[:x]
		print (listt)
	exit()
