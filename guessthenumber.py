import random
def guess(no):
	guessed_number=int(input("enter your number to check the validity"))
	valid=isinstance(guessed_number,int)
	if(valid==True):
		if(no==guessed_number):
			print("You have guessed the right number")
		elif(guessed_number-no>=10):
			print("Your number is too high")
		else:
			print("Your number is too low")
no=random.randint(1,100)
guess(no)
print("\n")
