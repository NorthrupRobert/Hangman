# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep

import random
import graphics
  
# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def word_selected(fname):
    word_file = open(fname,'r+')
    secret_word = random.choice(word_file.read().split())
    word_file.close()
    return secret_word

MAX_NUMBER_OF_WRONGS = 6

word = word_selected("words.txt")
win = False
wrongs = 0
knownCharacters = [] #LOWER CASE
triedCharacters = [] #ALSO LOWER CASE

clear()
graphics.TitleScreen()
print("GAME WILL BEGIN MOMENTARILY!")
sleep(3)

while (wrongs < MAX_NUMBER_OF_WRONGS) and not win:
	i = 0
	clear()
	print("Letters tried so far: ", end = "")
	
	j = 0
	while j < len(triedCharacters):
		print(triedCharacters[j].upper() + " ", end = "")
		j += 1
	print()
		
	print("Number of wrong tries (out of %d): %d" % (MAX_NUMBER_OF_WRONGS, wrongs))
	while i < len(word): #Get this to print only what you have figured out thus far
		try:
			if (None != knownCharacters.index(word[i].lower())): #should only return the first occurance of the letter known for now
				print (word[i].upper() + "", end = "")
		except:
			print("_", end = "")
		i += 1
	print()
	
	attempt = input("Try a letter!: ")
	if attempt == "END":
		break
	elif len(attempt) == 1:
		triedCharacters.append(attempt)
		j = 0
		while j < len(word):
			if (attempt.upper() == word[j].upper()):
				knownCharacters.append(attempt.lower())
				if (len(knownCharacters) == len(word)):
					win = True
					break
				else:
					chars = 0;
					count = 0;
					while count < len(word):
						try:
							if (None != knownCharacters.index(word[count].lower())): #should only return the first occurance of the letter known for now
								chars += 1
						except:
							chars = chars
						if chars == len(word):
							win = True
							break
						count += 1
				break
			j += 1
		if j == len(word):
			print("Aww shoot, that one attempt down!")
			sleep(2)
			wrongs += 1
	else:
		print("That input didn't seem to work, try again!")

clear()
print("The word was %s!" % word.upper())
print()

if wrongs == MAX_NUMBER_OF_WRONGS:
	print("YOU SUCK, HAHAHAHA")
	print("(Expand window size if it doesn't look right.)")
	graphics.Lose()
	print("(Expand window size if it doesn't look right.)")
elif (win):
	print("Congrats chief!")
	print("(Expand window size if it doesn't look right.)")
	graphics.Win()
	print("(Expand window size if it doesn't look right.)")