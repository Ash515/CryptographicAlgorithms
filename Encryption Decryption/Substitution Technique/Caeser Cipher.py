def caeser(text,s):
    res=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            res+=chr((ord(char)+s-65)%26+65)
        else:
            res+=chr((ord(char)+s-97)%26+97)
        
    return res

print("To Encrypt the given text using ceaser cipher technique")
t=input("Enter the text:")
key=int(input("Enter the key shift value:"))
print(caeser(t,key))


