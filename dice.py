import random

n=5
m=6
f=0
row=1
col=0
pos=0
col_s=0
roll_again = "yes"

print "Your initial position is 0,0"
print "row value 6"
print "column value 5"
while (roll_again=="yes" and f==0):
	print "Rolling Dice ....."
	rnd=(int)(((random.random()*100)%6)+1)
	print ("Dice value is %d" %rnd)
	#print ("Dice value is %d" %rnd1)
	#print (rnd+rnd1)
	if(pos+rnd>m*n):
		print ("Cannot add the dice value \n")
	else:
		pos=pos+rnd
		col=col+rnd
		#increment row and reset col when the col number exceeds n
		if(col>n):
			col=col%n
			row=row+1
		if(row%2==0):
			col_s=n+1-col
		else:
			col_s=col

	print ("Your current position is %d,%d" %(row-1,col_s-1))
	roll_again = input("Enter yes if you want to roll again :")
	if(pos==30):
		f=1;
		print ("final")

print ("Your final position is %d,%d" %(row-1,col_s-1))