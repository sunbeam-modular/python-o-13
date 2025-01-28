
# if-else statement -- find max of two numbers

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num1 > num2:
    # statements in if block must be given with indentation
    print("num1 is max number")
    print("max number =", num1)
else:
    # statements in else block must be given with indentation
    print("num2 is max number")
    print("max number =", num2)

print("this statement is outside else block")