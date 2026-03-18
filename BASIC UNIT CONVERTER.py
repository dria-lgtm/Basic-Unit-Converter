# Conversion dictionaries
length_units = {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "foot": 0.3048,
    "inch": 0.0254,
    "yard": 0.9144,
    "mile": 1609.34
}

weight_units = {
    "kilogram": 1,
    "gram": 0.001,
    "mg": 0.000001,
    "metric ton": 1000,
    "pound": 0.453592,
    "ounce": 0.0283495
}

temp_units = ["celsius", "fahrenheit", "kelvin"]

volume_units = {
    "liter": 1,
    "milliliter": 0.001,
    "gallon": 3.78541,
    "quart": 0.946353,
    "pint": 0.473176,
    "cup": 0.24,
    "fluid ounce": 0.0295735
}

area_units = {
    "m2": 1,
    "cm2": 0.0001,
    "km2": 1_000_000,
    "hectare": 10_000,
    "square mile": 2_589_988,
    "square foot": 0.092903,
    "acre": 4046.86
}

speed_units = {
    "meters/second": 1,
    "km/hr": 0.277778,
    "mph": 0.44704,
    "knots": 0.514444
}

currency_units = {
    "PHP": 1,
    "USD": 58.7
}

time_units = {
    "second": 1,
    "minute": 60,
    "hour": 3600,
    "day": 86400,
    "week": 604800,
    "month": 2_592_000,
    "year": 31_536_000
}

plural_units = {
    "meter": "meters",
    "kilometer": "kilometers",
    "centimeter": "centimeters",
    "millimeter": "millimeters",
    "foot": "feet",
    "inch": "inches",
    "yard": "yards",
    "mile": "miles",
    "liter": "liters",
    "milliliter": "milliliters",
    "gram": "grams",
    "kilogram": "kilograms",
    "pound": "pounds",
    "ounce": "ounces",
    "second": "seconds",
    "minute": "minutes",
    "hour": "hours",
    "day": "days",
    "week": "weeks",
    "month": "months",
    "year": "years"
}

categories = {
    "1": ("Length", length_units),
    "2": ("Weight", weight_units),
    "3": ("Volume", volume_units),
    "4": ("Area", area_units),
    "5": ("Speed", speed_units),
    "6": ("Currency", currency_units),
    "7": ("Time", time_units),
    "8": ("Temperature", temp_units)
}

# --- plural formatting ---
def format_unit(value, unit):
    if abs(value) == 1:
        return unit
    return plural_units.get(unit, unit + "s")

# --- Conversion Function ---
def convert_units(units, category, value, from_unit, to_unit):

    if category == "Temperature":
        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                return round((value * 9/5) + 32, 2)
            if to_unit == "kelvin":
                return round(value + 273.15, 2)

        if from_unit == "fahrenheit":
            if to_unit == "celsius":
                return round((value - 32) * 5/9, 2)
            if to_unit == "kelvin":
                return round((value - 32) * 5/9 + 273.15, 2)

        if from_unit == "kelvin":
            if to_unit == "celsius":
                return round(value - 273.15, 2)
            if to_unit == "fahrenheit":
                return round((value - 273.15) * 9/5 + 32, 2)

        return value

    else:
        base = units[from_unit]
        target = units[to_unit]
        return round(value * base / target, 4)


# --- Main Program ---
invalid_attempts = 0
MAX_INVALID = 6

while True:

    print("\n--- BASIC UNIT CONVERTER ---")
    for num, (name, _) in categories.items():
        print(f"{num}. {name}")
    print("9. Exit")

    choice = input("Choose a category (1-9): ")

    if choice == "9":
        print("Goodbye!")
        break

    if choice not in categories:
        print("Invalid category!")
        invalid_attempts += 1

        if invalid_attempts >= MAX_INVALID:
            print("Hint: Type the number corresponding to the category.")
            invalid_attempts = 0

        continue

    category_name, units = categories[choice]

    if category_name == "Temperature":
        units_list = units
    else:
        units_list = list(units.keys())

    print(f"\nAvailable units in {category_name}:")

    for i, unit in enumerate(units_list, 1):
        print(f"{i}. {unit}")

    try:

        from_index = int(input("From unit (enter number): ")) - 1
        to_index = int(input("To unit (enter number): ")) - 1

        if from_index not in range(len(units_list)) or to_index not in range(len(units_list)):
            print("Invalid unit selection!")
            continue

        value = float(input("Enter value: "))

        from_unit = units_list[from_index]
        to_unit = units_list[to_index]

        result = convert_units(
            units if category_name != "Temperature" else None,
            category_name,
            value,
            from_unit,
            to_unit
        )

        from_text = format_unit(value, from_unit)
        to_text = format_unit(result, to_unit)

        print(f"\n{value} {from_text} = {result} {to_text}")

    except ValueError:
        print("Invalid number entered!")
        continue

    again = input("\nWould you like to try again? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye!")
        break
