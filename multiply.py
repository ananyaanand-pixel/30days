#multiplication table(short version)
num=int(input("enter number for your table: "))
for x in range(1,11):
    print(num*x)



#multiplication table(long version)

num = int(input("Enter a number for your table: "))

print(f"\nGenerating multiplication table for {num}:")
print("-" * 20)


for x in range(1, 11):
    result = num * x
    print(f"{num} x {x} = {result}")

print("-" * 20)



