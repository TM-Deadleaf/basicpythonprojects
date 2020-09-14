import random
x="y"
while x=="y":
	no=random.randint(1,6)
	if no==1:
		print("     \n")
		print("  O  \n")
		print("     \n")
	if no==2:
		print("O    \n") 
		print("     \n")
		print("     O")
	if no==3:
		print("O    \n")
		print("   O  \n")
		print("     O")
	if no==4:
		print("O     O\n")
		print("       \n")
		print("O     O")
	if no==5:
		print("O     O\n")
		print("   O   \n")
		print("O     O")	
	if no==6:
		print("O     O\n")
		print("O     O \n")
		print("O     O")
	x=input("if you want to roll again press y othwerwise press n")
	print("\n")

