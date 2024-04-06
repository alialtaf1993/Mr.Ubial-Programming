def mcdonalds_bot():
    while True: #loop to keep prompting the user the question until they quit the program
        answer = input("Welcome to McDonald's big boy. Would you like fries with your meal? (Yes/No): ")

        # Convert them to lowercase so it's case-insensitive and it is easier to distinguish
        answer_lower = answer.lower()

        # Check if the user wants fries
        if answer_lower == 'yes':
            print("Wow you must be very hungry. Here are your juicy fries!")
            break
        elif answer_lower == 'no':
            print("Okay, no fries for your meal.")
            break
        elif answer_lower == 'hell nah':
            print('Sorry for disturbing you sir')
        else:
            print(f"Sorry, I am too incompetent to understand what is '{answer}'. Please answer with 'Yes' or 'No'.")

if __name__ == "__main__":
    mcdonalds_bot()