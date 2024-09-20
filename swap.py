#Without using third variable
'''
x=12
y=13
x,y=y,x
print("the value of x",x)
print("the value of y", y)
'''


#Using third variable
'''
x=12 
y=13
temp=x
print("the value of temp variable", temp)
x=y
print("the value of x", x)
y=temp
print("the vale of y", y)
'''

#check the number is positive, negative or zero
'''
x=int(input("Enter any number"))
if x > 0:
    print("it is a positive number")
elif x == 0:
    print("it is zero")
else:
    print("it is negative")
'''

#find the sum of natural number
'''
A=int(input("Enter any number"))
if A < 0:
    print("Plz enter positive number")
else:
    sum=0
    while A > 0:4
        sum += A
        A -= 1
    print(sum)        
'''

# write a python program to find the factorial of number
'''
A=int(input("Enter any number"))
fact=1
if A<0:
    print("factorial of this number is not exist")
if A==0:
    print("factorial of 0 is 1")
if A>0:
    for i in range (1, A+1):
        fact=fact*i
print("the factorial of number is", fact)
'''
# creat area calculator
'''
print("****AREA CALCULATOR***")
print("""preaa 1 to get Area of square
      press 2 to get Area of rectangle
      press 3 to get Area of triangle
      press 4 to get Area of circle""")

choose=int(input("Enter a number 1-4:"))
if choose==1:
    length=float(input("Enter a length "))
    area=length**2
    print("The area of Square is:",area)
    
elif choose==2:
    length=float(input("Enter a length"))
    breath=float(input("Enter a breath"))
    area=length*breath
    print("THe area of rectangle:",area)
    
elif choose==3:
    base=float(input("Enter base of triangle"))
    height=float(input("Enter height of triangle"))
    area=((1/2)*base*height) 
    print("The area of triangle:",area)
    
elif choose==4:
    radius=float(input("Enter a radius of circle"))
    area=((22/7)*radius**2)
    print("The area of circle:", area)
    
else:
    print("invalid number")   
'''
#SUM OF EVEN NUMBER UPTO 50
'''
sum=0
for i in range (0,51,2):
        sum+=i
print(sum)
'''

#WRITE A PROGRAM TO FIND FIRST 20 NUMBER AND THEIR SQUARE NUMBER
'''
for i in range (1,21):
    print(i,i**2)
'''
# WRITE A PROGRAM TO FIND THE SUM OF FIRST 10 ODD NUMBER USING WHILE LOOP
''' 
sum =0
num =0
while num <=20:
     if num%2==1:
         sum+=num
     num +=1
print(sum)         
'''

#WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 12 UPTO 100 NUMBER         
'''
for i in range (1,101):
    if i%8==0 and i%12==0:
        print (i)
'''        
#write a program to creat a billing system at supermart        
'''     
while True:
 name=input("Enter customer name ")
 total=0
 
 while True:
     print("ENTER QUANTITY AND AMOUNT")
     quantity=float(input("Enter quqntity"))
     amount=float(input("Enter amount"))
     total+=quantity*amount
     repeat=input("do you want to add more item? (yes /no)")
     if repeat=="no" or repeat=="NO":
         break
 print("_"*40)
 print("Name",name)
 print("Total amount",total)
 print("_"*40)


#######################################
num= [13, 15, 22, 23, 34, 36, 84]         
sum=0

if num % 2==0:
    sum+=num
    print(sum)           

# Initialize the starting number
num = 1

# Loop through the rows of the pyramid
for i in range(1, 5):
    # Loop through each number in the row
    for j in range(i):
        print(num, end=" ")
        num += 1
    # Move to the next line after each row
    print()
'''
#################################
'''
import numpy as np
values=np.array([[1,2,3],[4,5,6]])
my_value=values*values
print(values)
print(my_value)


import numpy as np 
array([[145, 195],
       [195, 265]])
np.dot(a,a.T)
'''
import requests
url = "https://en.wikipedia.org/wiki/Narendra_Modi"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

        
        