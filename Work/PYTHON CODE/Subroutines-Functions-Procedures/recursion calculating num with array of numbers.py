
def sumnum(num):
    if len(num)==1:
        return num[0]
    else:
        return num[0] + sumnum(num[1,])
    #end if
#end function

    
length = int(input("The number of numbers you want to enter"))
num = []

for index in range(0,length):
    num.append(input("Enter the number")

