
# In Java/C#, ...
#   String s1 = "One";
#   Variable declaration and Initialization -- Giving data type is compulsory.

# In Python, ...
#   s1 = "One"  -- Data type inferred at runtime.

# In Python -- Type Hinting
#   var:data-type = value
# Programmer may mention the data type while assigning variable for first time.
# Applications
#   1. Make program more readable to other developers
#   2. Used by Python type checker software to detect possible errors
#   3. Used by some IDEs for warnings (code check) and showing intellisense

s1:str = "One"
print("s1 =", s1)
print("s1 type=", type(s1)) # str

s2:int = 2
print("s2 =", s1)
print("s2 type=", type(s2)) # int

s3:float = 3.14
print("s3 =", s3)
print("s3 type=", type(s3)) # float

# Type Hint -- hint of data type is given to Python type checkers/IDE/teammates.
#   The actual type will be detected dynamically -- at runtime.
#   Python compiler/interpreter and PVM will ignore the type hints.
s4:str = 1234   # No error: Only waring -> Expected 'str' got 'int'
print("s4 =", s4)
print("s4 type=", type(s4)) # int

s5:int = 54
print("s5 =", s5)
print("s5 type=", type(s5)) # int

s5 = 5.6
print("s5 =", s5)
print("s5 type=", type(s5)) # float
