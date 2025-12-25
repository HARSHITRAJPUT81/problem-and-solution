# s1 = {1,2,5,7}
# s2 = {3,9,8}
# print(s1.union(s2))

# s1.update(s2)
# print(s1)

cities = {"Lucknow","Delhi","Kanpur","Agara"}
cities2 = {"Delhi","Mumbai","Varanashi"}
cities3 = cities.union(cities)
print(cities3)

cities.update(cities2)
print(cities)


set1 = {"apple", "banana"}
set2 = {"banana", "cherry"}
different = set1.symmetric_difference(set2)  # or set1 ^ set2
print(different)  # {'apple', 'cherry'}
