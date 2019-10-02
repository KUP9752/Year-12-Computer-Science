#Cipher

sent = input("Enter sentence to be encrypted")
enc = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
step = int(input("Enter the step shift you want"))
print(len(sent))

def cipher(n):
    for i in range(0,len(sent)):
        
        if sent[i] == " ":
            index = chr(32)
        elif sent[i].isupper():
            index = chr((ord(sent[i])+ n-65)%26 +65)
        else:
            index = chr((ord(sent[i])+n-97)%26 + 97)
        print(index, end='')
        
    
        #end if
    #next i
#end function
print(cipher(step))



