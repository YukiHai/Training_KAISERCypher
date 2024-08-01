alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alph_shift = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i = 0
x = 0
shifter = int(input("Type the shift: \n"))
print(range(shifter))



def shifted(i_1, x_2):
    for letter in alphabet:
        
        #TODO: Use Append instead of this and change lower value X_2 to use i_1 so that i dont need the extra variable
        if i_1+shifter < 26:
            alph_shift[i_1+shifter] = letter
            i_1+=1
        else:
            alph_shift[x_2] = letter
            x_2+=1

def encryptor(input_text, shifted_alph):
    listtext = []
    rem_number = []
    for letter in input_text:
        rem_number.append(shifted_alph.index(letter))
    print(rem_number)
    
    for item in rem_number:
        print(item)
        listtext.append(alphabet[item])
    print(listtext)

    return listtext

def decryptor(decrypting):
    decryptText = []
    rem_number = []
    for letter in decrypting:
        rem_number.append(alphabet.index(letter))
    print(rem_number)

    for item in rem_number:
        decryptText.append(alph_shift[item])
    print(decryptText)
    return 0


shifted(i, x)
print(alph_shift)

enc_dec = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
inp_text = input("Type your message: \n").lower()

encryptor(inp_text, alph_shift)
decryptToMessage = input("Type message to decrypt: \n").lower()
decryptor(decryptToMessage)
