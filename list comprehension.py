lst1 = [i for i in range(4)]
print(lst1)

lst2 = [i*i for i in range(4)]
print(lst2)

lst3 = [i*i for i in range(10) if i%2==0]
print(lst3)

names = ["milo","sarah","bruno","anastasia","rosa"]
namesWith_o = [item for item in names if "o" in item]
print(namesWith_o) 


names = ["milo","sarah","bruno","anastasia","rosa"]
namesWith_o = [item for item in names if (len(item) >4)]
print(namesWith_o) 