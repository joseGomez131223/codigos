# =================================================================================
# File: 2430475_GomezJose_t_strings.py
# Name: jose gomez
# Matriculation: 2430048
# Group: IM1
# Course: Communication and Digital Skills
# Assignment: Strings practice (t_strings)
# =================================================================================

# =============================================================================
# EXECUTIVE SUMMARY (6-10 lines)
# =============================================================================
"""
This file contains six exercises to practice string handling in Python. A Python
string (type str) is an immutable sequence of characters. Operations covered
include normalization (strip, lower, title), slicing, concatenation, searching,
replacing and splitting/joining. Input validation is applied to avoid empty or
malformed inputs (for example, simple email structure checks). Each problem
includes a problem description, input and output specification, validations,
and three test cases (normal, border and error). The solutions emphasize the
use of built-in string methods and clear error messages.
"""
# =============================================================================

# =============================================================================
# GOOD PRACTICES (COMMENTS)
# =============================================================================
# - Strings are immutable: operations return new strings.
# - Normalize inputs with strip() and lower() before comparisons.
# - Avoid magic indices; document what each slice extracts.
# - Prefer built-in string methods (split, join, replace, startswith) over manual parsing.
# - Validate: first check empty after strip(), then check format.
# - Use descriptive variable names in lower_snake_case.
# =============================================================================

# =============================================================================
# PROBLEM TEMPLATE (APPEARS BEFORE EACH PROBLEM)
# =============================================================================
# Problem X: <short title>
# Description: 2-4 lines
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


# =================================================================================
# PROBLEM 1: Full name formatter (name + initials)
# =================================================================================
"""
Problem 1: Full name formatter (name + initials)
Description:
Given a full name string, normalize whitespace and case, return Title Case name
and initials separated by dots (e.g., J.C.T.).

Inputs:
- full_name (string)

Outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validations:
- full_name must not be empty after strip()
- must contain at least two words (name and surname)
- words should contain alphabetic characters at least (basic check)
"""

def format_full_name(full_name):
    if full_name is None:
        return "Error: invalid input"

    cleaned = full_name.strip()
    if cleaned == "":
        return "Error: invalid input"

    # split by whitespace (handles multiple spaces)
    parts = [p for p in cleaned.split() if p != ""]
    if len(parts) < 2:
        return "Error: invalid input"

    # simple alpha check for each part (allow hyphens or apostrophes optionally)
    for p in parts:
        # allow letters, hyphen and apostrophe
        if not all(ch.isalpha() or ch in ("-", "'") for ch in p):
            return "Error: invalid input"

    title_name = " ".join(p.capitalize() for p in parts)
    initials = ".".join(p[0].upper() for p in parts) + "."

    return {"Formatted name": title_name, "Initials": initials}

# Problem 1 Tests
print("\n--- Problem 1 Tests ---")
tests_p1 = [
    # Normal
    "juan carlos tovar",
    # Border: extra spaces and mixed case
    "   MARIA  del  ROSARIO  ",
    # Error: only one word
    "singleword"
]
for t in tests_p1:
    print("Input:", repr(t))
    print("Result:", format_full_name(t))


# =================================================================================
# PROBLEM 2: Simple email validator (structure + domain)
# =================================================================================
"""
Problem 2: Simple email validator
Description:
Performs a basic validation: single '@', at least one '.' after '@', no spaces.
If valid, return domain (part after '@').

Inputs:
- email_text (string)

Outputs:
- "Valid email: true" or "Valid email: false"
- If valid: "Domain: <domain_part>"

Validations:
- email_text not empty after strip()
- contains exactly one '@'
- no spaces in string
- after '@' there is at least one '.'
"""

def validate_email_simple(email_text):
    if email_text is None:
        return "Error: invalid input"

    s = email_text.strip()
    if s == "":
        return "Error: invalid input"

    if " " in s:
        return {"Valid email": False}

    if s.count("@") != 1:
        return {"Valid email": False}

    user, domain = s.split("@")
    if user == "" or domain == "":
        return {"Valid email": False}

    if "." not in domain:
        return {"Valid email": False}

    # all basic checks passed
    return {"Valid email": True, "Domain": domain}

# Problem 2 Tests
print("\n--- Problem 2 Tests ---")
tests_p2 = [
    # Normal
    "student@example.edu",
    # Border: short domain with dot
    "a@b.c",
    # Error: missing at
    "notanemail.com"
]
for t in tests_p2:
    print("Input:", repr(t))
    print("Result:", validate_email_simple(t))


# =================================================================================
# PROBLEM 3: Palindrome checker (ignoring spaces and case)
# =================================================================================
"""
Problem 3: Palindrome checker
Description:
Check whether a phrase is a palindrome ignoring spaces and case. Optionally show
the normalized version.

Inputs:
- phrase (string)

Outputs:
- "Is palindrome: true" or "Is palindrome: false"
- "Normalized:" <normalized_string> (optional)

Validations:
- phrase not empty after strip()
- normalized length should be >= 3 (reasonable minimum)
"""

def is_palindrome_ignore_spaces(phrase):
    if phrase is None:
        return "Error: invalid input"

    s = phrase.strip()
    if s == "":
        return "Error: invalid input"

    # normalize: keep only alphanumeric characters to be nicer (remove punctuation)
    normalized = "".join(ch.lower() for ch in s if ch.isalnum())
    if len(normalized) < 3:
        return "Error: invalid input"

    result = normalized == normalized[::-1]
    return {"Is palindrome": result, "Normalized": normalized}

# Problem 3 Tests
print("\n--- Problem 3 Tests ---")
tests_p3 = [
    # Normal
    "Anita lava la tina",
    # Border: short but palindrome
    "aba",
    # Error: too short after cleaning
    "  a  "
]
for t in tests_p3:
    print("Input:", repr(t))
    print("Result:", is_palindrome_ignore_spaces(t))


# =================================================================================
# PROBLEM 4: Sentence word stats (lengths and first/last word)
# =================================================================================
"""
Problem 4: Sentence word stats
Description:
Normalize sentence, split words and provide word count, first/last word, shortest
and longest (by length).

Inputs:
- sentence (string)

Outputs:
- "Word count:", "First word:", "Last word:", "Shortest word:", "Longest word:"

Validations:
- sentence not empty after strip()
- must contain at least one word after split()
"""

def sentence_word_stats(sentence):
    if sentence is None:
        return "Error: invalid input"

    s = sentence.strip()
    if s == "":
        return "Error: invalid input"

    # split by whitespace, remove any empty tokens
    words = [w for w in s.split() if w != ""]
    if len(words) == 0:
        return "Error: invalid input"

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    # shortest and longest by length (if tie, first occurrence)
    shortest = min(words, key=len)
    longest = max(words, key=len)

    return {
        "Word count": word_count,
        "First word": first_word,
        "Last word": last_word,
        "Shortest word": shortest,
        "Longest word": longest
    }

# Problem 4 Tests
print("\n--- Problem 4 Tests ---")
tests_p4 = [
    # Normal
    "  This is a sample sentence for testing  ",
    # Border: single word
    "hello",
    # Error: empty
    "   "
]
for t in tests_p4:
    print("Input:", repr(t))
    print("Result:", sentence_word_stats(t))


# =================================================================================
# PROBLEM 5: Password strength classifier
# =================================================================================
"""
Problem 5: Password strength classifier
Description:
Classify password as weak, medium or strong.
Rules used (documented):
- If length < 8 -> weak
- Else:
  - strong if has_upper and has_lower and has_digit and has_symbol
  - medium if at least two of the above three classes present (upper/lower/digit),
    or length >= 8 with some complexity
- We treat symbols as non-alphanumeric characters.

Inputs:
- password_input (string)

Outputs:
- "Password strength: weak" / "medium" / "strong"

Validations:
- password_input not empty
"""

def classify_password_strength(password_input):
    if password_input is None:
        return "Error: invalid input"

    p = password_input
    if p.strip() == "":
        return "Error: invalid input"

    length = len(p)
    has_upper = any(ch.isupper() for ch in p)
    has_lower = any(ch.islower() for ch in p)
    has_digit = any(ch.isdigit() for ch in p)
    has_symbol = any(not ch.isalnum() for ch in p)

    if length < 8:
        return {"Password strength": "weak"}

    # strong: all four categories present
    if has_upper and has_lower and has_digit and has_symbol:
        return {"Password strength": "strong"}

    # medium: length >=8 and at least two of upper/lower/digit or contains symbol + one more
    categories = sum([has_upper, has_lower, has_digit])
    if categories >= 2 or (has_symbol and categories >= 1):
        return {"Password strength": "medium"}

    return {"Password strength": "weak"}

# Problem 5 Tests
print("\n--- Problem 5 Tests ---")
tests_p5 = [
    # Normal (strong)
    "Abcdef1!",
    # Border (length 8 but missing symbol)
    "Abcdef12",
    # Error (empty)
    "   "
]
for t in tests_p5:
    print("Input:", repr(t))
    print("Result:", classify_password_strength(t))


# =================================================================================
# PROBLEM 6: Product label formatter (fixed-width text)
# =================================================================================
"""
Problem 6: Product label formatter (fixed-width text)
Description:
Given product_name and price_value, produce a single-line label:
"Product: <NAME> | Price: $<PRICE>" that is exactly 30 characters.
If shorter -> pad spaces at end; if longer -> truncate to 30 chars.

Inputs:
- product_name (string)
- price_value (string or number)

Outputs:
- "Label: <30-char-string>"

Validations:
- product_name not empty after strip()
- price_value convertible to positive float (>= 0)
"""

def format_product_label(product_name, price_value):
    if product_name is None or price_value is None:
        return "Error: invalid input"

    name = product_name.strip()
    if name == "":
        return "Error: invalid input"

    # try to parse price
    try:
        price_f = float(price_value)
    except:
        return "Error: invalid input"

    if price_f < 0:
        return "Error: invalid input"

    # Format price to 2 decimals
    price_str = f"{price_f:.2f}"

    base_label = f"Product: {name} | Price: ${price_str}"
    # Ensure exactly 30 chars
    if len(base_label) < 30:
        label = base_label + " " * (30 - len(base_label))
    else:
        label = base_label[:30]

    return {"Label": label}

# Problem 6 Tests
print("\n--- Problem 6 Tests ---")
tests_p6 = [
    # Normal
    ("Soap", 12.5),
    # Border: long name that requires truncation
    ("ExtraLargeMultiPurposeCleaningSoapPack", 123.456),
    # Error: invalid price
    ("Shampoo", "free")
]
for t in tests_p6:
    print("Input:", t)
    print("Result:", format_product_label(*t))


# =================================================================================
# CONCLUSIONS (5-8 lines) - comments
# =================================================================================
"""
Conclusions:
- Strings are immutable; operations return new strings. Normalizing inputs
  (strip() and lower()/title()) avoids many comparison errors.
- Methods like split(), join(), replace(), startswith() and slicing make text
  processing concise and readable.
- Validations should check emptiness first, then format (for example, email or
  numeric conversion for price).
- Designing clear test cases (normal, border, error) helps ensure robustness.
- Slices and built-in functions reduce the chance of bugs compared to manual parsing.
"""
# =================================================================================

# =================================================================================
# REFERENCES (minimum 5) - comments
# =================================================================================
# References:
# 1) Python documentation - Text Sequence Type — str
# 2) Python documentation - Built-in Functions (len, str methods)
# 3) Real Python - "Working with Strings in Python"
# 4) Automate the Boring Stuff with Python - "Strings"
# 5) Official course notes and slides on input validation and string manipulation
# =================================================================================
