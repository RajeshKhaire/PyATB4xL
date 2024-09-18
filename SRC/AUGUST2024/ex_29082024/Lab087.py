squares = [1, 4, 9, 16, 25]
squares = [1, 4, 9, 16, 25]
print(squares.sort())

squares = [1, 4, 9, 16, 25]
print(squares.pop())
print(squares)

squares[3] = 18
print(squares)

# Tuple - collection of Item
my_tuple = (1, 4, 9, 16, 25)
#my_tuple[3] = 64 # immutable in nature
print(my_tuple) # 'Tuple' object does not support item assignment

shopping_list_wife =["bread", "butter", "paneer"]
#shopping_list_wife [2] ="Milk"
shopping_list_wife.append("Milk")
print(shopping_list_wife)

#real world project
# the testing academy.com, sdet, live
my_tuple = ("tta.com","sdet-live")
my_api_list = list(my_tuple) # conversion
print(my_api_list)
my_api_list = tuple(my_api_list)# conversion

# real case, where we tuples
Api_urlss = ("https://sdet.live/python0x", "https://awesomeqa.com","https://thetestingacademy.com")
print(Api_urlss[0])
print(Api_urlss[1])