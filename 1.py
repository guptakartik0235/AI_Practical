# This algoritm Inputs three sides of triangle
x= int(input("1st Side = "))

y= int(input("2nd Side = "))

z= int(input("3rd Side = "))

if x+y<z or x+z<y or z+y<x:

    print("It can't form a tringle")

else:

    print("It can form a triangle")
#Results - It tells us If These 3 sides can form a triangle or not

