# --------------------------------------------------
# PORTADA
# --------------------------------------------------
# Name: Gomez Rodriguez Jose de Jesus 
# Matriculation: 2430475
# Group: IM1
#
# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------
# In Python, integers (int) represent whole numbers, while floats (float)
# represent numbers with decimals used for precise calculations. Boolean
# values (True/False) are created from comparisons and logical evaluations
# such as >, <, ==, and logical operators like and/or/not. Validating inputs
# prevents invalid ranges, undefined operations and division by zero. This
# document includes six problems involving numeric operations, type casting,
# statistical calculations, decision making with booleans and input validation.
# Each problem contains descriptions, inputs, outputs, validations and test
# cases demonstrating the correct use of numeric and boolean types.
#
# --------------------------------------------------
# GOOD PRACTICES
# --------------------------------------------------
# - Use appropriate types: int for counters, float for decimal quantities.
# - Validate all user inputs before performing calculations.
# - Avoid repeating complex expressions by storing intermediate results.
# - Use descriptive variable names written in lower_snake_case.
# - Document how boolean flags are interpreted in each problem.
# - Ensure clear messages such as "Error: invalid input" when needed.
#
# ==================================================
# ===================== PROBLEM 1 ===================
# ===================================================
#
# Problem 1: Temperature converter and range flag
# Description:
# Converts a temperature in Celsius to Fahrenheit and Kelvin. Also determines
# whether it is a high temperature (>= 30°C).
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - Fahrenheit: <temp_f>
# - Kelvin: <temp_k>
# - High temperature: true|false
#
# Validations:
# - temp_c must be convertible to float
# - Kelvin result cannot be below 0.0
#
# Test cases:
# 1) Normal: temp_c = 25 → F=77, K=298.15, false
# 2) Border: temp_c = -273.15 → K=0.0
# 3) Error: temp_c = -300 → invalid (Kelvin < 0)
#
try:
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(is_high_temperature).lower())
except:
    print("Error: invalid input")


# ==================================================
# ===================== PROBLEM 2 ===================
# ===================================================
#
# Problem 2: Work hours and overtime payment
# Description:
# Calculates the weekly pay including overtime (above 40 hours).
#
# Inputs:
# - hours_worked (float)
# - hourly_rate (float)
#
# Outputs:
# - Regular pay:
# - Overtime pay:
# - Total pay:
# - Has overtime:
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: hours=45, rate=100 → reg=4000, ot=750, total=4750
# 2) Border: hours=40 → no overtime
# 3) Error: hours=-3 → invalid input
#
try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())
except:
    print("Error: invalid input")


# ==================================================
# ===================== PROBLEM 3 ===================
# ===================================================
#
# Problem 3: Discount eligibility with booleans
# Description:
# A client gets discount if:
# - is_student == true OR
# - is_senior == true OR
# - purchase_total >= 1000.0
#
# Inputs:
# - purchase_total (float)
# - is_student_text ("YES"/"NO")
# - is_senior_text ("YES"/"NO")
#
# Outputs:
# - Discount eligible: true|false
# - Final total:
#
# Validations:
# - purchase_total >= 0
# - student/senior text must be YES or NO
#
# Test cases:
# 1) Normal: 1200, NO, NO → eligible=true
# 2) Border: 999.99, YES → eligible=true
# 3) Error: student="MAYBE" → invalid
#
try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Is the customer a student? (YES/NO): ").upper()
    is_senior_text = input("Is the customer a senior? (YES/NO): ").upper()

    if purchase_total < 0:
        print("Error: invalid input")
    elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", final_total)
except:
    print("Error: invalid input")


# ==================================================
# ===================== PROBLEM 4 ===================
# ===================================================
#
# Problem 4: Basic statistics of three integers
# Description:
# Calculates sum, average, max, min and verifies whether all numbers are even.
#
# Inputs: n1, n2, n3 (int)
#
# Outputs:
# - Sum:
# - Average:
# - Max:
# - Min:
# - All even:
#
# Validations:
# - All must be integers
#
# Test cases:
# 1) Normal: 2,4,6 → all even
# 2) Border: -1,0,1
# 3) Error: n2="abc"
#
try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())
except:
    print("Error: invalid input")


# ==================================================
# ===================== PROBLEM 5 ===================
# ===================================================
#
# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# Determines loan eligibility using income, debt and credit score.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - Debt ratio:
# - Eligible:
#
# Validations:
# - monthly_income > 0
# - monthly_debt >= 0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: income=10000, debt=3000, score=700 → eligible
# 2) Border: income=8000, debt=3200 → ratio=0.4
# 3) Error: income=0 → invalid
#
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())
except:
    print("Error: invalid input")


# ==================================================
# ===================== PROBLEM 6 ===================
# ===================================================
#
# Problem 6: BMI and category flags
# Description:
# Calculates BMI and determines its category (underweight, normal, overweight).
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - BMI:
# - Underweight:
# - Normal:
# - Overweight:
#
# Validations:
# - weight > 0
# - height > 0
#
# Test cases:
# 1) Normal: 70kg, 1.75m → BMI=22.86 normal
# 2) Border: 50kg, 1.70m → underweight
# 3) Error: weight=-2 → invalid
#
try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = bmi >= 25.0

        print("BMI:", bmi_rounded)
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())
except:
    print("Error: invalid input")


# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Integers and floats allow precise numerical calculations together in real
# applications. Boolean values created through comparisons enable decision-
# making using logical conditions. Input validation ensures safety by preventing
# unexpected values, negative ranges or division by zero. Combining operators
# like and/or/not allows constructing complex conditions. These patterns repeat
# in payroll systems, discounts, loan evaluations and other real-world problems.
#
# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python Documentation – Built-in Types: Numeric Types
# 2) Python Documentation – Boolean Type (bool)
# 3) Python Operators – Arithmetic, Relational and Logical
# 4) Automate the Boring Stuff with Python – Chapter on Flow Control
# 5) Apuntes de clase – Validación de datos numéricos y manejo de errores
