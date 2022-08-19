l=list('1234')
print(l)
l[0]=l[1]='5'
print(l)

aree="hello"
print (aree[1:1])

a=4/5
print(a)
b=5//4
print(b)

#def fun():
	#print (pass)
	
	
a=100//5
b=20//3
print(a,b,a*b)

a=66
print('[%c]'%a)

a=[10,20]
b=a
b +=[30,40]
print(a)

a=4/5
print(a)
b=5/4
print(b)
print (a*b)

r="function. ..bguokhfhbb"
print (r.capitalize())
print("abc. DEF".capitalize())

L=[1,2,3,4]
for i in L[::1]:
	print(i)
	
set1={'yeh',50,20}
set2={80,20,'yeh'}
print (set1 & set2)
set3= set('abc')
print( set3)
set3.add('san')
print( set3)
#set3.update(set(['p','q']))
set3.update(set('pq'))
print( set3)
#set3.update(set([5,6]))
print( set3)
#set3.add(set('fine'))
print( set3)


tuple=(1,2,3)
#tuple[1]=8
print(tuple)

a='2'
b='2'
print(a+b)

a=1//3
print(a*4)
b=3/1
print (b)
print(a*b)

def solve(a,b):
	if (a==0):
		print(b)
	else:
		print (a,b)
		solve(b%a,a)
		
solve(20,50)
print(50/20)
print(59//20)
print(50%20)

List=[0,1,2,0,'python']
print(list(filter (bool,List)))

str1= str("python")
str2="python"
print (str1==str2, str1 is str2)

x=10
y=50
if x**2 >100 and y < 100 :
	print(x,y)

def fun():
	return 55++int(55.55)
	
print(fun())

myList=["python","hub"]
#for i in myList:
#	myList.append(i.upper())
#	print(myList)
	
print(myList)

a,b=1,0
a=b=a^b
print(a)