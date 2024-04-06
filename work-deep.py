def main():
    answer = input("What is the golden rule in life and the entire universe? ")
    answer_lower = answer.lower() # The lower function to convert the user's input to lowercase so it doesn't matter if it's capitalized or not

    if answer_lower == '42' or answer_lower == 'forty-two' or answer_lower == 'forty two':
        print("Yes")
    else:
        print("No")

if __name__ == "__main__": # Main method implementation for the python file
    main()
