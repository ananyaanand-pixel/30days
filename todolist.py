# to do list
a=[]
add=input("enter things to add in todo list: ")
a.append(add)
print(a)
extra=input("want to add more: ")
if extra=="yes":
    add1=input("enter things to add in todo list: ")
    a.append(add1)
    print(a)
elif extra=="no":
    print("thats your todo list then, ")
else:
    print("no more work")
