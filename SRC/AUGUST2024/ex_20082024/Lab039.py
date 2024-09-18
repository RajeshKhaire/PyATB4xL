# Problem find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
#o/p ->int or String with max number

# logic ? if else - 1 condition
# more 1 condition -> if elif else

# syntax
# if condition 1:
#   print("do 1")
# elif condition 2:
#   print("do 2")
# elif condition 3:
#   print("do 3")
# else:
#   print("do 4")

num1 = eval(input("Enter the num1\n")) # 5, # 10
num2 = eval(input("Enter the num2\n")) # 3, # 12
num3 = eval(input("Enter the num3\n")) # 2, # 11

# 5>3 and 5>2 -> true ->5
# num1 > num2 and num1 > num3-> true -> num1

# 12 > 10 and 12 > 11 -> true ->12
# num2 > num1 and num2 > num3-> true -> num2

# num3

if num1 > num2 and num1 > num3:
    print(f"num1 is greater: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"num2 is greater: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"num3 is greater: {num3}")

result = max(num1, num2, num3)
print(result)