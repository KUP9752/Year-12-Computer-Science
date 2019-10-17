#Cipher-> Decrypt

##f = open("output.txt", "rt")
##data = f.read()
##f.close()
data = "z"
step = int(input("Enter the step of the encryption to Decrypt:   "))

            #//Can't decrypt lowercase letters for some reason

def cipher(n):
    for i in range(0, len(data)):
        if data[i] == " ":
                index = chr(32)
                print(index, end='')
        elif data[i] == "(":
            index = chr(40)
            print(index, end='')
        elif data[i] == ")":
            index = chr(41)
            print(index, end='')
        elif data[i] == ".":
            index = chr(46)
            print(index, end='')
        elif data[i] == ",":
            index = chr(44)
            print(index, end='')
        elif data[i].isupper():
            index = chr((ord(data[i])-n+65)%26 +65)
            print(index, end='')
        elif data[i].islower():
            index = chr((ord(data[i])-n+97)%26 + 97)
            print(index, end='')
        else:
            index = data[i]
            print(index, end='')
        #end if
#next i
#end procedure

cipher(step)

