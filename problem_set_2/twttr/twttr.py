def main():
    user_input = input()
    output = remove_vowels(user_input)
    print(output)

def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_without_vowels = ''
    for char in text:
        if char.lower() not in vowels:
            text_without_vowels += char

    return text_without_vowels

if __name__ == "__main__":
    main()