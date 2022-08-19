l=[2,3,4]
#l.extend(1)#Only iterable item allowed for arguments of extend function. integer is not iterable. it's type error.
l.extend([1]) #extend will add list to other lists
l.append(5) #use append function to add items to list. extend is for string objects.

print(l)