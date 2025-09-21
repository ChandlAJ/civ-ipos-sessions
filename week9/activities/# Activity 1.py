# Activity 1
# What are the major step to solving the task?


def most_frequent_character_count(text_string):
    #loop over the letters and store in dictionary
    #convert string to lower case
    text = text_string.lower()
    letters_in_text = {}
    for letter in text:
        if letter.isalpha():
            if letter in letters_in_text.keys():
                letters_in_text[letter] = letters_in_text.get(letter, 0) + 1
            else:
                letters_in_text[letter] = 1
        else:
            continue
    most_frequent = max(letters_in_text, key=letters_in_text.get)
    return most_frequent, letters_in_text[most_frequent]


phrase = "Hello there! How are you today?"
print(most_frequent_character_count(phrase))
