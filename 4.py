#It Inputs Gender & Age
#Firstly It Takes Age as Input
#Then it takes gender input in (M Or F)form

age = int(input("Please Enter your Age:- "))
Gender = (input("Please Enter your Gender:- ")).upper()

if Gender=="F" and age >=20 and age<=60:
    print("You can work in Urban Areas")

elif Gender=="M" and age>=20 and age<=40:
    print("You can work Anywhere") 

elif Gender=="M" and age>=40 and age<=60:
    print("You can work in Urban Areas") 

else:
    print("ERROR") 
#It then tells that if we can work in Urban Areas/Anwheyere else it shows error