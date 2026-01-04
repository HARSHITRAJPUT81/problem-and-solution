#Enumerate in Python

marks = [12,34,43,67,96,75,64]
#We can write like this
index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("Harry,awwesome!")
    index +=1    
#and also like this
for index, mark in enumerate (marks):
    print(mark)
    if (index == 3):
        print("Harry,awesome!")



fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

