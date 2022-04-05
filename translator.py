from smtpd import DebuggingServer


#Giraffe Language
#vowels -> g

#dog - dgg
#cat - cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# more efficient and correct
'''
you can also comment stuff like this
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
