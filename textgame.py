prompt=input("Do you want  to play the game yes/no").lower().strip()
list=[]
if prompt=="yes":
	p1=input("enter the direction you want to move (north/east/west/south)").lower().strip()

	if p1=="north":
		print("you have come in north direction ,there is a monster in the room of north direction,please go to nother direction")
	elif p1=="east":
		print("east direction has a beautifull room containiing lots of flowers")
	elif p1=="west":
		print("west direction has no room ,there is a wall")	
	elif p1=="south":
		print("room has a lost of games to play with")
	else:
		print("Invalid input")
	list.append(p1)
	print(list)
	if len(list)==4:
		print(list)
else:
	print("you have exited the game")
