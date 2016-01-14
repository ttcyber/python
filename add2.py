fh = open("math-class.in", "r")
textin = fh.readline()
print(textin)
textsplit = textin.split(' ')
op = textsplit[0]
ad1 = int(textsplit[1])
ad2 = int(textsplit[2])
if (op == "add"): 
	sum = ad1 + ad2
if (op == "subtract"): 
	sum = abs(ad1 + ad2)
print(sum)
sumstr = str(sum)
fo = open("math-class.out","w")
fo.write(sumstr+"\n")
fo.close()
