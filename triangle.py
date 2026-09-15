# multiple types of '*' triangle where i ask user to input number of rows of '*' triangle and hollow triangle
#triangle
n=int(input("enter your digit"))

for x in range(1,n+1):
    print("*"*x)

#hollow triangle
for i in range(1, n + 1):
    s = " " * (n - i)
    if i == 1:
        print(s + "*")
    elif i == n:
        print("*" * (2 * n - 1))  # Solid bottom row
    else:
        # Middle spaces inside the triangle
        i_s = " " * (2 * i - 3)
        print(s + "*" + i_s + "*")
