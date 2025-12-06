# ================================================================
# PORTADA
# ================================================================
# Name: Jose de jesus Gomez rodriguez 
# Matriculation: 2430475
# Group: IM1
#
# ================================================================
# EXECUTIVE SUMMARY
# ================================================================
# This program generates the Fibonacci series up to n terms based
# on user input. The Fibonacci sequence begins with 0 and 1, and
# each following number is the sum of the previous two. The program
# reads an integer, validates the input, and displays the series
# using a loop. Input validation ensures that n is a positive
# integer within an acceptable range. The solution demonstrates
# the use of variables, loops, and clean program structure.
#
# ================================================================
# PROBLEM DOCUMENTATION
# ================================================================
# Problem: Fibonacci series generator
#
# Description:
# Program that reads an integer n and prints the first n terms of
# the Fibonacci series starting at 0 and 1.
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - "Fibonacci series:" followed by the n terms separated by spaces
#
# Validations:
# - n must be an integer
# - n must be >= 1
# - Optional limit: n <= 50 (to avoid excessively long series)
#
# ---------------------------------------------------------------
# TEST CASES
# ---------------------------------------------------------------
# 1) Normal case:
#    Input: n = 7
#    Output: Fibonacci series: 0 1 1 2 3 5 8
#
# 2) Border case:
#    Input: n = 1
#    Output: Fibonacci series: 0
#
# 3) Error case:
#    Input: n = -3 or n = "abc"
#    Output: Error: invalid input
#
# ---------------------------------------------------------------
# OPTIONAL DIAGRAM (TEXT DESCRIPTION)
# ---------------------------------------------------------------
# Flowchart (text):
# 1. Start
# 2. Read n
# 3. Validate n
#     - If invalid, print error and stop
# 4. Initialize first two terms (0, 1)
# 5. Use loop to print the first n terms
# 6. End
#
# ================================================================
# CODE IMPLEMENTATION
# ================================================================

print("Number of terms:", end=" ")

user_input = input().strip()

# --- Input validation ---
if not user_input.isdigit():
    print("Error: invalid input")
else:
    n = int(user_input)

    # Check valid range
    if n < 1 or n > 50:
        print("Error: invalid input")
    else:
        # Fibonacci logic
        print("Fibonacci series:", end=" ")

        if n == 1:
            print("0")
        else:
            first_term = 0
            second_term = 1
            print(first_term, second_term, end=" ")

            # Loop from 3 to n
            for _ in range(3, n + 1):
                next_term = first_term + second_term
                print(next_term, end=" ")
                first_term = second_term
                second_term = next_term

            print()  # newline at the end

# ================================================================
# CONCLUSIONS
# ================================================================
# The use of loops greatly simplifies generating the Fibonacci
# series because each term depends on the two previous ones.
# Handling special cases such as n = 1 or n = 2 ensures correct
# output formatting and program stability. Input validation is
# essential for preventing incorrect or unexpected behavior.
# This logic can also be reused in programs involving sequences,
# mathematical patterns, or iterative algorithms.
#
# ================================================================
# REFERENCES
# ================================================================
# 1) Python documentation – while and for loops
# 2) Python documentation – built-in types and numeric operations
# 3) Tutorial: Fibonacci sequence in Python (Real Python)
