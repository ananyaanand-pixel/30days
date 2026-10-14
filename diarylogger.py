print("=== 📓 Welcome to the Day 09 Personal Diary Logger ===")


while True:
    print("\n--- Diary Actions ---")
    print("1. Write a new entry")
    print("2. Read all past entries")
    print("3. Exit Program")
    
    choice = input("Select an option (1-3): ").strip()
    
    
    if choice == "1":
        entry = input("\nType your diary entry here:\n> ").strip()
        
        # 'with open' safely handles opening and closing the file for you automatically
        # 'a' stands for append, which adds text to the end of the file instead of wiping it
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
            file.write("-" * 40 + "\n")  # Adds a nice divider line between entries
            
        print("✅ Entry saved successfully to 'diary.txt'!")
        
   
    elif choice == "2":
        print("\n📖 Reading your past diary entries:\n")
        print("=" * 40)
        
       
        try:
            # 'r' stands for read mode
            with open("diary.txt", "r") as file:
                content = file.read()
                
                # Check if the file is completely empty
                if not content.strip():
                    print("[ Your diary file is empty. Type entry #1 first! ]")
                else:
                    print(content)
                    
        except FileNotFoundError:
            print("[ No diary records found yet. Try writing your first entry! ]")
            
        print("=" * 40)
        
   
    elif choice == "3":
        print("👋 Closing your diary. Keep protecting your streak!")
        break
        
    else:
        print("⚠️ Invalid choice! Please select 1, 2, or 3.")
