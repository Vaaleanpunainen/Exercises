example = input("Enter your string: ")

character = example[0]

def char_class(character):
    if character.islower():
        return "lower"
    elif character.isupper():
        return "upper"
    elif character.isdigit():
        return "digit"
    else:
        return "other"


print(char_class(character))
