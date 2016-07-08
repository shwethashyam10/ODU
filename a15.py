import random
import sys

n=6
row=1
col=0
pos=0
col_s=0
f=0
d=0

roll_again = "yes"

flag=[[0 for j in range(n)] for i in range(n)]


def check( flag ):
	count=0

	for i in range(n):
		count=0
		for j in range(n):
			if(flag[i][j]==1):
				count=count+1
		if(count==n):
			print ("The row %d was completely visited\n" %i)
			return 1

	for i in range(n):
		count=0
		for j in range(n):
			if(flag[j][i]==1):
				count=count+1
		if(count==n):
			print ("The column %d was completely visited\n" %i)
			return 1

	return 0


print ("Your initial position is 0,0")


while (roll_again=="yes"):
	print ("Rolling Dice .....")
	rnd=(int)(((random.random()*100)%6)+1)
	print ("Dice value is %d" %rnd)
	if((pos+rnd)>(n*n)):
		row=1
		col=0
		rnd=((pos+rnd)-(n*n))
		pos=0
	
	pos=pos+rnd
	col=col+rnd
		
	if(col>n):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																	
		col=col%n
		row=row+1
	if(row%2==0):
		col_s=n+1-col
	else:
		col_s=col

	print ("Your current position is %d,%d" %(row-1,col_s-1))

	flag[row-1][col_s-1]=1

	f=check(flag)
	if(f==1):
		var=input("game ends")
		quit()
	d=0
	roll_again = input("Enter yes if you want to roll again :")

print ("Your final position is %d,%d"  %(row-1,col_s-1))