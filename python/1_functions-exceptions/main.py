from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    power_numbers,
    calculator,
)

operations = {
        1: add_numbers,
        2: subtract_numbers,
        3: multiply_numbers,
        4: divide_numbers,
        5: power_numbers
    }


def user_input():
    while True:
        try:
            operation = int(
                input(
                    "Choose an operation: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power: "
                )
            )
            if operation not in operations.keys():
                print("Invalid operation selected. Please choose a valid operation.")
                continue

            numbers_count = int(
                input(
                    "Enter the number of numbers you want to perform the operation on: "
                )
            )

            if numbers_count < 1:
                print("Number of numbers should be at least 1.")
                continue

            numbers = []
            for _ in range(numbers_count):
                input_number = int(input("Enter the number: "))
                numbers.append(input_number)

            return operation, numbers

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def main():
    operation, numbers = user_input()
    execute_operation(operation, numbers)


def execute_operation(operation, numbers):
    operation_names = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Division",
        5: "Power"
    }
    try:
        if operation in [1, 2, 3, 4]:
            result = calculator(operations[operation], *numbers)
        else:
            base = numbers[0]
            exponent = numbers[1] if len(numbers) > 1 else 1
            result = calculator(power_numbers, base, exponent)
    except ValueError as e:
        print(e)
    finally:
        print(f"The result of the operation is: {result}")
        print(f"{operation_names[operation]} Operation completed.")

if __name__ == "__main__":
    main()
