# --- Calculator Class ---
class Calculator:
    def __init__(self):
        pass  # No state needed

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b


# --- Sample Usage ---
def main():
    calc = Calculator()

    a = 10
    b = 5

    print(f"{a} + {b} = {calc.add(a, b)}")
    print(f"{a} - {b} = {calc.subtract(a, b)}")
    print(f"{a} * {b} = {calc.multiply(a, b)}")
    print(f"{a} / {b} = {calc.divide(a, b)}")
    print(f"{a} ^ {b} = {calc.power(a, b)}")
    print(f"{a} % {b} = {calc.modulus(a, b)}")

    # Edge case
    print(f"{a} / 0 = {calc.divide(a, 0)}")

if __name__ == "__main__":
    main()
