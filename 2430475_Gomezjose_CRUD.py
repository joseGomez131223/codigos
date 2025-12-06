# =============================================================================
# Name: Gomez Rodriguez JOse de Jesus
# Matriculation: 2430475
# Group: IM1
# Course: Metodologia a la programacion 
# Assignment: In-memory CRUD manager with functions
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY (5-8 lines)
# =============================================================================
"""
This program implements a simple in-memory CRUD manager for items (e.g. inventory
products). CRUD stands for Create, Read, Update and Delete. The implementation
uses a dictionary as the main data structure (item_id -> item_dict) for O(1)
lookups and straightforward updates. Each CRUD operation is encapsulated in a
function, and a menu-driven main loop delegates work to those functions. Input
validation prevents invalid IDs and numeric fields, and three test cases
(normal, border and error) are provided and executed when running the test mode.
"""
# =============================================================================

# =============================================================================
# DESIGN DECISION
# =============================================================================
# Data structure choice: Option A (dictionary)
# Reason: A dict mapping item_id -> { "name": ..., "price": ..., "quantity": ... }
# provides fast lookup, easy update/delete by id and simple existence checks.
#
# All messages and identifiers are in English. Functions use lower_snake_case.
# =============================================================================

# =============================================================================
# PROBLEM: In-memory CRUD manager with functions
# Description:
#   Program that implements Create, Read, Update, Delete operations for items
#   stored in memory using a dictionary. Each operation is implemented as a
#   separate function. A text menu allows the user to interact with the system.
#
# Inputs:
#   - Menu option (int)
#   - For CREATE/UPDATE: item_id (string), name (string), price (float), quantity (int)
#   - For READ/DELETE: item_id (string)
#
# Outputs:
#   - "Item created"
#   - "Item updated"
#   - "Item deleted"
#   - "Item not found"
#   - "Items list:" (followed by item representations)
#   - "Error: invalid input"
#
# Validations:
#   - option must be integer in valid range
#   - item_id must not be empty after strip()
#   - price must be float >= 0.0
#   - quantity must be int >= 0
#   - create disallows duplicate id (policy: do not allow duplicates)
#   - read/update/delete must report "Item not found" if id absent
#
# Test cases:
# 1) Normal: create item 'p1', read it, update it, delete it -> final not found
# 2) Border: create item with quantity = 0 and price = 0.0 -> allowed
# 3) Error: attempt to create with empty id or non-numeric price -> error messages
# =============================================================================

# =============================================================================
# CONSTANTS
# =============================================================================
EXIT_OPTION = 0
CREATE_OPTION = 1
READ_OPTION = 2
UPDATE_OPTION = 3
DELETE_OPTION = 4
LIST_OPTION = 5
TESTS_OPTION = 9  # hidden option to run automated tests

# =============================================================================
# CRUD FUNCTIONS (operate on data_structure which is a dict)
# =============================================================================

def validate_item_fields(item_id, name, price, quantity):
    """
    Validate fields for create/update.
    Returns (True, cleaned_item) or (False, "Error: invalid input")
    cleaned_item: (item_id_str, name_str, price_float, quantity_int)
    """
    if item_id is None or str(item_id).strip() == "":
        return False, "Error: invalid input"
    item_id_str = str(item_id).strip()

    if name is None or str(name).strip() == "":
        return False, "Error: invalid input"
    name_str = str(name).strip()

    try:
        price_f = float(price)
    except:
        return False, "Error: invalid input"
    if price_f < 0.0:
        return False, "Error: invalid input"

    try:
        quantity_i = int(quantity)
    except:
        return False, "Error: invalid input"
    if quantity_i < 0:
        return False, "Error: invalid input"

    return True, (item_id_str, name_str, price_f, quantity_i)


def create_item(data_structure, item_id, name, price, quantity):
    """
    Create a new item in the data_structure (dict).
    Policy: do not allow duplicate ids.
    Returns: ("Item created", item_dict) on success or ("Error: ...", None)
    """
    ok, res = validate_item_fields(item_id, name, price, quantity)
    if not ok:
        return res, None

    item_id_str, name_str, price_f, quantity_i = res

    if item_id_str in data_structure:
        return "Error: invalid input"  # ID already exists considered invalid per spec
    # create
    item = {"id": item_id_str, "name": name_str, "price": price_f, "quantity": quantity_i}
    data_structure[item_id_str] = item
    return "Item created", item


def read_item(data_structure, item_id):
    """
    Return the item dict if found, otherwise return ("Item not found", None)
    """
    if item_id is None or str(item_id).strip() == "":
        return "Error: invalid input", None
    item_id_str = str(item_id).strip()
    if item_id_str not in data_structure:
        return "Item not found", None
    return "Item found", data_structure[item_id_str]


def update_item(data_structure, item_id, new_name=None, new_price=None, new_quantity=None):
    """
    Update fields of an existing item. Only non-None fields will be updated.
    Validation applies to provided fields. Returns ("Item updated", item) or error.
    """
    if item_id is None or str(item_id).strip() == "":
        return "Error: invalid input", None
    item_id_str = str(item_id).strip()
    if item_id_str not in data_structure:
        return "Item not found", None

    current = data_structure[item_id_str].copy()

    # Prepare values: if None -> keep current; else validate individually
    if new_name is not None:
        if str(new_name).strip() == "":
            return "Error: invalid input", None
        current["name"] = str(new_name).strip()

    if new_price is not None:
        try:
            price_f = float(new_price)
        except:
            return "Error: invalid input", None
        if price_f < 0.0:
            return "Error: invalid input", None
        current["price"] = price_f

    if new_quantity is not None:
        try:
            quantity_i = int(new_quantity)
        except:
            return "Error: invalid input", None
        if quantity_i < 0:
            return "Error: invalid input", None
        current["quantity"] = quantity_i

    # commit update
    data_structure[item_id_str] = current
    return "Item updated", current


def delete_item(data_structure, item_id):
    """
    Delete item by id. Returns ("Item deleted", item) or ("Item not found", None)
    """
    if item_id is None or str(item_id).strip() == "":
        return "Error: invalid input", None
    item_id_str = str(item_id).strip()
    if item_id_str not in data_structure:
        return "Item not found", None
    removed = data_structure.pop(item_id_str)
    return "Item deleted", removed


def list_items(data_structure):
    """
    Return a list of item dicts (copy) to avoid exposing internal structure.
    """
    return list(data_structure.values())


# =============================================================================
# HELPER: pretty print for items
# =============================================================================
def print_item(item):
    print(f" - id: {item['id']}, name: {item['name']}, price: {item['price']:.2f}, quantity: {item['quantity']}")


def print_items_list(items):
    if not items:
        print("Items list: (empty)")
        return
    print("Items list:")
    for it in items:
        print_item(it)


# =============================================================================
# MAIN MENU HANDLING
# =============================================================================
def show_menu():
    print("\nMenu:")
    print(f"{CREATE_OPTION}) Create item")
    print(f"{READ_OPTION}) Read item by id")
    print(f"{UPDATE_OPTION}) Update item by id")
    print(f"{DELETE_OPTION}) Delete item by id")
    print(f"{LIST_OPTION}) List all items")
    print(f"{EXIT_OPTION}) Exit")
    # hidden test option
    print(f"{TESTS_OPTION}) Run automated tests (demo) [hidden]")


def input_prompt(prompt_text):
    try:
        return input(prompt_text)
    except EOFError:
        # For non-interactive environments
        return ""


def main_loop():
    """
    Runs an interactive menu loop until user chooses EXIT_OPTION.
    """
    # main data structure: dict id -> item dict
    data = {}
    while True:
        show_menu()
        option_raw = input_prompt("Choose an option: ").strip()
        try:
            option = int(option_raw)
        except:
            print("Error: invalid input")
            continue

        if option == EXIT_OPTION:
            print("Bye!")
            break

        elif option == CREATE_OPTION:
            item_id = input_prompt("Enter item id: ")
            name = input_prompt("Enter name: ")
            price = input_prompt("Enter price: ")
            quantity = input_prompt("Enter quantity: ")
            message, item = create_item(data, item_id, name, price, quantity)
            print(message)

        elif option == READ_OPTION:
            item_id = input_prompt("Enter item id: ")
            message, item = read_item(data, item_id)
            if item is None:
                print(message)
            else:
                print("Item found:")
                print_item(item)

        elif option == UPDATE_OPTION:
            item_id = input_prompt("Enter item id: ")
            # ask which fields to change - if left blank, keep current
            print("Leave field blank to keep current value.")
            new_name = input_prompt("New name: ")
            new_name = new_name if new_name.strip() != "" else None
            new_price = input_prompt("New price: ")
            new_price = new_price if new_price.strip() != "" else None
            new_quantity = input_prompt("New quantity: ")
            new_quantity = new_quantity if new_quantity.strip() != "" else None

            message, item = update_item(data, item_id, new_name, new_price, new_quantity)
            print(message)

        elif option == DELETE_OPTION:
            item_id = input_prompt("Enter item id: ")
            message, item = delete_item(data, item_id)
            print(message)

        elif option == LIST_OPTION:
            items = list_items(data)
            print_items_list(items)

        elif option == TESTS_OPTION:
            run_test_cases()
        else:
            print("Error: invalid input")


# =============================================================================
# TESTS: Three test cases (normal, border, error) - executed by run_test_cases()
# =============================================================================
def run_test_cases():
    """
    Run the three required test cases (normal, border, error) and print outcomes.
    This function demonstrates expected messages and final state.
    """
    print("\n--- Running automated test cases ---")
    data = {}

    # Test 1: Normal flow - create, read, update, delete
    print("\nTest 1 (Normal): create -> read -> update -> delete")
    msg, _ = create_item(data, "p1", "Widget", 9.99, 10)
    print("create:", msg)  # expect Item created
    msg, item = read_item(data, "p1")
    print("read:", msg, "->", item)
    msg, _ = update_item(data, "p1", new_name="WidgetPro", new_price=12.5, new_quantity=5)
    print("update:", msg)
    msg, item = read_item(data, "p1")
    print("read after update:", msg, "->", item)
    msg, _ = delete_item(data, "p1")
    print("delete:", msg)
    msg, _ = read_item(data, "p1")
    print("read after delete:", msg)  # expect Item not found

    # Test 2: Border case - minimal valid data (quantity = 0, price = 0.0)
    print("\nTest 2 (Border): create item with price=0.0 and quantity=0")
    msg, _ = create_item(data, "p2", "FreeSample", 0.0, 0)
    print("create:", msg)
    items = list_items(data)
    print_items_list(items)
    # cleanup
    delete_item(data, "p2")

    # Test 3: Error cases - invalid id, invalid price
    print("\nTest 3 (Error): create with empty id and create with non-numeric price")
    msg, _ = create_item(data, "", "NoId", 1.0, 1)
    print("create with empty id:", msg)  # expect Error: invalid input
    msg, _ = create_item(data, "p3", "BadPrice", "not_a_number", 1)
    print("create with bad price:", msg)  # expect Error: invalid input

    print("\n--- Automated tests finished ---\n")


# =============================================================================
# CONCLUSIONS (5-8 lines) - comments
# =============================================================================
"""
Conclusions:
- Using a dictionary for in-memory CRUD provides efficient lookup, update and delete by id.
- Separating each operation into functions keeps the main loop concise and improves testability.
- Input validation was essential to avoid invalid states (empty ids, negative prices/quantities).
- To extend this CRUD, data persistence (files or a database) and input sanitization could be added.
- The test function demonstrates normal, border and error behaviors to validate requirements.
"""
# =============================================================================

# =============================================================================
# REFERENCES (minimum 3) - comments
# =============================================================================
# References:
# 1) Python documentation - Data structures: https://docs.python.org/3/tutorial/datastructures.html
# 2) Python documentation - Defining functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 3) Real Python - "Python Dictionaries" (guide)
# =============================================================================

# =============================================================================
# ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    # Run interactive main loop
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nBye!")
