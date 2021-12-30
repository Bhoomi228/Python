#Calculate perimeter of a circle

radius=float(input("Enter the Radius:"))
pi=3.14

perimeter=int(2*pi*radius)
print("Perimeter of circle with  radius {} is {}".format(radius,perimeter))




#Calculate the Area od Cone where area=(1/3 *pi *r*r*h)

radius=float(input("Enter the Radius:"))
height=float(input("Enter the Height:"))
pi=3.14

area= int( 1/3*pi*radius*radius*height)
print("The Area of Cone with radius {} and height {} is {}".format(radius,height,area))
