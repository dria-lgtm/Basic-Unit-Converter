# BASIC UNIT CONVERTER

    while True:
        print("\n--- BASIC UNIT CONVERTER ---")
        print("1. Meters to Feet")
        print("2. Feet to Meters")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. PHP to USD")
        print("6. USD to PHP")
        print("7. Liters to Milliliters")
        print("8. Milliliters to Liters")
        print("9. Exit")

        choice = input("Choose (1-9): ")
    
        if choice == "1":
            m = float(input("Enter meters: "))
            print("Feet:", round(m * 3.28084, 2))
    
        elif choice == "2":
            ft = float(input("Enter feet: "))
            print("Meters:", round(ft / 3.28084, 2))
    
        elif choice == "3":
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", round((c * 9/5) + 32, 2))
    
        elif choice == "4":
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", round((f - 32) * 5/9, 2))
    
        elif choice == "5":
            php = float(input("Enter PHP: "))
            print("USD:", round(php * 0.017, 2))
    
        elif choice == "6":
            usd = float(input("Enter USD: "))
            print("PHP:", round(usd * 58.7, 2))
    
        elif choice == "7":
            L = float(input("Enter Liters: "))
            print("Milliliters:", round(L * 1000, 2))
    
        elif choice == "8":
            mL = float(input("Enter Milliliters: "))
            print("Liters:", round(mL / 1000, 4))
    
        elif choice == "9":
            print("Goodbye!")
            break
    
        else:
            print("Invalid choice!")
    
        again = input("\nConvert again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break
