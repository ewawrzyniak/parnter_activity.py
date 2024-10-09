#1. ask for peice of text 
userText = input(" Enter any text you please:")
#2. ask for 3 letter
firstLetter =input(" Enter the first letter : ")
secondLetter = input('Now enter the second letter: ')
thirdLetter =input('Finally, enter the last letter')

#3. convert string to lowercase
userText.lower()
firstLetter.lower()
secondLetter.lower()
thirdLetter.lower()

#4. Convert string to list 
listofWords = userText.split()
print(listofWords)

#5. print out word count (how many objects are in list 
wordCount= len(listofWords)
print(f"The word count is {wordCount} words")

#6. invert list of words
backwardsList =list(reversed(listofWords))

#7. join list using spaces 
print(" ".join(backwardsList))
      
#8. create boolean asking of "python" is in list of words 
listofWords.find("Python") 

#9. Make list into bigger list using ech letter
listofLetters =list(userText.lower())

#10. Find first and last letter of the list 

#11. Print how many times the letter is found in the text 
total1Letter= listofLetters.count(firstLetter)
print(f'')
total2Letter=
total3Letter=

for letter in 
