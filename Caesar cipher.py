alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print ( len(alphabet)) 
direction = input("Type 'encode' OR 'e' to encrypt, type 'decode' OR 'd' to decrypt:\n").lower()
password = input ( " Enter your Password " )
iteration = int ( input ( " Enter Iteration value " ))
result = ''
for i in password :
    length = alphabet.index(i)
    length += iteration
    result += alphabet[length]
print ( result ) 
