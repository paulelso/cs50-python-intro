def main():
    text = input("Input: ")
    modified_text = remove_vowels(text)
    print(modified_text)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

if __name__ == "__main__":
    main()