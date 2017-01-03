# Ask user for a word to translate
original = input('Enter a word:')

# Rule to add at end of word for translation
pyg = 'ay'

# Determine if original word is valid entry for translation 
# i.e. that it has a length and contains only letters (no numbers or spaces)
if len(original) > 0 and original.isalpha():
    #change original word to lowercase
    word = original.lower()
    
    #take the first letter of the word for translation
    first = word[0]
    
    #create the new word by taking off the first character and adding it to the end with 'ay' after it
    new_word = word[1:len(word)] + first + pyg
    
    #print the new word
    print(new_word)

# If word isn't valide will return empty
else:
    print('empty')