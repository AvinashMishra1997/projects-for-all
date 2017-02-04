from PyDictionary import PyDictionary


dictionary = PyDictionary()
print ('choose if u want the antonym or synonym or meaning or translations of a word')
d=raw_input ("Enter 'a' for antonym 's' for synonym 'm' for meanings and 't' for translations : ")
if d=='m':
    word=raw_input('Enter the word you want the meaning for: ')
    print (dictionary.meaning(word))
elif d=='s':
    word = raw_input('Enter the word you want the synonym for: ')
    print (dictionary.synonym(word))
elif d=='a':
    word = raw_input('Enter the word you want the antonym for: ')
    print (dictionary.antonym(word))
elif d=='t':
    word = raw_input('Enter the word you want the translation for: ')
    language = raw_input('enter the language code as per google: ')
    print (dictionary.translate(word , language))
