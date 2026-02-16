## BASIC UNIT CONVERTER
  The Basic Unit Converter is a simple Python program that converts values between units like length, weight, temperature, and time. It takes the user’s input and instantly calculates the equivalent value, making it a useful beginner-friendly coding project.

---

**PROBLEM**

  Many people struggle with converting units quickly, especially when switching between different measurements like length, temperature, currency, or volume. There is a need for a simple, offline, and easy-to-use tool that provides accurate conversions immediately.

---

**TARGET USERS**

	1.	Students & Teachers
	2.	General users
	3.	Beginners in programming

---

**OBJECTIVES**

	1.	Create a basic unit converter using simple Python concepts.
	2.	Provide accurate conversions for different measurement categories (length, temperature, currency, volume).
	3.	Design an interface that is easy to understand using a menu-based system.
	4.	Allow multiple conversions within one run using loops.
	5.	Help users learn how if-else statements, formulas, and inputs/outputs work.

---

**FEATURES (v1.5.0)**

	- Loop feature for multiple conversions  
	- Length conversions (meters, kilometers, miles, centimeters)  
	- Mass/Weight conversions (grams, kilograms, pounds)  
	- Temperature conversions (Celsius, Fahrenheit)  
	- Time conversions (seconds, minutes, hours)  
	- Volume conversions (liters, milliliters, gallons)  
	- Currency conversion (USD, PHP)  
	- Error handling for invalid numeric inputs  
	- Decimal rounding (2–4 decimal places)  
	- Improved menu-based interface  
	- Separated conversion functions for better code structure  

---
  
**HOW TO RUN THE PROGRAM**

      - Make sure you have Python installed.
      - Save the file as unit_converter.py.
      - Open a terminal or command prompt
      -  Run with python unit_converter.py.
      - Follow the on-screen instructions.
      
---
    
**EXAMPLE OF OUTPUT**

--- Basic Unit Converter ---

1: Meters → Feet

2: Feet → Meters

3: Celsius → Fahrenheit

4: Fahrenheit → Celsius

5: PHP → USD

6: USD → PHP

_Choose (1-6): 5_

Enter PHP: 1000

USD: 17.0

Do you want to convert another value? (yes/no): yes

_Choose (1-6): 3_

Enter Celsius: 30

Fahrenheit: 86.0

# FUTURE GOALS
- Add graphical user interface (GUI)
- Add more currencies with live API
- Add unit tests
- Deploy as web application

# METHODOLOGY
1. Development Approach

The Basic Unit Converter was developed by planning the features, coding the program in Python, and testing it with different values to make sure the conversions are accurate. After testing, the project was uploaded to GitHub for storage and documentation.

2. GitHub Repository Documentation

The GitHub repository contains the source code, README, and project files. It is used to store the project, track changes, and allow updates and collaboration.

3. Core Features Implementation

The program uses Python functions and conditional statements to convert units. The user enters a value and selects the units, and the program calculates and displays the converted result.

4. Technologies Used and Justification

Python was used because it is simple and beginner-friendly. GitHub was used for version control and file management. The command line was used because it is easy to implement and does not need extra tools.

5. Backend and Frontend Communication

The user interacts directly with the program through the command line. Python processes the input and shows the output immediately.

6. Design Decisions and Trade-offs

The program was designed to be simple and easy to understand. Advanced features like a graphical interface were not included to keep it lightweight.

7. Ethical Considerations

The program does not collect user data, ensuring privacy. Accurate formulas were used, and the code is available on GitHub for transparency.
