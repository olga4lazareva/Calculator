from core.operations import add, subtract, multiply, divide

def calculate(operation, a, b):
    if operation == "add":
        return add.run(a, b)
    elif operation == "subtract":
        return subtract.run(a, b)
    elif operation == "multiply":
        return multiply.run(a, b)
    elif operation == "divide":
        return divide.run(a, b)
    else:
        raise ValueError("Unknown operation")
