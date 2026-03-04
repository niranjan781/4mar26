class AdvancedCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b

    def floor_division(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a // b


# ---------------- Main Program ---------------- #

calc = AdvancedCalculator()

while True:
    print("\n--- ADVANCED CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == "8":
        print("Exiting calculator...")
        break

    if choice not in ("1","2","3","4","5","6","7"):
        print("Invalid choice. Try again.")
        continue

    # Taking inputs
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Match choice to method
    if choice == "1":
        print("Result:", calc.add(a, b))
    elif choice == "2":
        print("Result:", calc.subtract(a, b))
    elif choice == "3":
        print("Result:", calc.multiply(a, b))
    elif choice == "4":
        print("Result:", calc.divide(a, b))
    elif choice == "5":
        print("Result:", calc.power(a, b))
    elif choice == "6":
        print("Result:", calc.modulus(a, b))
    elif choice == "7":
        print("Result:", calc.floor_division(a, b))
