import math
def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    if y == 0:
        return "Error"
    return x / y
def power (x,y):
    return x ** y 
def get_number(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == "pi":
        return math.pi
    elif user_input == "e":
        return math.e
    elif user_input == "tau":
        return 2 * math.pi
    elif user_input == "phi":
        return (1 + 5 ** 0.5) / 2
    elif user_input == "g":
        return 9.81
    elif user_input == "inf" or user_input == "infinity":
        return math.inf
    else:
        return float(user_input)
    
print("Welcome to the Calculator!")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Trigonometry")
print("Pro Tip: You can type 'pi', 'e', 'inf' and more when entering your numbers!")

while True:
    choice = input("Enter choice: ")

    if choice == "1":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print(f"The answer is {add(num1, num2)}")
    elif choice == "2":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print(f"The answer is {subtract(num1, num2)}")
    elif choice == "3":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print(f"The answer is {multiply(num1, num2)}")
    elif choice == "4":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print(f"The answer is {divide(num1, num2)}")
    elif choice == "5":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print(f"The answer is {power(num1, num2)}")
    elif choice == "6":
        print("1. Sine\n2. Cosine\n3. Tangent")
        second_choice = input("Enter the function you want to use: ")
        if second_choice == "1":
            angle_in_degrees = get_number("Enter angle in degrees: ")
            angle_in_radians = math.radians(angle_in_degrees)
            print(f"The answer is {math.sin(angle_in_radians)}")
        elif second_choice == "2":
            angle_in_degrees = get_number("Enter angle in degrees: ")
            angle_in_radians = math.radians(angle_in_degrees)
            print(f"The answer is {math.cos(angle_in_radians)}")
        elif second_choice == "3":
            angle_in_degrees = get_number("Enter angle in degrees: ")
            angle_in_radians = math.radians(angle_in_degrees)
            print(f"The answer is {math.tan(angle_in_radians)}")
        else:
            print("Invalid! Please choose from 1-3.")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid! Please choose from 1-6.")
