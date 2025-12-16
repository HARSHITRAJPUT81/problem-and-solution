l = [3,5,8]
# print(marks)
print(type(l))
print(l)

marks = [3,5,7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])



colours = ["Red","Green","Blue","Yellow","Green"]
if "Yellow" in colours:
    print("Yes")
else:
    print("No")    


details = ["Abhijeet",18,"FYBScIT",9.8]
print(details)



#Negative Indexing
marks = [3,5,6,"Harry",True ,6,4,0,3,2,6,8]
print(marks[-3]) #Negative index
print(len(marks)-3) #Positive index 
print(marks[5-3]) #Positive index
print(marks[2]) #Positive index 

if 6 in  marks:
    print("yes")
else:
    print("no")    

if"arry" in "Harry":
    print("yes")  


#Jump indexing  
marks = [3,5,6,"Harry",True ,6,4,0,3,2,6,8]
print(marks[0:7])
print(marks[1:9])
print(marks[1:9:2])


