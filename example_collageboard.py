newPhrase = "rainstorm"
shortPhrase = substring(newPhrase,4, len(newPhrase)-2)
print(shortPhrase)

#c reate new variable called shortPhrase
#assign it a value by slicing the newStriing vsariaable by removing the first 3 characters and the last 3 characters 
#the first 3 chsaracters are rai and the last 3 are orm 
#substring(string,start,end)

shortphrase = newPhrase[3:len(newPhrase)]

#collage board version 
# [4:len(newPhrase)-6]
print(shortphrase)
#len(newphrase)-3 = 9-3 = 6
#ends with 6 because last index is not included 