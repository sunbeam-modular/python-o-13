
# Type conversion -- Implicit conversion or Explicit conversion
num1 = 12       # int
num2 = 1.2      # float
num3 = num1 + num2
        # num1 (int) -- temp converted to float
        # then will be added into num2 float
        # will yield float result
print("num3 =", num3)
print("num3 type =", type(num3))

var1 = True     # bool
var2 = 40       # int
var3 = var1 + var2
        # var1 True --> int(1) + var2 int = var3 int
print("var3 =", var3)
print("var3 type =", type(var3))

num = 300
string = "War"
# result = num + string
        # int is not auto converted to string in Python
        # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Explicit conversion functions
#   str(), int(), float(), bool() -- basic fns
#   list(), set(), tuple(), dict() -- advanced fns for conversion

result = str(num) + string
        # str(num) temp converts num from int to "str" type.
        # can be added to other string
print("result =", result)
print("result type =", type(result))    # str

s = "Nilesh"
flag = bool(s)     # explicit conversion from str to bool
        # If string is empty -- bool() will return False
        # If string is not empty -- bool() will return True
print("flag =", flag)       # True
print("flag type =", type(flag))  # bool

# In Python, there is no concept of const/final variables.
#   Conventionally, const variables should be named in capital.
PI = 3.14
num = 7
res = num + int(PI)     # PI is temp converted to int (.14 is lost)
print("res =", res)       # 10
print("res type =", type(res))  # int

ch = "A"
# n = int(ch)     # ValueError: invalid literal for int() with base 10: 'A'
ch = "123456"
n = int(ch)
print("n =", n)
print("n type =", type(n))  # int

