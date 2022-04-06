def encryptCaesar(text,s):
 encryption = ""
 for i in range(len(text)):
      char = text[i]
      # Encrypts uppercase
      if (char.isupper()):
         encryption += chr((ord(char) + s-65) % 26 + 65)
      elif (char == " "):
         encryption = encryption + " "
      # Encrypts lowercase
      else:
         encryption += chr((ord(char) + s - 97) % 26 + 97)
 return encryption
originText = "Devionne Littleton"
s = 6

print ("Original Text : " + originText)
print ("The Shift Amount : " + str(s))
print ("Encryption: " + encryptCaesar(originText,s))