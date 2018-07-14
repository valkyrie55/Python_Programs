#To find factorial of a no.
num=int(input("Enter a number"))
i=num
res=1
while(num!=0):
	res=res*num
	num-=1
print("The factorial of %d is %d"%(i,res))
