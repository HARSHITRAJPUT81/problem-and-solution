#1.Update method
info = {'name':'karan','age':19,'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2005})
print(info)

#2.Removing item from dictionary
#Clear() Method
info = {'name':'karan','age':19,'eligible':True}
info.clear()
print(info)

#3.Pop() Method
info = {'name':'karan','age':19,'eligible':True}
info.pop('age')
print(info)


#4.Pop item() Method
info = {'name':'karan','age':19,'eligible':True}
info.popitem()
print(info)

#5.Del() Method
info = {'name':'karan','age':19,'eligible':True}
del info ['age']             #if key is not defining the Del keyword will delete the entire dictionary. 
del info ['name']
print(info)

