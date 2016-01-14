def summation(val):
	sum = 0
	for i in range (1,val+1):
		sum = sum + i
		print(sum)
		
import sys
val = int(sys.argv[1])
print (val)
summation(val)
