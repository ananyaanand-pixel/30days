#multiplication table(short version)
num=int(input("enter number for your table: "))
for x in range(1,11):
    print(num*x)



#multiplication table(long version)
# 1. Take integer input from the user
num = int(input("Enter a number for your table: "))

print(f"\nGenerating multiplication table for {num}:")
print("-" * 20)

# 2. Use range(1, 11) to automatically count from 1 up to 10
for x in range(1, 11):
    result = num * x
    # Using an f-string to make the output look clean like a real math book
    print(f"{num} x {x} = {result}")

print("-" * 20)
