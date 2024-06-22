expression = input("Expression: ")

x_str, operator, z_str = expression.split()

x = int(x_str)
z = int(z_str)

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError("Invalid operator")

result = calculator(x, z, operator)

print(f"{result:.1f}")
