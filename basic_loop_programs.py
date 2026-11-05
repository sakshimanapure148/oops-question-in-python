"""
Daily Python Task: Number Toolkit
Topics: loops, conditions, functions, and basic number logic.

Run: python basic_loop_programs.py
"""

def print_numbers():
    print("\nNumbers from 1 to 100:")
    for number in range(1, 101):
        print(number, end=" ")
    print()


def show_even_odd():
    even_numbers = []
    odd_numbers = []

    for number in range(1, 101):
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    print("\nEven numbers (1 to 100):")
    print(*even_numbers)
    print("\nOdd numbers (1 to 100):")
    print(*odd_numbers)


def sum_natural_numbers():
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Please enter a number greater than 0.")
        return

    total = 0
    for number in range(1, n + 1):
        total += number

    print(f"Sum of natural numbers from 1 to {n}: {total}")


def find_factorial():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    factorial = 1
    for number in range(2, n + 1):
        factorial *= number

    print(f"Factorial of {n}: {factorial}")


def check_prime():
    n = int(input("Enter an integer: "))

    if n <= 1:
        print(f"{n} is not a prime number.")
        return

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            print(f"{n} is not a prime number.")
            return

    print(f"{n} is a prime number.")


def main():
    while True:
        print("\n========== NUMBER TOOLKIT ==========")
        print("1. Print numbers from 1 to 100")
        print("2. Print even and odd numbers")
        print("3. Find sum of natural numbers")
        print("4. Find factorial of a number")
        print("5. Check prime number")
        print("0. Exit")

        choice = input("Choose an option (0-5): ").strip()

        if choice == "1":
            print_numbers()
        elif choice == "2":
            show_even_odd()
        elif choice == "3":
            sum_natural_numbers()
        elif choice == "4":
            find_factorial()
        elif choice == "5":
            check_prime()
        elif choice == "0":
            print("Thanks for using Number Toolkit!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 5.")


if __name__ == "__main__":
    main()
