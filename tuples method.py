#Manipulating tuples
countries = ("Spain","Italy","India","England")
temp = list(countries)
temp.append("Russia")      #add item
temp.pop(3)                #remove item
temp[2] = "Finland"       #change item
countries = tuple(temp)
print(countries)



#We can directly concatenate two tuples without converting them to list
#EX.
countries = ("Spain","Italy","India","England")
countries2 = ("Vietnam","India","China","Japan")
southEastAsia = (countries + countries2)
print(southEastAsia)



#Tuple Methods
#1.Count() Method
#Syntex:- tuple.count(element)
tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.count(3)
print('countof 3 in tuple1 is:',res)


#2.Index Method
#Syntex:- tuple.index(element,stsrt,end)
tuple = (0,1,2,31,2,3,1,3,2)                  #This method raises a valueErrorif the element is not found in the tuple.
res = tuple.index(3)
print('First occurrence of 3 is',res)
