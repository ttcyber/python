fh = open("can-you-even.in", "r")
text = fh.readline()
print(text)
textsplit = text.split(',')
textsplit = [int(i) for i in textsplit]
print(textsplit)
count = 0
for i in range (0,len(textsplit)):
	if (textsplit[i] == 0 ):
		count = count + 1;
print(count)
countstr = str(count)
fo = open("can-you-even.out","w")
fo.write(countstr+"\n")
fo.close()

#easyctf{?v=8ruJBKFrRCk}
