#Cipher-> Encrypt
### SRC - This is a good effort, but I did get some
### strange characters with a shift of 5.
### I couldn't get the decrypt to work.


step = int(input("Enter the step shift you want:   "))

f = open("input.txt","rt")
sent = str(f.read())
f.close()

def cipher(n):
    for i in range(0,len(sent)):
        
            if sent[i] == " ":
                index = chr(32)
                print(index, end='')
            elif sent[i] == "(":
                index = chr(40)
                print(index, end='')
            elif sent[i] == ")":
                index = chr(41)
                print(index, end='')
            elif sent[i] == ".":
                index = chr(46)
                print(index, end='')
            elif sent[i] == ",":
                index = chr(44)
                print(index, end='')
            elif sent[i].isupper():
                index = chr((ord(sent[i])+ n-65)%26 +65)
                print(index, end='')
            elif sent[i].islower():
                index = chr((ord(sent[i])+n-97)%26 + 97)
                print(index, end='')
            
            else:
                index = sent[i]
                print(index, end='')
            
        #end if
    #next i
#end procedure

cipher(step)
##p = open("output.txt", "wt")
##p.write(print(cipher(step)))
##p.close





