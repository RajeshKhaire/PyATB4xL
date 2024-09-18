def sum_of_three_number(a, b, c):
    print(a + b + c)

result = sum_of_three_number(10, 20, 30)
print(result)

def sum_of_three_number(a, b=20, c=40):
    return a + b + c

#result = sum_of_three_number(10, 20, 30)
#result = sum_of_three_number(10,  , 30)
#result = sum_of_three_number(10)
#result = sum_of_three_number()
result = sum_of_three_number(a= 20, c= 30)

print(result)