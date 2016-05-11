from random import randrange

phone_numbers=[]
x=0
while x <100:
	b=336
	c=randrange(111,999)
	d=randrange(1111,9999)
	b=str(b)
	c=str(c)
	d=str(d)
	random_number=b+"-"+c+"-"+d
	phone_numbers.append(random_number)
	x+=1

random_index = randrange(0,len(phone_numbers))
print("hey you should prank call "+ phone_numbers[random_index])
