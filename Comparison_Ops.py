# Comparison Operators
while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Equal Operator
    if num1 == num2:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
    
    # Greater Than Operator
    if num2 > num1:
        print("Second number is greater than first number")
    
    # Greater Than or Equal To Operator
    if num2 >= num1:
        print("Second number is greater than or equal to first number")
    
    # Logical AND Operator
    if num1 > 100 and num2 > 100:
        print("Both numbers are big!")
    
    # Logical OR Operator
    if num1 > 100 or num2 > 100:
        print("At least one number is big!")
    
    # Logical NOT Operator
    big_numbers = not (num1 <= 100 and num2 <= 100)
    print(f"big_numbers is set to {big_numbers}")
    
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != 'yes':
        break