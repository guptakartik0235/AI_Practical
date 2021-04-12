#Enter an comma-seperated list with as much integers you want (Please only Include integers 
#Avoid spaces between comma & integers

l=[]

sum = 0

n = (input("list = "))

(k) = n.split(",")

for i in range(len(k)):

    sum = sum + int(k[i])

print("Sum = ",sum)

avg = sum/len(k)

print("Average = ",avg)

#Results - It will pass out the Average & Sum of the list as a result.
