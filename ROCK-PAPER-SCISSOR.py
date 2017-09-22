import random
import os

def Comp_c():
	os.system("clear")
	print "========ROCK PAPER SCISSORS========"
	comp_choice = random.randint(1,3)
	if comp_choice ==1:
		Rock()
	elif comp_choice == 2:
		Paper();
	else:
		Scissors()


def Rock():
	print "1. ROCK\t2.PAPER\t3.SCISSORS\n"
	player_c=raw_input("Enter Your Choice : ")
	if  player_c== "1":
		print "TIE : you and computer both choose ROCK\n"
		play_again()
	elif player_c == "2":
		print "YOU WIN: you choose PAPER and computer choose ROCK\n"
		play_again()
	elif player_c == "3":
		print "YOU LOSE: you choose SCISSOR and computer choose ROCK\n"
		play_again()
	else :
		print "INVALID INPUT \nTRY AGAIN\n"
		Rock()

def Paper():
	print "1. ROCK\t2.PAPER\t3.SCISSORS\n"
	player_c=raw_input("Enter Your Choice : ")
	if  player_c== "1":
		print "YOU LOSE : you choose ROCK and computer choose PAPER\n"
		play_again()
	elif player_c == "2":
		print "TIE: you and computer both choose PAPER\n"
		play_again()
	elif player_c == "3":
		print "YOU WIN: you choose SCISSOR and computer choose PAPER\n"
		play_again()
	else :
		print "INVALID INPUT \nTRY AGAIN\n"
		Paper()

def Scissors():
	print "1. ROCK\t2.PAPER\t3.SCISSORS\n"
	player_c=raw_input("Enter Your Choice : ")
	if  player_c== "1":
		print "YOU WIN : you choose ROCK and computer choose SCISSOR\n"
		play_again()
	elif player_c == "2":
		print "YOU LOSE: you choose PAPER and computer choose SCISSOR\n"
		play_again()
	elif player_c == "3":
		print "TIE: you and computer both choose SCISSOR\n"
		play_again()
	else :
		print "INVALID INPUT \nTRY AGAIN\n"
		scissor()

def play_again():
	choose=raw_input("Do You Want To Play AGAIN (y/n) : ")
	if choose == "y" or choose == "Y":
		Comp_c()
	elif choose == "N" or choose == "n":
		print "THANKS For PLAYING\n"
		quit()
	else:
		play_again()

Comp_c()
