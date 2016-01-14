#Use the programming interface to complete this task.
#Input: A string containing alphanumeric characters.
#Output: A string containing only the letters of the input.
#Read the input from a file called looking-for-letters.in that's in the current working directory, 
#and then write your output to a file called looking-for-letters.out.
fh = open("looking-for-letters.in", "r")
text = fh.readline()
print(text)
result = list(text)
strlen = len(text)
newstring = ""
for x in range(0, strlen):
	#print(ord(result[x]))
	if(ord(result[x]) > 57):
		newstring = newstring + result[x];
print(newstring)
fo = open("looking-for-letters.out","w")
fo.write(newstring+"\n")
fo.close()
