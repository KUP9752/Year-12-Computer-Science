#Cipher



step = int(input("Enter the step shift you want"))

f = open("input.txt","rt")
sent = f.read()
f.close()

def cipher(n):
    for i in range(0,len(sent)):
        
        if sent[i] == " ":
            index = chr(32)
        elif sent[i].isupper():
            index = chr((ord(sent[i])+ n-65)%26 +65)
        else:
            index = chr((ord(sent[i])+n-97)%26 + 97)
        print(index, end='')
        p = open("output.txt","wt")
        p.write(cipher(step))
        p.close
        
    
        #end if
    #next i
#end procedure

print(cipher(sent))






