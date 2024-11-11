# Temporary variable and label counters
temp_counter = 0
label_counter = 0

def new_temp():
    global temp_counter
    temp = f"t{temp_counter}"
    temp_counter += 1
    return temp

def new_label():
    global label_counter
    label = f"L{label_counter}"
    label_counter += 1
    return label

# Function to handle assignment statements
def handle_assign():
    var_name = input("Enter variable name: ")
    left_operand = input("Enter left operand: ")
    operator = input("Enter operator (+, -, *, /, etc.): ")
    right_operand = input("Enter right operand: ")
    
    temp = new_temp()
    print(f"{temp} = {left_operand} {operator} {right_operand}")
    print(f"{var_name} = {temp}")

# Function to handle if-else statements
def handle_if_else():
    left_operand = input("Enter left operand of condition: ")
    comparison_operator = input("Enter comparison operator (==, !=, >, <, etc.): ")
    right_operand = input("Enter right operand of condition: ")
    
    label_true = new_label()
    label_false = new_label()
    label_end = new_label()

    print(f"if {left_operand} {comparison_operator} {right_operand} goto {label_true}")
    print(f"goto {label_false}")
    
    print(f"{label_true}:")
    while True:
        statement = input("Enter statement for the 'true' block (or 'done' to finish): ")
        if statement.lower() == "done":
            break
        handle_assign()
    print(f"goto {label_end}")
    
    print(f"{label_false}:")
    has_else = input("Do you want an 'else' block? (yes/no): ")
    if has_else.lower() == "yes":
        while True:
            statement = input("Enter statement for the 'false' block (or 'done' to finish): ")
            if statement.lower() == "done":
                break
            handle_assign()
    print(f"{label_end}:")

# Function to handle while loops
def handle_while():
    left_operand = input("Enter left operand of condition: ")
    comparison_operator = input("Enter comparison operator (==, !=, >, <, etc.): ")
    right_operand = input("Enter right operand of condition: ")

    label_start = new_label()
    label_end = new_label()

    print(f"{label_start}:")
    print(f"if not {left_operand} {comparison_operator} {right_operand} goto {label_end}")
    
    while True:
        statement = input("Enter statement for the 'while' loop body (or 'done' to finish): ")
        if statement.lower() == "done":
            break
        handle_assign()
    
    print(f"goto {label_start}")
    print(f"{label_end}:")

# Function to handle function calls
def handle_call():
    function_name = input("Enter function name: ")
    arguments = input("Enter arguments separated by commas: ").split(',')
    for arg in arguments:
        print(f"param {arg.strip()}")
    temp = new_temp()
    print(f"{temp} = call {function_name}, {len(arguments)}")

# Main loop to interactively create TAC for Zara code
def main():
    print("Three-Address Code (TAC) Generator for Zara Code")
    while True:
        statement_type = input("Enter statement type (assign, if, while, call, or 'done' to finish): ")
        
        if statement_type == "assign":
            handle_assign()
        elif statement_type == "if":
            handle_if_else()
        elif statement_type == "while":
            handle_while()
        elif statement_type == "call":
            handle_call()
        elif statement_type == "done":
            print("TAC generation completed.")
            break
        else:
            print("Unknown statement type. Please enter 'assign', 'if', 'while', 'call', or 'done'.")

# Run the main program
if __name__ == "__main__":
    main()
