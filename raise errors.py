#This is Rising custom errors.We can raise the error by own and we can also costom the errors according us. 

a =int(input("Enter any value between 5 and 10:- "))
if(a<5 or a>10):
    raise ValueError("Value should be between 5 and 10")



class AgeError(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    raise AgeError("Age must be 18 or above")
else:
    print("You are eligible")
