import random
list=["PHP", "Exercises", "Backend"]
def hangman():
	cnt=4
	while cnt!=0:
		list_random=random.choice(list)
		al=input("enter the character for guessing")
		if len(al)==1:
			for i in list_random:
				if al in list_random:
					print("You have guessed the right letter")
				else:
					print("you had guessed the wrong answer")
	cnt=cnt-1
hangman()
	 
