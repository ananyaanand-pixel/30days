#bill tip calculation + splitting of amount 
bill=int(input("Enter the bill amount: "))
tip=int(input("Enter the tip percentage: "))
tipamt=(bill*tip)/100
total=bill+tipamt
print("The tip amount is: ",tipamt)
print("The total amount to be paid is: ",total)
split=int(input("Enter the number of people to split the bill: "))
if split>0:
    amtpp=total/split
    print("The amount per person is: ",amtpp)
else:
    print("since number of people is zero, so no split.")
    
