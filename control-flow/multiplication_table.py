print =("\n welcome to the multiplication table")
number =int(input("Enter a number to see its multiplication table:"))
for num in range(1,11):
    for numbers in range(1,11):
           print(f"{number} x {numbers} =.format {number * numbers}")
