Improvements:
- Conversion logic separated into functions
- Input validation centralized
- Main loop handled in `run_program()`
- Improved readability and maintainability

# TECHNOLOGY USED

1. Phython
2. Github

### JUSTIFICATION

Python was chosen because it is beginner-friendly, readable, and ideal for mathematical calculations and menu systems.


# METHODOLOGY

## Core Feature Implementation

### Menu-Based System
Implemented using a `while` loop and `if-elif-else` statements to allow continuous conversions until the user exits.

### Conversion Calculations
Each conversion uses direct mathematical formulas.

Example:
F = (C × 9/5) + 32
USD = PHP / exchange_rate

### Error Handling
Implemented using `try-except` blocks to prevent crashes from invalid inputs.

### Rounding
Used Python’s `round()` function for decimal precision

# COMMUNICATION

This project runs entirely in the terminal.

- Frontend: Terminal input/output  
- Backend: Python functions handling logic  

Flow:
User input → Processed by function → Output displayed in terminal  

# KEY DESIGNS

1. Offline currency conversion  
   - Exchange rates are manually set  
   - Trade-off: Not real-time but works offline  

2. Menu-based system instead of GUI  
   - Chosen for simplicity and beginner focus  

3. No external libraries  
   - Keeps project portable and simple  

# CONSIDERATIONS

1. Accuracy  
   - Used standard SI formulas  
   - Verified correct unit relationships  

2. User Privacy  
   - No data collection  
   - Fully offline program  

3. Accessibility  
   - Simple text interface  
   - Clear instructions  
   - Error messages guide users  

4. Transparency  
   - Exchange rates and formulas visible in code  

# REFERENCES

National Institute of Standards and Technology. (2019). *Guide for the use of the International System of Units (SI).* https://www.nist.gov  

Investopedia. (2024). *Currency conversion definition.* https://www.investopedia.com  
