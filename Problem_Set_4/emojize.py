import emoji

def main():
    text = input("Enter a string with emoji codes: ")

    convert = emoji.emojize(text, language='alias')

    print("Output: ", convert)

if __name__ == '__main__':
    main()
