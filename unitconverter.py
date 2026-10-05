#unit converter
def ctof(cel):
    f=(cel * 9/5) + 32
    return f
def feettoinch(feet):
    inch=feet*12
    return inch

while True:
    print("\n--- Available Conversions ---")
    print("1. Celsius to Fahrenheit")
    print("2. Feet to Inches")
    print("3. Exit Program")

    user=input("Enter the number of the conversion you want to perform (1-3): ").strip()

    if user=="1":
        c=float(input("enter temperature in Celsius: "))
        result=ctof(c)
        print(f"{c} Celsius is equal to {result} Fahrenheit.")
    elif user=="2":
        ft=float(input("enter length in Feet: "))
        result=feettoinch(ft)
        print(f"{ft}Feet is equal to {result} inches.")
    elif user=="3":
        print("As per yr request, exiting program...")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 3.")
        
