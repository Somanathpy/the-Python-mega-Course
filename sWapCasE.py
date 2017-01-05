str = raw_input("enter a String to swap case:")
x = []
for i in str:
	if i.isupper():
		i = i.lower()
		x.append(i)
	else:
		i = i.upper()
		x.append(i)
	str1 = ''.join(x)
print str1