'''
Joseph Labrum
Assignment 1 - Hangman
CSCI310 - Python

This is a hangman game written in Python.
'''
import random
import re

def getGuess(tried):
	g=""
	g = input("\nEnter any letter to guess: ")
	while len(g)!=1 or str.isalpha(g)==False or tried.find(g.upper())!=-1:
		if tried.find(g.upper())!=-1 and g != "":
			print("\nYou have already tried that letter! Please try again.")
		else:
			print("\nGame only accepts single letters. Please try again.")
		g = input("\nEnter any letter to guess: ")
	return g

def playGame():
	failCount=0
	number = random.randrange(0,19)
	tried=""
	wordbank = ["BANANAS", "FLASHFLOOD", "BATMAN", "BUBBLEGUM", "LAUGHING", "ELIMINATION", "SUNSHINE", "BUTTERFLY", "PARAMETER", "HERCULES", "SWEETNESS", "JAMAICA", "DERRIERE", "SUPERSTAR", "LIFESTYLE", "PHOTOGRAPH", "TELEPHONE", "SUBSCRIPTION", "SCIENCE", "GREEN"]
	word = wordbank[number]
	Correct = [False]*len(word)

	print("\nWelcome to Hangman")

	while failCount<5 and False in Correct:

		print("\n\n\n\n   ________")
		print("   |      |")
		if failCount < 1: 
			print("   |")
		else: print("   |      O")
		if failCount < 2: 
			print("   |")
		else: 
			if failCount < 3:  
				print("   |      H")
			else: 
				print("   |     /H|")
		if failCount < 4: 
			print("   |")
		else:
			print("   |      M")
		print("   |\n  _|__________\n")

		for num in range(0,len(word)):
			if Correct[num]==False:
				print("_",end="")
			else:
				print(word[num],end=""),
			print(" ",end="")
		print("\n\nRemaining guesses: ",5-failCount)
		print("Attempted Letters: ", tried)
		
		guess = getGuess(tried)

		if word.find(guess.upper())==-1:
			failCount=failCount+1
			tried+=guess.upper()
		else:
			for m in re.finditer(guess.upper(), word):
				Correct[m.start()]=True
	print("")
	for num in range(0,len(word)):
		print(word[num],end=""),
		print(" ",end="")
	if False not in Correct:
		print("\nYou Win! Congratulations!\n")

	else:
		print("\n\nYou Lose! Game Over.\n\n")

	v = input("\nWould you like to play again?\nEnter 'Y' to play again. Enter anything else to exit: ")
	if v == "Y" or v == "y":
		playGame()
	else:
		print("THANKS FOR PLAYING!")

def main():
	playGame()

if __name__ == "__main__":
	main()
