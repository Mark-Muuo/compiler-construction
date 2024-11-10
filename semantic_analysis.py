class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # List of dictionaries representing scopes

    def enter_scope(self):
        """Enter a new scope."""
        self.scopes.append({})

    def exit_scope(self):
        """Exit the current scope."""
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise Exception("Cannot exit global scope")

    def declare_variable(self, name, var_type):
        """Declare a variable in the current scope."""
        current_scope = self.scopes[-1]
        if name in current_scope:
            raise Exception(f"Variable '{name}' already declared in the current scope.")
        current_scope[name] = var_type

    def get_variable_type(self, name):
        """Retrieve the type of a variable, searching from the innermost to outermost scope."""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' not declared in any accessible scope.")

class FunctionTable:
    def __init__(self):
        self.functions = {}

    def declare_function(self, name, param_types, return_type):
        """Declare a function with parameter types and a return type."""
        if name in self.functions:
            raise Exception(f"Function '{name}' already declared.")
        self.functions[name] = {
            "params": param_types,
            "return": return_type
        }

    def get_function_signature(self, name):
        """Retrieve the function signature (parameter types and return type)."""
        if name not in self.functions:
            raise Exception(f"Function '{name}' not declared.")
        return self.functions[name]

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.function_table = FunctionTable()

    def analyze_variable_declaration(self, name, var_type):
        """Analyze variable declaration."""
        self.symbol_table.declare_variable(name, var_type)

    def analyze_assignment(self, var_name, expr_type):
        """Analyze assignment to ensure type consistency."""
        var_type = self.symbol_table.get_variable_type(var_name)
        if var_type != expr_type:
            raise Exception(f"Type error in assignment: Variable '{var_name}' is of type '{var_type}', cannot assign '{expr_type}'.")

    def analyze_array_assignment(self, array_name, element_type):
        """Analyze array assignment to ensure element type consistency."""
        array_type = self.symbol_table.get_variable_type(array_name)
        expected_array_type = f"array[{element_type}]"
        if array_type != expected_array_type:
            raise Exception(f"Type error: '{array_name}' should be of type '{expected_array_type}', got '{array_type}'.")

    def analyze_stack_operation(self, stack_name, element_type, operation):
        """Analyze stack operation (e.g., push/pop) for type consistency."""
        stack_type = self.symbol_table.get_variable_type(stack_name)
        expected_stack_type = f"stack[{element_type}]"
        if stack_type != expected_stack_type:
            raise Exception(f"Type error in stack '{operation}': '{stack_name}' should be of type '{expected_stack_type}', got '{stack_type}'.")

    def analyze_scope(self, statements):
        """Analyze a series of statements within a scope."""
        self.symbol_table.enter_scope()
        try:
            for statement in statements:
                statement()  # Execute each statement
        finally:
            self.symbol_table.exit_scope()

    def analyze_function_declaration(self, name, param_types, return_type):
        """Analyze function declaration with parameter and return types."""
        self.function_table.declare_function(name, param_types, return_type)

    def analyze_function_call(self, name, arg_types):
        """Analyze function call to ensure argument type matching."""
        func = self.function_table.get_function_signature(name)
        param_types = func["params"]
        if len(arg_types) != len(param_types):
            raise Exception(f"Function '{name}' expects {len(param_types)} arguments, got {len(arg_types)}.")
        for i, (arg_type, param_type) in enumerate(zip(arg_types, param_types)):
            if arg_type != param_type:
                raise Exception(f"Type error in function call '{name}': Argument {i+1} expected '{param_type}', got '{arg_type}'.")

    def analyze_return(self, return_type, expected_type):
        """Analyze return statement to ensure type consistency."""
        if return_type != expected_type:
            raise Exception(f"Return type mismatch: Expected '{expected_type}', got '{return_type}'.")

# Testing the Semantic Analyzer with Zara code examples

def test_semantic_analyzer():
    analyzer = SemanticAnalyzer()

    try:
        # Test variable declarations and assignments
        analyzer.analyze_variable_declaration("a", "int")
        analyzer.analyze_variable_declaration("b", "float")
        analyzer.analyze_assignment("a", "int")  # Correct assignment
        try:
            analyzer.analyze_assignment("a", "float")  # Type mismatch
        except Exception as e:
            print(e)

        # Test scope rules
        def inner_scope():
            analyzer.analyze_variable_declaration("c", "int")
            analyzer.analyze_assignment("c", "int")  # Correct usage in scope

        analyzer.analyze_scope([inner_scope])
        try:
            analyzer.analyze_assignment("c", "int")  # Accessing outside scope
        except Exception as e:
            print(e)

        # Test array and stack type consistency
        analyzer.analyze_variable_declaration("arr", "array[int]")
        try:
            analyzer.analyze_array_assignment("arr", "float")  # Type mismatch in array
        except Exception as e:
            print(e)

        analyzer.analyze_variable_declaration("stack_var", "stack[int]")
        try:
            analyzer.analyze_stack_operation("stack_var", "float", "push")  # Type mismatch in stack
        except Exception as e:
            print(e)

        # Test function declarations and calls
        analyzer.analyze_function_declaration("add", ["int", "int"], "int")
        analyzer.analyze_function_call("add", ["int", "int"])  # Correct usage
        try:
            analyzer.analyze_function_call("add", ["int", "float"])  # Type mismatch in arguments
        except Exception as e:
            print(e)

        # Test return type consistency
        try:
            analyzer.analyze_return("float", "int")  # Return type mismatch
        except Exception as e:
            print(e)

    except Exception as overall_exception:
        print("Overall exception during analysis:", overall_exception)

# Run the test
test_semantic_analyzer()
