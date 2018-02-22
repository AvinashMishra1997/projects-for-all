from sys import exit


def sumofsquares(x):
	flag = 0
	i=1
	a=1
	b=1


	if x <= 0:
		flag = 0
	else:
		for a in range(1 , x):
			for b in range(1  , a+1):
				if((a**2)+(b**2) == x):
					flag=1;
					break
				else:
					b+=1
			a+=1
	if flag ==1:
		print('True')
	elif flag == 0:
		print('False')
	exit()


