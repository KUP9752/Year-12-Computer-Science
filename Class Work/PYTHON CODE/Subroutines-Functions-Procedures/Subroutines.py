#passing by referance in most programing languages, means updating the original values
#passing by value doesn't update the original values it only copies its address and
#updates in the function, but doesn't update the original value

#the memory address of the original "immutable" value is copied when it enters the function

num = 3
name ="Dave"

name_list = ["D","a","v","e"]


def add_one(x):
    x +=1
    return x
#end function

def add_s(name):
    name = name+"s"
    return name
#end function

def append_s(name):
    name.append("s")
    print(name)
#end procedure

print(add_one(num))
print(num)

print(add_s(name))
print(name)

append_s(name_list)
print(name_list)

#so python passes everything by referance
#checks something called "mutability", so the original value cant be changed,
#so a new referance value is created so the function can return a new value,
#without the original "immutable" value being changed.
#however, with mutable data like the "name_list" we used, it just updates the list,
#This means the function doesn't copy the value, it just updates the original value in the corresponding address
