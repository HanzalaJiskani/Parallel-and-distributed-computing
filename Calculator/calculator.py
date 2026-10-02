"Simple python calculator"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a // b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot take modulus by zero.")
    return a % b


def power(a, b):
    return a ** b


OPERATIONS = {
    "1": ("Addition (+)", add),
    "2": ("Subtraction (-)", subtract),
    "3": ("Multiplication (*)", multiply),
    "4": ("Division (/)", divide),
    "5": ("Floor Division (//)", floor_divide),
    "6": ("Modulus (%)", modulus),
    "7": ("Exponent (**)", power),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again.")


def main():
    print("=== Python Calculator ===")
    while True:
        print("\nChoose an operation:")
        for key, (name, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("Your choice: ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break
        if choice not in OPERATIONS:
            print("Invalid choice, try again.")
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")
        name, func = OPERATIONS[choice]

        try:
            print(f"Result ({name}): {func(a, b)}")
        except ZeroDivisionError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
