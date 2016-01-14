x = raw_input("enter the password: ");
y = "";
for c in x:
	y += chr(ord(c) ^ 14);
	print(y)
	if y == "ko}wmzhugQocQoQhbois":
		print "congratz the flag is " + y;
	else:
		print "nope";
