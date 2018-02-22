from sys import exit




def parenthesis_checker(s):
	depth = 0;
	for a in s:
		if a == "(":
			depth += 1
		elif a == ")":
			depth -=1
	if depth == 0:
		print("True")
	else:
		print("False")
	exit()





