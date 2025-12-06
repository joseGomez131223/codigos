# =============================================================================
# PORTADA / COVER
# =============================================================================
# Name: Gomez Rodriguez Jose de Jesus
# Matriculation: 2430475
# Group: IM1
# Course: Communication and Digital Skills
# Assignment: Collections in Python (lists, tuples, dicts)
# =============================================================================


# =============================================================================
# EXECUTIVE SUMMARY (6-10 lines)
# =============================================================================
"""
This document practices collections in Python: lists, tuples and dictionaries.
Lists are ordered, mutable collections for items that change often. Tuples are
ordered, immutable collections suited for fixed records like coordinates. 
Dictionaries map keys to values for fast lookups and structured records. This
file contains six problems that demonstrate creation, access, insertion,
deletion, search, aggregation and simple CRUD operations using these
collections. Each problem includes description, inputs, outputs, validations,
and three test cases (normal, border, error).
"""
# =============================================================================


# =============================================================================
# GOOD PRACTICES (COMMENTS)
# =============================================================================
# - Use lists when you need to add/remove items frequently.
# - Use tuples for data that must not change (coordinates, constants).
# - Use dicts for key-based lookups (name -> record).
# - Avoid modifying a list while iterating; instead iterate over a copy or build a new list.
# - Use descriptive variable names in lower_snake_case.
# - Validate inputs before using indexes or performing arithmetic.
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
# PROBLEM 1: Shopping list basics (list operations)
# ============================================================
"""
Description:
Manage a shopping list where items are strings. Create an initial list from a
comma-separated string, append a new item, count items, and check existence.

Inputs:
- initial_items_text (string), e.g. "apple,banana,orange"
- new_item (string)
- search_item (string)

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text must not be empty after strip() (empty allowed if user wants; here we treat empty as empty list).
- new_item and search_item must not be empty after strip().
- Trim whitespace around items.
"""

def shopping_list_operations(initial_items_text: str, new_item: str, search_item: str):
    # Validate inputs
    if initial_items_text is None:
        return "Error: invalid input"
    if new_item is None or search_item is None:
        return "Error: invalid input"

    initial_items_text = initial_items_text.strip()
    # If empty string, start with empty list
    if initial_items_text == "":
        items_list = []
    else:
        # split and strip whitespace from each item, ignore empty tokens
        items_list = [it.strip() for it in initial_items_text.split(",") if it.strip() != ""]

    if new_item.strip() == "" or search_item.strip() == "":
        return "Error: invalid input"

    items_list.append(new_item.strip())
    len_list = len(items_list)
    found = (search_item.strip() in items_list)

    # Outputs
    return {
        "Items list": items_list,
        "Total items": len_list,
        "Found item": found
    }

# --- Problem 1 Tests ---
print("\n--- Problem 1 Tests ---")
tests_p1 = [
    # Normal
    ("apple,banana,orange", "grapes", "banana"),
    # Border: empty initial list
    ("   ", "milk", "milk"),
    # Error: new_item empty
    ("apple,pear", "   ", "pear")
]
for t in tests_p1:
    result = shopping_list_operations(*t)
    print("Input:", t)
    print("Result:", result)


# ============================================================
# PROBLEM 2: Points and distances with tuples
# ============================================================
"""
Description:
Use tuples to store two 2D points, compute Euclidean distance and the midpoint.

Inputs:
- x1, y1, x2, y2 (floats)

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance> (float)
- "Midpoint:" (mx, my) (tuple)

Validations:
- All inputs must be convertible to float.
"""

def points_distance_midpoint(x1, y1, x2, y2):
    try:
        x1_f = float(x1)
        y1_f = float(y1)
        x2_f = float(x2)
        y2_f = float(y2)
    except:
        return "Error: invalid input"

    point_a = (x1_f, y1_f)
    point_b = (x2_f, y2_f)
    distance = ((x2_f - x1_f)**2 + (y2_f - y1_f)**2) ** 0.5
    midpoint = ((x1_f + x2_f)/2, (y1_f + y2_f)/2)

    return {
        "Point A": point_a,
        "Point B": point_b,
        "Distance": distance,
        "Midpoint": midpoint
    }

# --- Problem 2 Tests ---
print("\n--- Problem 2 Tests ---")
tests_p2 = [
    # Normal
    (0, 0, 3, 4),
    # Border: same point (distance 0)
    (1.5, 2.5, 1.5, 2.5),
    # Error: non-numeric
    ("a", 0, 1, 2)
]
for t in tests_p2:
    print("Input:", t)
    print("Result:", points_distance_midpoint(*t))


# ============================================================
# PROBLEM 3: Product catalog with dictionary
# ============================================================
"""
Description:
Manage a small product catalog (dict: product_name -> unit_price).
Read a product name and quantity, compute total if product exists.

Inputs:
- product_name (string)
- quantity (int)

Outputs:
- If exists:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- If not exists:
  - "Error: product not found"

Validations:
- product_name not empty after strip()
- quantity must be integer > 0
"""

def product_catalog_checkout(product_name: str, quantity):
    # Sample initial catalog
    product_prices = {
        "apple": 10.0,
        "banana": 5.0,
        "orange": 8.0,
        "milk": 20.0
    }

    if product_name is None:
        return "Error: invalid input"
    product_name_clean = product_name.strip()
    if product_name_clean == "":
        return "Error: invalid input"

    try:
        qty = int(quantity)
    except:
        return "Error: invalid input"

    if qty <= 0:
        return "Error: invalid input"

    if product_name_clean not in product_prices:
        return "Error: product not found"

    unit_price = product_prices[product_name_clean]
    total_price = unit_price * qty

    return {
        "Unit price": unit_price,
        "Quantity": qty,
        "Total": total_price
    }

# --- Problem 3 Tests ---
print("\n--- Problem 3 Tests ---")
tests_p3 = [
    # Normal
    ("apple", 3),
    # Border: quantity = 1
    ("banana", 1),
    # Error: product not found
    ("chocolate", 2),
]
for t in tests_p3:
    print("Input:", t)
    print("Result:", product_catalog_checkout(*t))


# ============================================================
# PROBLEM 4: Student grades with dict and list
# ============================================================
"""
Description:
Manage student grades with a dictionary: student_name -> list_of_grades.
Compute average and passed flag (average >= 70.0).

Inputs:
- student_name (string)

Outputs:
- If exists:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- If not exists:
  - "Error: student not found"

Validations:
- student_name not empty after strip()
- grade list must not be empty
"""

def student_average_and_passed(student_name: str):
    # Sample students data
    grades_db = {
        "Alice": [90.0, 85.0, 78.0],
        "Bob": [60.0, 70.0, 65.0],
        "Charlie": [100.0, 95.0]
    }

    if student_name is None:
        return "Error: invalid input"
    name_clean = student_name.strip()
    if name_clean == "":
        return "Error: invalid input"

    if name_clean not in grades_db:
        return "Error: student not found"

    grades_list = grades_db[name_clean]
    if len(grades_list) == 0:
        return "Error: invalid input"

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0

    return {
        "Grades": grades_list,
        "Average": average,
        "Passed": is_passed
    }

# --- Problem 4 Tests ---
print("\n--- Problem 4 Tests ---")
tests_p4 = [
    # Normal
    ("Alice",),
    # Border: average exactly 70 (Bob -> 65+70+60 = 195/3 = 65 -> not passed; to show border, we add another student)
    ("Bob",),
    # Error: student not found
    ("Daniel",)
]
for t in tests_p4:
    print("Input:", t)
    print("Result:", student_average_and_passed(*t))


# ============================================================
# PROBLEM 5: Word frequency counter (list + dict)
# ============================================================
"""
Description:
Count frequency of each word in a sentence (case-insensitive). Return words
list, frequency dictionary and most common word.

Inputs:
- sentence (string)

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validations:
- sentence not empty after strip()
- handle simple punctuation by removing . , ? ! ; : characters
"""

import string

def word_frequency_counter(sentence: str):
    if sentence is None:
        return "Error: invalid input"
    sentence_clean = sentence.strip()
    if sentence_clean == "":
        return "Error: invalid input"

    # Simple punctuation removal (for basic handling)
    for ch in ".,?!;:":
        sentence_clean = sentence_clean.replace(ch, "")

    words_list = sentence_clean.lower().split()
    if len(words_list) == 0:
        return "Error: invalid input"

    freq_dict = {}
    for w in words_list:
        if w in freq_dict:
            freq_dict[w] += 1
        else:
            freq_dict[w] = 1

    # Find most common word (if tie, any one is fine)
    most_common_word = max(freq_dict, key=lambda k: freq_dict[k])

    return {
        "Words list": words_list,
        "Frequencies": freq_dict,
        "Most common word": most_common_word
    }

# --- Problem 5 Tests ---
print("\n--- Problem 5 Tests ---")
tests_p5 = [
    # Normal
    ("This is a test. This test is simple."),
    # Border: single word repeated
    ("hello hello hello"),
    # Error: empty sentence
    ("   ")
]
for t in tests_p5:
    print("Input:", repr(t))
    print("Result:", word_frequency_counter(t))


# ============================================================
# PROBLEM 6: Simple contact book (dictionary CRUD)
# ============================================================
"""
Description:
Implement a small contact book with actions: ADD, SEARCH, DELETE.

#Inputs:
- action_text ("ADD", "SEARCH", "DELETE") - case-insensitive
- name (string)
- phone (string) - only for ADD

#Outputs:
- ADD:
  - "Contact saved:" name, phone
- SEARCH:
  - If exists: "Phone:" <phone>
  - Else: "Error: contact not found"
- DELETE:
  - If exists: "Contact deleted:" name
  - Else: "Error: contact not found"

#Validations:
- action_text must be one of ADD, SEARCH, DELETE
- name must not be empt
"""