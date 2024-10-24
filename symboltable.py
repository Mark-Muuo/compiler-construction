class SymbolTableHeap:
    def __init__(self):
        self.symbols = []
    
    def add_symbol(self, name, symbol_type, value=None):
        # Adds a symbol (variable) to the heap
        symbol_entry = (name, {"type": symbol_type, "value": value})
        self.symbols.append(symbol_entry)
        self._heapify_up()

    def update_symbol(self, name, new_value):
        # Updates an existing symbol's value in the heap
        for i, (sym_name, sym_data) in enumerate(self.symbols):
            if sym_name == name:
                self.symbols[i] = (name, {"type": sym_data["type"], "value": new_value})
                break
        self._heapify_down()

    def get_symbol(self, name):
        # Retrieves a symbol's data from the heap
        for sym_name, sym_data in self.symbols:
            if sym_name == name:
                return sym_data
        return None

    def _heapify_up(self):
        # Heapify logic to maintain heap properties
        pass

    def _heapify_down(self):
        # Heapify logic to maintain heap properties
        pass

# Example Zara program
symbol_table = SymbolTableHeap()

# Variable Declarations
symbol_table.add_symbol("x", "int", 10)
symbol_table.add_symbol("y", "float", 3.14)
symbol_table.add_symbol("name", "string", "Zara")

# Update a symbol's value
symbol_table.update_symbol("x", 20)

# Retrieve and print symbol details
print(symbol_table.get_symbol("x"))  # Output: {'type': 'int', 'value': 20}
print(symbol_table.get_symbol("name"))  # Output: {'type': 'string', 'value': 'Zara'}

# Sub-program example (method in Zara)
def my_method():
    symbol_table.add_symbol("z", "int", 30)
    print(symbol_table.get_symbol("z"))

my_method()
