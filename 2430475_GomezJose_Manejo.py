# Portada:
# Name: Gomez Rodriguez Jose de Jesus
# Matricula: 2430475
# Group: IM1

"""
Executive Summary (6-10 lines):
This Python file contains six problems designed to practice defining and using functions.
A function in Python is a reusable block of code defined with def and used to encapsulate logic.
Parameters appear in the function definition; arguments are the actual values passed when calling it.
Separating logic into functions improves readability, reusability and makes testing easier.
Functions return values using return so callers can further process results instead of only printing.
This document includes problem descriptions, validations, implementations and test cases.
"""

# ----------------------
# Principles and best practices (short comments)
# - Prefer small functions with single responsibility.
# - Avoid duplicating code: extract repeated logic into helper functions.
# - Aim for pure functions when possible (same input -> same output, no side-effects).
# - Document each function with short comments and meaningful names.
# ----------------------

# TEMPLATE PER PROBLEM (example comment block before each problem is provided)

# -----------------------------------------------------------------------------
# Problem 1: Rectangle area and perimeter
# Description:
#   Calculate area and perimeter of a rectangle given width and height.
#
# Inputs:
#   - width (float)
#   - height (float)
#
# Outputs:
#   - prints "Area:" <area_value>
#   - prints "Perimeter:" <perimeter_value>
#
# Validations:
#   - width > 0
#   - height > 0
#   - else print "Error: invalid input"
#
# Test cases:
#   1) Normal: width=5, height=3 -> Area: 15, Perimeter: 16
#   2) Border: width=0.0001, height=1 -> valid small positive numbers
#   3) Error: width=-1, height=2 -> Error: invalid input
# -----------------------------------------------------------------------------

def calculate_area(width, height):
    """Return area of rectangle: width * height"""
    return width * height


def calculate_perimeter(width, height):
    """Return perimeter of rectangle: 2*(width + height)"""
    return 2 * (width + height)

# -----------------------------------------------------------------------------
# Problem 2: Grade classifier
# Description:
#   Classify a numeric score into letter grade A/B/C/D/F.
#
# Inputs:
#   - score (float or int)
#
# Outputs:
#   - prints "Score:" <score>
#   - prints "Category:" <grade_letter>
#
# Validations:
#   - 0 <= score <= 100
#   - else print "Error: invalid input"
#
# Test cases:
#   1) Normal: score=92 -> Category: A
#   2) Border: score=90 -> Category: A; score=89.999 -> B
#   3) Error: score=150 -> Error: invalid input
# -----------------------------------------------------------------------------

def classify_grade(score):
    """Return letter grade for numeric score (0-100)."""
    if not isinstance(score, (int, float)):
        raise TypeError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("invalid score range")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# -----------------------------------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# Description:
#   Parse a comma-separated string of numbers and summarize min, max and average.
#
# Inputs:
#   - numbers_text (string) e.g. "10,20,30"
#
# Outputs:
#   - prints "Min:" <min_value>
#   - prints "Max:" <max_value>
#   - prints "Average:" <average_value>
#
# Validations:
#   - numbers_text.strip() must not be empty
#   - all items convertible to float
#   - resulting list not empty
#   - else print "Error: invalid input"
#
# Test cases:
#   1) Normal: "10,20,30" -> Min:10 Max:30 Average:20
#   2) Border: "5" -> Min=Max=Average=5
#   3) Error: "10,abc,20" -> Error: invalid input
# -----------------------------------------------------------------------------

def summarize_numbers(numbers_list):
    """Return a dict with keys: min, max, average for a list of numbers."""
    if not numbers_list:
        raise ValueError("numbers list is empty")
    # convert elements to floats (assume they are numeric already)
    numeric = [float(x) for x in numbers_list]
    return {
        "min": min(numeric),
        "max": max(numeric),
        "average": sum(numeric) / len(numeric)
    }

def parse_numbers_text(numbers_text):
    """Convert comma-separated string to list of floats (as numbers)."""
    if not isinstance(numbers_text, str) or numbers_text.strip() == "":
        raise ValueError("invalid input")
    parts = [p.strip() for p in numbers_text.split(",") if p.strip() != ""]
    if not parts:
        raise ValueError("invalid input")
    try:
        nums = [float(p) for p in parts]
    except Exception:
        raise ValueError("invalid input")
    return nums

# -----------------------------------------------------------------------------
# Problem 4: Apply discount list (pure function)
# Description:
#   Given list of prices and discount rate, return new list with discounted prices.
#
# Inputs:
#   - prices_text (string) e.g. "100,200,300"
#   - discount_rate (float between 0 and 1)
#
# Outputs:
#   - prints "Original prices:" <original_list>
#   - prints "Discounted prices:" <discounted_list>
#
# Validations:
#   - prices_text not empty, prices > 0
#   - 0 <= discount_rate <= 1
#   - else print "Error: invalid input"
#
# Test cases:
#   1) Normal: prices="100,200", rate=0.1 -> [90.0,180.0]
#   2) Border: prices="0.01", rate=0 -> no change
#   3) Error: rate=1.5 or negative price -> Error: invalid input
# -----------------------------------------------------------------------------

def apply_discount(prices_list, discount_rate):
    """Return a new list with discounted prices. Does not modify input list."""
    if not isinstance(prices_list, list) or len(prices_list) == 0:
        raise ValueError("invalid prices list")
    if not isinstance(discount_rate, (int, float)):
        raise TypeError("discount_rate must be numeric")
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("invalid discount rate")
    discounted = []
    for price in prices_list:
        if price <= 0:
            raise ValueError("invalid price")
        discounted_price = price * (1 - discount_rate)
        discounted.append(discounted_price)
    return discounted

# Helper to parse prices text
def parse_prices_text(prices_text):
    if not isinstance(prices_text, str) or prices_text.strip() == "":
        raise ValueError("invalid input")
    parts = [p.strip() for p in prices_text.split(",") if p.strip() != ""]
    if not parts:
        raise ValueError("invalid input")
    try:
        prices = [float(p) for p in parts]
    except Exception:
        raise ValueError("invalid input")
    return prices

# -----------------------------------------------------------------------------
# Problem 5: Greeting function with default parameters
# Description:
#   Build greeting message optionally including title before the name.
#
# Inputs:
#   - name (string)
#   - title (string, optional)
#
# Outputs:
#   - prints "Greeting:" <greeting_message>
#
# Validations:
#   - name must not be empty after strip
#
# Test cases:
#   1) Normal: name="Alice", title="Dr." -> "Hello, Dr. Alice!"
#   2) Border: title empty -> "Hello, Alice!"
#   3) Error: name empty -> Error: invalid input
# -----------------------------------------------------------------------------

def greet(name, title=""):
    """Return greeting string. title is optional."""
    if not isinstance(name, str) or name.strip() == "":
        raise ValueError("invalid input")
    clean_name = name.strip()
    clean_title = title.strip() if isinstance(title, str) else ""
    full_name = f"{clean_title} {clean_name}".strip()
    return f"Hello, {full_name}!"

# -----------------------------------------------------------------------------
# Problem 6: Factorial function (iterative)
# Description:
#   Compute n! for integer n >= 0. Iterative implementation chosen for clarity and
#   to avoid recursion depth issues.
#
# Inputs:
#   - n (int)
#
# Outputs:
#   - prints "n:" <n>
#   - prints "Factorial:" <value>
#
# Validations:
#   - n integer, n >= 0, and n <= 20 (to avoid very large integers in this exercise)
#   - else print "Error: invalid input"
#
# Test cases:
#   1) Normal: n=5 -> 120
#   2) Border: n=0 -> 1
#   3) Error: n=-3 or n=50 -> Error: invalid input
# -----------------------------------------------------------------------------

def factorial(n):
    """Iterative factorial. Returns n! for n >= 0."""
    if not isinstance(n, int):
        raise TypeError("n must be integer")
    if n < 0 or n > 20:
        raise ValueError("invalid input")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# -----------------------------------------------------------------------------
# Main code: run test cases for each problem and print outputs as requested.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Problem 1 tests
    print("\n--- Problem 1 Tests ---")
    try:
        w, h = 5, 3  # normal
        if w <= 0 or h <= 0:
            print("Error: invalid input")
        else:
            print("Area:", calculate_area(w, h))
            print("Perimeter:", calculate_perimeter(w, h))
    except Exception:
        print("Error: invalid input")

    try:
        w, h = 0.0001, 1  # border
        if w <= 0 or h <= 0:
            print("Error: invalid input")
        else:
            print("Area:", calculate_area(w, h))
            print("Perimeter:", calculate_perimeter(w, h))
    except Exception:
        print("Error: invalid input")

    try:
        w, h = -1, 2  # error
        if w <= 0 or h <= 0:
            print("Error: invalid input")
        else:
            print("Area:", calculate_area(w, h))
            print("Perimeter:", calculate_perimeter(w, h))
    except Exception:
        print("Error: invalid input")

    # Problem 2 tests
    print("\n--- Problem 2 Tests ---")
    for score in [92, 90, 150]:
        try:
            if not (isinstance(score, (int, float)) and 0 <= score <= 100):
                print("Error: invalid input")
            else:
                print("Score:", score)
                print("Category:", classify_grade(score))
        except Exception:
            print("Error: invalid input")

    # Problem 3 tests
    print("\n--- Problem 3 Tests ---")
    cases = ["10,20,30", "5", "10,abc,20"]
    for case in cases:
        try:
            nums = parse_numbers_text(case)
            summary = summarize_numbers(nums)
            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])
        except Exception:
            print("Error: invalid input")

    # Problem 4 tests
    print("\n--- Problem 4 Tests ---")
    tests = [ ("100,200,300", 0.1), ("0.01", 0), ("100, -50", 0.2) ]
    for prices_text, rate in tests:
        try:
            prices = parse_prices_text(prices_text)
            discounted = apply_discount(prices, rate)
            print("Original prices:", prices)
            print("Discounted prices:", discounted)
        except Exception:
            print("Error: invalid input")

    # Problem 5 tests
    print("\n--- Problem 5 Tests ---")
    tests = [ ("Alice", "Dr."), ("Bob", ""), ("   ", "Mr.") ]
    for name, title in tests:
        try:
            greeting = greet(name, title)
            print("Greeting:", greeting)
        except Exception:
            print("Error: invalid input")

    # Problem 6 tests
    print("\n--- Problem 6 Tests ---")
    for n in [5, 0, -3]:
        try:
            if not isinstance(n, int) or n < 0 or n > 20:
                print("Error: invalid input")
            else:
                print("n:", n)
                print("Factorial:", factorial(n))
        except Exception:
            print("Error: invalid input")

# -----------------------------------------------------------------------------
# Conclusions (comments): 5-8 lines
# - Functions help organize code into reusable units and clarify intent.
# - Returning values (instead of only printing) makes functions composable and testable.
# - Default parameters and named arguments increase flexibility and readability.
# - Encapsulating repeated logic (parsing, validation) simplifies the main flow.
# - Separating main program logic from function definitions aids testing and maintenance.
# -----------------------------------------------------------------------------

# References (minimum 5) - in comments
# References:
# 1) Python documentation - Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) Python docs - More on defining functions and parameters: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
# 3) "Clean Code" ideas adapted to functions (Robert C. Martin) - general best practices
# 4) Real Python - Python functions tutorials (realpython.com)
# 5) Python standard library docs - Built-in Functions: len, sum, min, max
# -----------------------------------------------------------------------------
