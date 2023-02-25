def fact(i):
	if i==1:
		f=1
	else:
		f=i*fact(i-1)
	return f

num = int(input("Enter the number:"))
res = fact(num)

print("the factorial is number: %s is:"%num,res)