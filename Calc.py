#This is a calculator project

print (" ")
print("************************")
print("This is a calculator app")
print("************************")
print (" ")
val1 = input("Enter the 1st number: ")
print (" ")
val2 = input("Enter the 2nd number: ")
print (" ")
num1 = int(val1)
num2 = int(val2)
print("----------------------------------------------------")
print("You can perform the following arithmetic operations:")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
print("----------------------------------------------------")
print (" ")

while True:
    print (" ")
    choice = input("Enter your choice (1/2/3/4): ")
    print (" ")

    if choice == "1":
        result = num1 + num2 
        print (" ")
        print("--------------------------------------")
        print(f"sum of {num1} and {num2} is: {result}")
        print("--------------------------------------")
        print (" ")
        break
    elif choice == "2":
        result = num1 - num2
        print (" ")
        print("---------------------------------------------")
        print(f"Subtration of {num1} and {num2} is: {result}")
        print("---------------------------------------------")
        print (" ")
        break
    elif choice == "3":
        result = num1 * num2
        print (" ")
        print("-------------------------------------------------")
        print(f"Multiplication of {num1} and {num2} is: {result}")
        print("-------------------------------------------------")
        print (" ")
        break
    elif choice == "4":
        result = num1 / num2
        print (" ")
        print("-------------------------------------------")
        print(f"Division of {num1} and {num2} is: {result}")
        print("-------------------------------------------")
        print (" ")
        break
    else:
        print("Incorrect choice. Enter 1 or 2 or 3 or 4")