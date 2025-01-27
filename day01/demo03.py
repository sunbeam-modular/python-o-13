
# Python statements
#   Single line statement
#       Usually one statement on one line
#       Optional semicolon at the end.
#       If multiple statements to be written on single line must give ; at end of each stmt.
#   Multi-line statement
#       Single Python statement spanning across multiple lines of code.
#       Used for making code more readable.
#       Commonly used for creating colletions (Lists, Dictionaries, ...)
#   Comments
#       Start with #

# Single line statements
print("statement 1");
print("statement 2")

print("statement 3"); print("statement 4"); print("statement 5")

# Multi-line statements
num_list = [
            11,
                22,
                    33,
            44
        ]

# multiline statement -- using line continuation char (\)
result = 11 + 22 \
         + 33 + 44 + 55 \
         + 66

print(result)