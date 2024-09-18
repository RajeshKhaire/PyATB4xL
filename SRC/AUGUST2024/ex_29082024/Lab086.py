# list
# List - collection of items (duplication is allowed)
my_list = [1,2,3] # same type of data (int)
my_list2 = [1, True,"pramod", 12.34]
print(my_list)
print(my_list2)
print(len(my_list))

print(my_list[0])
print(my_list[2])
#print(my_list[10]) # list index out of range - exception

my_list[0] = "Pramod"
my_list[1] = "Dutta"
my_list[2] = "Dutta2"

#Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 0 - ", my_list[1])
print("element at the index 0 - ", my_list[2])

print(my_list)
for element in my_list:
    print(element)

for i in range(1,10): # [1,2,3,4,5,6,7,8,9]
    print(i)

# range(1,10,1) - > list [1,2,3,4,5,6,7,8,9
print("------")
my_list = [1,2,3]

# Append
my_list.append(4) # Append object to the end of the list
my_list.append(5)
print(my_list)

my_list.extend([6,7,8])
my_list.extend([9])
print(my_list)

# insert()
my_list.insert(1,"dutta")
print(my_list)
print(len(my_list))

# remove()
my_list.remove("dutta")
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove(9)
print(my_copy_list)
my_copy_list.sort()
my_copy_list.sort(reverse=False)
print(my_copy_list)
my_copy_list.reverse()
print(my_copy_list)