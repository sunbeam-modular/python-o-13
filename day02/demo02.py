
# In Python, numeric variables cannot be modified in-place.
#   If you try to modify the variable, internally it will create a new variable at
#       new memory location.
#   The old memory location will be automatically freed by Python (mem manager)

num1 = 12
print("(int) num1 =", num1)
print("num1's type =", type(num1))
print("num1's addr =", id(num1))

num1 = 23
print("(int) num1 =", num1)
print("num1's type =", type(num1))
print("num1's addr =", id(num1))

# If same const value is assigned to two different variables,
#   In memory they will be stored at same location (memory optimization)
num2 = 34
print("num2's addr =", id(num2))
num3 = 34
print("num3's addr =", id(num3))

# print(num4) # Error: cannot create uninitialized variables
