print("Enter '0' for exit.");
al = input("Enter any character: ");
if al== '0':
    exit();
else:
    if((al>='a' and al<='z') or (al>='A' and al<='Z')):
    	print(al, "is an alphabet.");
    else:
    	print(al, "is not an alphabet.");
