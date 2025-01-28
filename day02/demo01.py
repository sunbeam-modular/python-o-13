# Variables demo program

# Variable = Vary Able = Named memory location
#   In Python, variables are not declared before use (as in C/C++/Java).
# In Python variables are associated with data type -- Dynamically (at runtime).
#   So Python is "Dynamic Typing" language
#   One cannot create un-intialized variable
#   To check type of any variable -- use type() function
# To print variable address in memory, use id() function

num1 = 12
print("(int) num1 =", num1)
print("num1's type =", type(num1))
print("num1's addr =", id(num1))
print("num1 obj's size =", num1.__sizeof__())
# print(f"num1 = {num1}")

num2 = 3.14
print("(float) num2 =", num2)
print("num2's type =", type(num2))
print("num2's addr =", id(num2))
print("num2 obj's size =", num2.__sizeof__())

num3 = 2+3j
print("(complex) num3 =", num3)
print("num3's type =", type(num3))
print("num3's addr =", id(num3))
print("num3 obj's size =", num3.__sizeof__())

num4 = True
print("(bool) num4 =", num4)
print("num4's type =", type(num4))
print("num4's addr =", id(num4))
print("num4 obj's size =", num4.__sizeof__())

name = "Nilesh"
print("(str) name =", name)
print("name's type =", type(name))
print("name's addr =", id(name))
print("name obj's size =", name.__sizeof__())
