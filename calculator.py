"""
Simple Calculator Module
Author: Saige Gee
Date: 02/11/26
Version: 1.0

This module provides basic arithmetic operations:
- Addition
- Subtraction  
- Multiplication
- Division (with zero-division protection)
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Test the functions
if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    

if __name__ == "__main__":
    print(f"6 * 7 = {multiply(6, 7)}")
    
print(f"20 / 4 = {divide(20, 4)}")
print(f"10 / 0 = {divide(10, 0)}")