 # Datatype in python
'''
'
1. Number(int, complex, float )
2. sequence type (string, tuple, list)
3. boolean
4. set
5. dictionary

'''
# Numbers datatypes
'''
a = 5;
b = 10.5;
c = 4j;

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

'''
# Sequence type datatype
'''
a = "ghaziabad";
b = ("mumbai","delhi","kolkata","chennai");
c = ["india","pakistan","nepal","srilanka"];

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'''

# Boolean datatype
'''
x = true
print(x)
print(type(x))
'''

# Set datatype
'''
 c = {"india","pakistan","nepal","srilanka"};

 print(c)
 print(type(c))
 '''

 # Dictionary datatype

Dict = {'brand': 'lamborgini', 'model': 'aventador', 'color': 'matt black'}
'''
 print("car brand ", Dict['brand'])
 print("car model ", Dict['model'])
 print("car color ", Dict['color'])
 '''
# rules for making variables in python


'''
1. Do not use space while making variables (my_name = "varun";)
2. Do not use special symbols while making variables (n@me = "varun";)
3. Do not use number as first letter of your variables (8list = "list";)
4. Invalid (my name ="";, n@me = "";)
5. valid ( my name = ""; mynam3 = ""; my_name = "";)
'''
# Invalid variable type
'''
my name = "varun";
n@me = "varun sharma ";
8list = "list";

print(my name)
print(n@me)
print(8list)
'''
'''

name = "varun";
mynam3 = "varun sharma";
my_name = "sharma varun";

 print(name)
 print(mynam3)
 print(my_name)
 '''

 # type casting in python
'''
 x = int(5.55);
 print(x)
 print(type(x))


#  invalid type casting

  x = int ("varun")
 print(x)
 print(type(x))

'''
  # Taking Input from user
'''
ipt = input("enter a numer : ")
ipt = int()
print(" you entered numer : ", ipt )
print(type(ipt))

print(1,2,3,4,5, sep=' # ')


print('value is : {capital}} & {country}' .format(
    capital = 'canberra', country = 'australia'))
'''

# Operqators in python

# Arithmetic operator (+,-,*,/,%,//,**)

 # x = 5
 # y = 3

'''
print("The Addition is : ", x + y)
print("The subtraction is : ", x - y)
print("The Muitiplication is : ", x * y )
print("The Divide is : ", x / y)
print("The Modulus is : ", x % y )
print(" The Explonation  is : ", x ** y)
print("The Floor Division is : ", x// y)
'''

# Assignment operator (+=, -=, *=, /=, **=, =)
'''
x += 3  # x = x + 3
print(x)
x -= 3  # x = x -3
print(x)
x *= 3  # x = x * 3
print(x)
x /= 3
print(x)
x **= 3
print(x)
x == 3
print(x)
'''

# Comparison operator (==, >, <, <=, >=, !=)
'''
print(" Comparison == is :", x == y)
print(" Comparison > is :", x > y)
print(" Comparison < is :", x < y)
print(" Comparison <= is :", x <= y)
print(" Comparison >= is :", x >= y)
print(" Comparison != is :", x != y)
print(type(x != y))
'''

# Logical operator ( and , or, not)
'''
print(x == 6 and y == 3) # false
print(x == 5 or y == 3 ) # true
print(not(x == 6 and y == 3)) # false
'''
# bitwise operator (^,|, ~, <<, >> )

# x = 7
# y = 2
'''
print("Bitwise for Xor ^ ", x ^ y)  #0111 ^ 0010 =0101 0*0=0, 1*0=1, 1*0=1, 1*1=0
#0111 | 0010 = 0111 0*0=0, 1*0=1, 0*1=1, 1*1=1
print("Bitwise for or | ", x | y)
#0111 & 0010 = 0010 0*0=0, 1*1=1, 0*1=0, 1*0=0
print("Bitwise for and & ", x & y)
print(~(x)) #0111 -1000 -8
print("Bitwise for ls << ", x << 2) # 7 * 2 = 14 , 14 * 2 = 28
print("Bitwise for rs >>", x >> 2) # 7 / 2= 3.5 ,3/ 2 = 1
'''

# membership operator (in, not in)
'''
x = ["India","pakistran"]
print("India" in x)

x = ["India","pakistran"]
print("Nepal" not in x)
'''

# identity operator (is, is not)
'''
x = ["BMW", "Audi", "Rangerover"]
y = ["BMW", "Audi", "Rangerover"]
z = x

print(x is z )
print(x is y )
print(x == y )
print(x is not y)
print(x != y)

'''
# if-else statement
'''
age = int(input("enter your age :"))

if age > 1 and age < 18:
  print("you are not eligible for registration")
elif age >= 18 and age <= 90:
  print("you are eligible for registration ")
  if age > 18 and age <50:
    print("you are too young! (nested if)", age)
  else:
    print("you are in mid range (elsen nested)", age)
else:
  print("our recommandation is to make old age cards")
  '''

  # switch case statement
'''
def day1():
    return "monday"

def day2():
    return "tuesday"

def day3():
    return "wednesday"

def day4():
    return "thursday"

def day5():
    return "friday"

def day6():
    return "saturday"

def day7():
    return "sunday"
  
def default(): 
    return "incorrect day"

switcher = {
    1: day1,
    2: day2,
    3: day3,
    4: day4,
    5: day5,
    6: day6,
    7: day7,

   }

def switch(Dayweak):
    return switcher.get(Dayweak, default)()

inp=int(input("plese enter Day number 1 to 7"))
print(switch(inp))
'''
# Loops in python (While, for, nested)

# while loop
'''
a = 1
while a < 11:
  print(a)
  a += 1 # a = a+1
'''
# for loop 
'''
num = int(input("enter a number for table :"))

for a in range(1, 11):
  print(num, 'x', a, '=', num*a)
'''

# nested loop
'''
colour = ["red", "yellow", "matte black"]
car = ["bently", "mclaren", "BMW"]
  
for x in colour:
  for y in car:
    print(x, y)
'''

 # break & continue statement
 
 # continue statement
 
 
