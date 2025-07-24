 Indian Currency Formatter

This Python script converts a numeric value into a string formatted using the **Indian numbering system** (e.g., Lakh, Crore) by placing commas appropriately.

Features

- Supports both integers and floating-point numbers.
- Handles edge cases (less than 1000, decimal points).
- No external libraries required.

Format Style

 Western Format  Indian Format 

 123456.78       1,23,456.78   
 1000000         10,00,000     
 12345           12,345        

Input

- A number (integer or float)

Output

- A string formatted in Indian currency style

Usage Example

```python
from indian_currency import format_indian_currency

print(format_indian_currency(123456.7891))    # Output: 1,23,456.7891
print(format_indian_currency(100))            # Output: 100
print(format_indian_currency(987654321.05))   # Output: 98,76,54,321.05# Indian-Currency-Formatting
