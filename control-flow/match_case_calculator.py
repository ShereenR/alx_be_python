num1 = int(input("Enter the first number:"))
operation = input("Choose the operation (+, -, *, /):")
num2 = int(input("Enter the second number:"))
match operation :
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0 :
           print(num1 / num2)
        else :
             print("Cannot divide by zero")
    case _:
        print("error")
print(f"The result is {num1 * num2}")