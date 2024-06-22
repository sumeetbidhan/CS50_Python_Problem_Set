def main():
    word = input("Input: ")

    result = shorten(word)
    print(f"Output: {result}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    removed_vowel = ""

    for char in word:
        if char not in vowels:
            removed_vowel +=char
    return removed_vowel

if __name__ == '__main__':
    main()
