# =============================================================================
# COVER
# =============================================================================
# Name: Gomez Rodriguez Jose de Jesus 
# Matriculation: 2430475
# Group: IM1
# Course: Communication and Digital Skills
# Assignment: Loops in Python (for / while)
# =============================================================================


# =============================================================================
# EXECUTIVE SUMMARY (6-10 lines)
# =============================================================================
"""
This document practices loop constructs in Python: for and while. A for loop is
used when the number of iterations is known or when iterating over sequences;
a while loop is used when repetition depends on a condition (sentinel, attempts,
menu). Counters and accumulators are introduced to count items and sum values.
Careful design of loop exit conditions prevents infinite loops. The file
contains six problems demonstrating for+range, for over lists, while with
sentinels, attempt-limited authentication, menus, and nested loops for patterns.
Each problem includes description, inputs, outputs, validations and three test
cases (normal, border, error).
"""
# =============================================================================


# =============================================================================
# GOOD PRACTICES (COMMENTS)
# =============================================================================
# - Use for with range() when you know how many iterations are required.
# - Use while when iterations depend on runtime conditions or sentinels.
# - Initialize counters and accumulators before entering the loop.
# - Update loop control variables in while loops to avoid infinite loops.
# - Keep loop bodies simple; move complex logic to functions.
# =============================================================================


# =============================================================================
# PROBLEM TEMPLATE (to appear before each problem)
# =============================================================================
# Problem X: <short title>
# Description: 2-4 lines explaining what the program does.
#
# Inputs:
# - ...
#
# Outputs:
# - ...
#
# Validations:
# - ...
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...
# =============================================================================


# ============================================================
# PROBLEM 1: Sum of range with for
# ============================================================
"""
Problem 1: Sum of range with for
Description:
Calculate the sum of integers from 1 to n (inclusive). Also calculate the sum
of even numbers in the same range using a for loop.

Inputs:
- n (int)

Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validations:
- n must be convertible to int and n >= 1
- On invalid input print "Error: invalid input"
"""

def sum_range_and_even_sum(n):
    # Validate
    try:
        n_int = int(n)
    except:
        return "Error: invalid input"

    if n_int < 1:
        return "Error: invalid input"

    total_sum = 0
    even_sum = 0
    for i in range(1, n_int + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i

    return {"Sum 1..n": total_sum, "Even sum 1..n": even_sum}

# --- Problem 1 Tests ---
print("\n--- Problem 1 Tests ---")
tests_p1 = [
    # Normal
    10,    # sum 1..10 = 55, even sum = 2+4+6+8+10 = 30
    # Border
    1,     # sum 1..1 = 1, even sum = 0
    # Error
    "zero" # invalid
]
for t in tests_p1:
    print("Input:", t)
    print("Result:", sum_range_and_even_sum(t))


# ============================================================
# PROBLEM 2: Multiplication table with for
# ============================================================
"""
Problem 2: Multiplication table with for
Description:
Generate a multiplication table for a base number from 1 to m inclusive.

Inputs:
- base (int)
- m (int)

Outputs:
- Lines formatted: "<base> x <i> = <product>" for i in 1..m

Validations:
- base and m convertible to int
- m >= 1
- On invalid input print "Error: invalid input"
"""

def multiplication_table(base, m):
    try:
        base_i = int(base)
        m_i = int(m)
    except:
        return "Error: invalid input"

    if m_i < 1:
        return "Error: invalid input"

    lines = []
    for i in range(1, m_i + 1):
        product = base_i * i
        lines.append(f"{base_i} x {i} = {product}")

    return {"Table": lines}

# --- Problem 2 Tests ---
print("\n--- Problem 2 Tests ---")
tests_p2 = [
    # Normal: base 5, m 4
    (5, 4),
    # Border: m = 1
    (7, 1),
    # Error: m = 0
    (3, 0)
]
for t in tests_p2:
    print("Input:", t)
    result = multiplication_table(*t)
    print("Result:", result)


# ============================================================
# PROBLEM 3: Average of numbers with while and sentinel
# ============================================================
"""
Problem 3: Average of numbers with while and sentinel
Description:
Read numbers repeatedly until sentinel_value (-1) is entered. Compute count and
average of valid numbers. If no valid numbers were entered, return error.

Inputs:
- A sequence of numbers (floats) terminated by sentinel -1 (the sentinel is not included in calculations)

Outputs:
- "Count:" <count>
- "Average:" <average_value>
- If no valid numbers, "Error: no data"

Validations:
- Each input must be convertible to float; ignore invalid conversions with an error message or treat them as invalid input.
- The sentinel is -1 (float)
"""

def average_with_sentinel(inputs, sentinel=-1.0):
    """
    inputs: iterable of values (strings or numbers) representing user entries in order.
    sentinel: numeric sentinel value (default -1.0)
    Returns dict or error message strings as specified.
    """
    total = 0.0
    count = 0

    for entry in inputs:
        # attempt to convert
        try:
            num = float(entry)
        except:
            # invalid numeric entry -> treat as invalid input (spec says attempt conversion and validate)
            return "Error: invalid input"

        if num == sentinel:
            break
        total += num
        count += 1

    if count == 0:
        return "Error: no data"

    average = total / count
    return {"Count": count, "Average": average}

# --- Problem 3 Tests ---
print("\n--- Problem 3 Tests ---")
tests_p3 = [
    # Normal: three numbers then sentinel
    [10, 20.5, 30, -1],
    # Border: first entry is sentinel (no data)
    [-1],
    # Error: invalid numeric input among entries
    [5, "abc", -1]
]
for t in tests_p3:
    print("Input:", t)
    print("Result:", average_with_sentinel(t))


# ============================================================
# PROBLEM 4: Password attempts with while
# ============================================================
"""
Problem 4: Password attempts with while
Description:
Allow user up to MAX_ATTEMPTS tries to enter the correct password.
If correct within attempts: "Login success", else after attempts: "Account locked"

Inputs:
- A sequence of attempt strings (simulating user inputs)

Outputs:
- "Login success" if matched
- "Account locked" if all attempts used without success

Validations:
- MAX_ATTEMPTS > 0
"""

MAX_ATTEMPTS = 3
CORRECT_PASSWORD = "admin123"

def password_attempts(attempts):
    """
    attempts: iterable/list of attempt strings in order.
    Returns the final message string.
    """
    if MAX_ATTEMPTS <= 0:
        return "Error: invalid configuration"

    attempts_count = 0
    for attempt in attempts:
        attempts_count += 1
        # compare as strings
        if str(attempt) == CORRECT_PASSWORD:
            return "Login success"
        if attempts_count >= MAX_ATTEMPTS:
            break

    return "Account locked"

# --- Problem 4 Tests ---
print("\n--- Problem 4 Tests ---")
tests_p4 = [
    # Normal: correct on second try
    ["wrong", "admin123"],
    # Border: correct on last allowed try
    ["x", "y", "admin123"],
    # Error: no attempts or all wrong (simulate more wrongs)
    ["a", "b", "c", "admin123"]
]
for t in tests_p4:
    print("Input:", t)
    print("Result:", password_attempts(t))


# ============================================================
# PROBLEM 5: Simple menu with while
# ============================================================
"""
Problem 5: Simple menu with while
Description:
Text menu repeats until the user chooses 0 (Exit).
Options:
1) Show greeting -> prints "Hello!"
2) Show current counter value -> prints "Counter: <value>"
3) Increment counter -> increments and prints "Counter incremented"
0) Exit -> prints "Bye!"

Inputs:
- A sequence of option inputs (each one should be convertible to int or treated invalid)

Outputs:
- Messages based on option
- For invalid option: "Error: invalid option"

Validations:
- Options must be one of 0,1,2,3 (after int conversion)
"""

def run_menu_simulation(option_inputs):
    """
    Simulate menu driven by option_inputs iterable.
    Returns list of output messages in sequence.
    """
    outputs = []
    counter = 0

    for raw in option_inputs:
        # validate conversion to int
        try:
            option = int(raw)
        except:
            outputs.append("Error: invalid option")
            continue

        if option == 1:
            outputs.append("Hello!")
        elif option == 2:
            outputs.append(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            outputs.append("Counter incremented")
        elif option == 0:
            outputs.append("Bye!")
            break
        else:
            outputs.append("Error: invalid option")

    return outputs

# --- Problem 5 Tests ---
print("\n--- Problem 5 Tests ---")
tests_p5 = [
    # Normal: show greeting, increment, show counter, exit
    [1, 3, 2, 0],
    # Border: immediate exit
    [0],
    # Error: invalid option input present
    [5, "a", 3, 2, 0]
]
for t in tests_p5:
    print("Input:", t)
    print("Result:", run_menu_simulation(t))


# ============================================================
# PROBLEM 6: Pattern printing with nested loops
# ============================================================
"""
Problem 6: Pattern printing with nested loops
Description:
Print a right-angled triangle of asterisks with n rows:
For n = 4:
*
**
***
****

Optionally also print inverted triangle.

Inputs:
- n (int)

Outputs:
- Lines of asterisks, one per row. If inverted implemented, print inverted after.
Validations:
- n convertible to int and n >= 1
- On invalid input print "Error: invalid input"
"""

def triangle_pattern(n, inverted=False):
    try:
        n_i = int(n)
    except:
        return "Error: invalid input"

    if n_i < 1:
        return "Error: invalid input"

    lines = []
    # normal triangle
    for i in range(1, n_i + 1):
        lines.append("*" * i)

    # optional inverted triangle
    if inverted:
        # add a separator for clarity
        lines.append("--- inverted ---")
        for i in range(n_i, 0, -1):
            lines.append("*" * i)

    return {"Pattern": lines}

# --- Problem 6 Tests ---
print("\n--- Problem 6 Tests ---")
tests_p6 = [
    # Normal: n = 4
    (4, False),
    # Border: n = 1
    (1, False),
    # Error: invalid n
    ("zero", False)
]
for t in tests_p6:
    print("Input:", t)
    print("Result:", triangle_pattern(*t))


# =============================================================================
# CONCLUSIONS (5-8 lines) - comments
# =============================================================================
"""
Conclusions:
- Use for loops (and range) when the number of iterations is known: they are concise
  and safe for counters and simple accumulations.
- Use while loops when repetition depends on runtime conditions (sentinels, menus,
  attempt limits) but always ensure the loop variable changes to avoid infinite loops.
- Counters and accumulators help track quantity and sums inside loops and are
  foundational to many algorithms (averages, totals, statistics).
- Menus and login attempts are typical while-loop examples; nested loops are useful
  for patterns and matrix-like tasks.
- Validating inputs before and inside loops reduces runtime errors and unexpected behavior.
"""
# =============================================================================


# =============================================================================
# REFERENCES (minimum 5) - comments
# =============================================================================
# References:
# 1) Python documentation - The for statement
# 2) Python documentation - The while statement
# 3) Real Python - "For Loops in Python"
# 4) Real Python - "While Loops in Python"
# 5) "Automate the Boring Stuff with Python" - Chapter on Flow Control
# =============================================================================
