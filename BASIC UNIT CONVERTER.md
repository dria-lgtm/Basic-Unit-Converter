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

    # Meters → Feet
    if choice == "1":
        m = float(input("Enter meters: "))
        ft = m * 3.28084
        print("Feet:", round(ft, 2))

    # Feet → Meters
    elif choice == "2":
        ft = float(input("Enter feet: "))
        m = ft / 3.28084
        print("Meters:", round(m, 2))

    # Celsius → Fahrenheit
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print("Fahrenheit:", round(f, 2))

    # Fahrenheit → Celsius
    elif choice == "4":
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Celsius:", round(c, 2))

    # PHP → USD
    elif choice == "5":
        php = float(input("Enter PHP: "))
        usd = php * 0.017   # example rate
        print("USD:", round(usd, 2))

    # USD → PHP
    elif choice == "6":
        usd = float(input("Enter USD: "))
        php = usd * 58.7    # example rate
        print("PHP:", round(php, 2))

    # Liters → Milliliters
    elif choice == "7":
        L = float(input("Enter Liters: "))
        mL = L * 1000
        print("Milliliters:", round(mL, 2))

    # Milliliters → Liters
    elif choice == "8":
        mL = float(input("Enter Milliliters: "))
        L = mL / 1000
        print("Liters:", round(L, 4))

    # EXIT
    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

    again = input("\nConvert again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
