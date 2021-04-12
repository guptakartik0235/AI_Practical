# This algoritm Inputs three sides of triangle
x= int(input("1st Side = "))

y= int(input("2nd Side = "))

z= int(input("3rd Side = "))

if x==y==z :
    print("It's an Equilateral Triangle")
elif x==y or y==z or z==x:
    print("It's an Isoceles Triangle")
else:
    print("It's a Scalene Triangle")

# Result - It tells us the Type Of Triangle Formed




