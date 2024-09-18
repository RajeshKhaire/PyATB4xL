t = ("The Testing Academy", "for", " The Testing Academy")
print(t)
print(set(t))

set1 ={1,2,3}
set2 ={4,5,6}
my_set = set1.union(set2)
print(my_set)

set1 ={1,2,3,4,5,}
set2 ={4,5,6,7,8,9,}
my_set = set1.intersection(set2)
print(my_set)

# my_set = set1.difference(set2)
set1 ={11,22,33,44,55,}
set2 ={44,55,66,77,88,99,}
my_set = set1.difference(set2)
print(my_set)

set1 ={1,2,3,4,5,}
set2 ={2,7,8,9,}
subset = set2.issubset(set1)
print(subset)