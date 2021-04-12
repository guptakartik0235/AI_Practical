#This Algortihm inputs the lenght & width of a Square or Rectangle
length = int(input("Enter the Length:-"))
width = int(input("Enter the Width:-"))
if width==length:
    print("Its a Square")
    print("It's area is:-",length*width)
    print("Its perimeter is:-",4*length)
else :
    print("Its a Rectangle")
    print("It's area is:-",length*width)
    print("Its perimeter is:-",2*(length+width))

#Results - It Tells us if it is a square or Rectangle along with its area & Perimter
