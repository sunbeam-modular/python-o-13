
# calculate area of circle
PI = 3.14       # conventionally const values are declared in caps

rad = float(input("Enter circle radius: "))
#area = PI * rad * rad
area = PI * rad ** 2            # ** is power operator
print("circle area =", area)

# in-place operator
num = 8
num += 2        # num = num + 2
print("num =", num) # 10

# var=+n -- doing assignment
# var+=n -- in-place addition
var1=+2     #  var1 = +2        (+2 is same 2)
var1+=4     #  var1 += 4        (var1 = var1 + 4)

var2 = 11
# var2++      # ++ and -- operators not allowed in Python
