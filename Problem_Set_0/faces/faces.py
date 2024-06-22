def faces(input):
    if input == "Hello :)" :
        return "Hello 🙂"
    elif input == "Goodbye :(" :
        return "Goodbye 🙁"
    elif input =="Hello :) Goodbye :(" :
        return "Hello 🙂 Goodbye 🙁"
    else:
        return "enter a valid input"


greeting = input("Enter a greeting from Hello :) or Goodbye :( -> " )

result = faces(greeting)
print(result)
