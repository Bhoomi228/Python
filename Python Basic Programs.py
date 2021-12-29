#Calculate perimeter of a circle

radius=5.25
pi=3.14

perimeter=int(2*pi*radius)
print("Perimeter of circle with  radius {} is {}".format(radius,perimeter))

#Calculate the Area od Cone where area=(1/3 *pi *r*r*h)

radius=2.5
height=3.5
pi=3.14

area= int( 1/3*pi*radius*radius*height)
print("The Area of Cone with radius {} and height {} is {}".format(radius,height,area))


#Conversion from int to float/bool/str

num1=10
num2=20

add=float(num1+num2)

print(add)

num1=10
num2=20

add=bool(num1+num2)

print(add)

num1=10
num2=20

add=str(num1+num2)

print(add)


#Conversion from str to float/bool/int

string="55"

Float=float(string)

print(Float)

num1="10"
num2="20"

add=float(num1+num2)

print(add)

num1="10"
num2="20"

add=int(num1+num2)

print(add)

num1="10"
num2="20"

add=bool(num1+num2)

print(add)








