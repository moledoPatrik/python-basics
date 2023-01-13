# translate to a language where vowels are turned to g

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate("To be or not to be"))
