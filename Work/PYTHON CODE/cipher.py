#Cipher

sent = input("Enter sentence to be encrypted")
enc = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
step = int(input())
def cipher(n):
    for i in range(0,len(sent)):
        index = 0
        if sent[i] == " ":
            enc[i] = " "
        else:
            index =(((ord(sent[i])+ n)-65)%26)+65)
            enc[i] = chr(index)
    print(enc)
        #end if
    #next i
#end procedure
cipher(step)
            
        
