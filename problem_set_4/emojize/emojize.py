import emoji

def emojize_string():
    user_input = input("Input: ")
    emojized_string = emoji.emojize(user_input, language='alias')
    print(emojized_string)

emojize_string()