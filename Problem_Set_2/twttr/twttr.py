def main():
    text = input("Input: ")

    result = remove_vowels(text)
    print(f"Output: {result}")


def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    removed_vowel = ""

    for char in text:
        if char not in vowels:
            removed_vowel +=char
    return removed_vowel

if __name__ == '__main__':
    main()
