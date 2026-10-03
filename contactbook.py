#iiiiiii

contacts={
    "anna": "123456789",
    "bob": "123456788",
    "carol": "123456777",
    "derek": "123456666",
    "ellie": "123455555",
}

while True:
    print("main menu")
    print("1. Look up a contact number")
    print("2. Add or update a contact")
    print("3. View all contacts")
    print("4. Exit program")
    
    choice=input("enter option 1-4: ").strip()
    
    if choice=="1":
        name=input("enter name of contact: ").strip().lower()
        if name in contacts:
            print(f"{name}'s number is:  {contacts[name]}")
        else:
            print(f"{name} is not in contacts")

    if choice=="2":
        name1 = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name1] = phone
        print(f"✅ successfully saved {name1} to your contact book!")
        
    if choice=="3":
        print(f"{contacts}")
        
    if choice=="4":
        print("ended the contacts list")
        break
    
    else:
        print("choose correct option")
