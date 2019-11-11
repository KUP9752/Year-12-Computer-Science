###-> Random List of 20 Number Generator<-###
import json
import random

numbers= []
for num in range(0,20):
     numbers.append(random.randint(0,1000))
#end if

file =input("Enter the name of the file you want to create the number list in.")
file =file + ".json"
print("Your file is called-->",file)

w = open(file,'wt')
json.dump(numbers,w)
w.close()
