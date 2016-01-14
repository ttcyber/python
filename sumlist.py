fh = open("addition.in", "r")
text = fh.readline()
print(text)
text_split = text.split(',')
text_split = [int(i) for i in text_split]
print(text_split)
sum = 0
for i in range (0,len(text_split)):
	sum = text_split[i] + sum;
print(sum)
sumstr = str(sum)
fo = open("addition.out","w")
fo.write(sumstr+"\n")
fo.close()
