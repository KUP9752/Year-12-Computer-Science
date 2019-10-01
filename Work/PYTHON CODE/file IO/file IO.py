
f = open("input.txt", "rt")
data=f.read()
f.close()
print(data)

for line in data: #prints individual letters line by line
    print(line)
    
f = open("input.txt","rt")
for a in f:
    print(a)
f.close()

f = open("output.txt","wt")
f.write(data)
f.close()

f = open("output.txt","wt")
print(data,file = f)
f.close()
