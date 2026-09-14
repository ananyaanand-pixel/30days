#bill tip calculation + splitting of amount 
bill=int(input("enter bill amount="))
tip=int(input("enter tip percentage="))
tipamt=bill*(tip/100)
total=bill+tipamt
print("total amount to be paid is ->",total)
split=int(input("number of person to split the bill-"))
if split>0:
    spamt=total/split
    print("the amount to be paid by each person is -",spamt)
else:
    print("since person is only you, so enjoy paying the bill!")
