print("                  WELCOME TO HORSE  GAME")
print("__________________________________________________")
print("RULES OF THE GAME")
print("1. Any one of the player should get 6 to enter the game.")
print("2. Each one will throw your dies 6 times.")
print("3. Their horse will move those many times.")
print("4. After six throws who's horse travells more distance is the winner.")
print("__________________________________________________")
z=str(input("TYPE enter TO PROCEED :"))
print("__________________________________________________")
x=str(input("enter first player name :"))
y=str(input("enter second player name :"))
print("__________________________________________________")
import random
s=random.randint(5,6)
print("starting roll is-",s)
print("__________________________________________________")
if s==6:
		total=total1=0
		list=[]
		for i in range(6):
			import random
			i1=random.randint(1,6)
			list.append(i1)
		print(x," got : ",list)
		a=(list[0])
		b=(list[1])
		c=(list[2])
		d=(list[3])
		e=(list[4])
		f=(list[5])
		total=a+b+c+d+e+f
		print(x,"'s horse has moved to ",total,"th place")
		print("__________________________________________________")
		list=[]
		for i in range(6):
			import random
			i2=random.randint(1,6)
			list.append(i2)
		print(y," got : ",list)
		a=(list[0])
		b=(list[1])
		c=(list[2])
		d=(list[3])
		e=(list[4])
		f=(list[5])
		total1=a+b+c+d+e+f
		print(y,"'s horse has moved to ",total1,"th place")
		print("__________________________________________________")
		if total>total1:
			print("congratulations",x,"is the winner")
		else:
			print("congratulations",y,"is the winner")
			print("__________________________________________________")
else:
	print("better luck next time")
	print("__________________________________________________")

	
	
	
	