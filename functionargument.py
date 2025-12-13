def average(a=9, b=1):
    print("The average is", (a+b)/2)


#average(4,6)

average(b=9)   


    
#Default Argument
def name(fname,mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname,mname,lname)

name("Amy")   




#Keyword Argument
#In this argument we can chnage the order
def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")





#Required Argument
#In this argument,we have to give the value.It is necessary
def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)

name("Peter","Quill") 






#Variable-length Argument
#1. Arbitrary argument
def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum=i
    print("Average is:",sum/len(numbers))

average(5,6,7,1)        




#2.Keyword Arbitrary Argument
def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname = "Buchaman", lname = "Barnes", fname = "james")    

