# Counter for temporary variables and labels
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

# Function to generate TAC for expressions
def generate_expression_tac(expression):
    tokens = expression.split()  # Basic split based on spaces
    if len(tokens) == 5 and tokens[1] == "=" and tokens[3] in ["+", "-", "*", "/"]:
        # Example: x = a + b
        left_var = tokens[0]
        op1 = tokens[2]
        operator = tokens[3]
        op2 = tokens[4]
        
        if operator == "*":
            temp = new_temp()
            print(f"{temp} = {op1} * {op2}")
            print(f"{left_var} = {temp}")
        elif operator == "+":
            temp = new_temp()
            print(f"{temp} = {op1} + {op2}")
            print(f"{left_var} = {temp}")
        # Add more operators as needed
    else:
        print("Expression format not recognized")

# Function to generate TAC for if-else statements
def generate_if_else_tac(condition, true_block, false_block):
    label_true = new_label()
    label_false = new_label()
    label_end = new_label()

    print(f"if {condition} goto {label_true}")
    print(f"goto {label_false}")

    print(f"{label_true}:")
    for statement in true_block:
        generate_expression_tac(statement)
    print(f"goto {label_end}")

    print(f"{label_false}:")
    for statement in false_block:
        generate_expression_tac(statement)

    print(f"{label_end}:")

# Function to generate TAC for method calls
def generate_method_call_tac(method_name, params, result_var):
    for param in params:
        print(f"param {param}")
    temp = new_temp()
    print(f"{temp} = call {method_name}, {len(params)}")
    print(f"{result_var} = {temp}")

# Sample usage
print("TAC for expression 'x = a + b * c':")
generate_expression_tac("x = a + b * c")

print("\nTAC for if-else statement:")
generate_if_else_tac("a > b", ["x = x + 1"], ["x = x - 1"])

print("\nTAC for method call 'result = add(a, b)':")
generate_method_call_tac("add", ["a", "b"], "result")
