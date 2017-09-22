import random
import os



#To GENERATE The PASSWORD
def Password():
	os.system("clear")
	password=""
	length=input("What Do You Want The Length Of PASSWORD To Be : ")
	if length <= 0:
		raw_input( "\nINVALID INPUT : Input Error\n\nDo you want to TRY AGAIN press<ENTER>")
		Password()
	len=0
	while len <= length:
		len+=1
		password+=chr(random.randrange(33,126))

	
	print "\n\n\t\tYour UNIQUE PASSWORD Is : "+password+"\n\n"

	try_again=raw_input("Do You Want To Try Another Password (y/n) : ")
	if try_again=='y' or try_again=='Y' or try_again=='YES' or try_again=="Yes" or try_again=='yes' :
		Password()
	elif try_again=="n" or try_again=="N" or try_again=="No" or try_again=="NO" or try_again=="no":
		print("Thanks for TRYING ME : \nCome Again If You Need Unique PASSWORDS ")
		quit()


Password()

