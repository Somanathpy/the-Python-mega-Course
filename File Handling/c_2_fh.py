temperatures=[10,-20,-289,100]
fh = [ i*(9/5)+32 for i in temperatures]
file = open("fh.txt","w")
for i in fh:
	if i < -273.15:
		continue
	else:
		file.write(str(i)+"\n")
file.close()
