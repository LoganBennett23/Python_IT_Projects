#This program has multiple menu options for passwords
#Using my base knowledge of Python and some help from AI, I was able to create this program.
#This is still a work in progress and I will be adding more features to it in the future (hopefully).

#Imported modules
import random
import string

#Function for menu option 3: "Generate a memorable random password with words"
def gen_memorable_password():
    # Ask the user which word list they want to use
    while True:
        choice = input(
            "Do you want to use the default word list or provide your own? "
            "(default/custom): "
        ).lower().strip()

        if choice == "default":
            #These were randomly generated words from AI, good thing is you can always add more words to the default list!
            words = [
                "war", "peace", "love", "hate", "friendship", "betrayal", "courage", "fear",
                "hope", "despair", "joy", "sorrow", "freedom", "oppression",
                "truth", "lies", "light", "darkness", "life", "death",
                "music", "art", "science", "technology", "nature", "society",
                "history", "future", "dreams", "reality", "imagination",
                "soldier", "king", "queen", "prince", "princess", "knight", "wizard",
                "dragon", "castle", "forest", "mountain", "river", "ocean", "desert", "island", 
                "city", "village", "temple", "palace",
                "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", 
                "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon",
            ]
            break

        elif choice == "custom":
            while True:
                custom_words = input(
                    "Enter your custom word list, separated by commas: "
                )

                words = [word.strip() for word in custom_words.split(",") if word.strip()]

                if words:
                    break

                print("\033[1m\033[31mPlease enter at least one word.\033[0m")

            break

        else:
            print("\033[1m\033[31mInvalid choice. Please enter 'default' or 'custom'.\033[0m")

    # Ask whether numbers should be included
    while True:
        choice_num = input(
            "Do you want numbers in your password? (yes/no): "
        ).lower().strip()

        if choice_num in ("yes", "no"):
            break

        print("\033[1m\033[31mInvalid choice. Please enter 'yes' or 'no'.\033[0m")

    # Ask whether special characters should be included
    while True:
        special_char_choice = input(
            "Do you want special characters in your password? (yes/no): "
        ).lower().strip()

        if special_char_choice in ("yes", "no"):
            break

        print("\033[1m\033[31mInvalid choice. Please enter 'yes' or 'no'.\033[0m")

    # Ask how many words the password should contain
    while True:
        try:
            num_words = int(
                input("Enter the number of words for the memorable password: ")
            )

            if num_words <= 0:
                print("\033[1m\033[31mPlease enter a number greater than 0.\033[0m")
                continue

            break

        except ValueError:
            print("\033[1m\033[31mInvalid input. Please enter a number.\033[0m")


    # Generate the memorable password
    memorable_password = ''.join(
        random.choice(words) for _ in range(num_words)
    )

    # Add a number if requested
    if choice_num == "yes":
        memorable_password += str(random.randint(0, 9))

    # Add a special character if requested
    if special_char_choice == "yes":
        memorable_password += random.choice(string.punctuation)

    print("\n")

    # Print the generated password
    print(
        "\033[1m\033[32m"
        f"Generated memorable password: {memorable_password}"
        "\033[0m\n"
    )

    input_save = input(
        "Do you want to save this password to a file? (yes/no): "
    ).lower().strip()
    if input_save == "yes":
        with open("memorable_passwords.txt", "a") as file:
            file.write(memorable_password + "\n")

#Function for menu option 1: "Generate a random password"
def gen_password():
   

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except ValueError:
            print("\033[1m\033[31mInvalid input. Please enter a number.\033[0m")

    # Create a pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    gen_pass = ''.join(random.choice(characters) for i in range(length))

    print("\n")
    #Print the generated password in bold and green text
    print("\033[1m\033[32mGenerated password: {}\033[0m".format(gen_pass) + "\n")

#Function for menu option 2: "Check a password"
def check_password(password_check):
    # Check password length

    print("\n")

    #Check for length requirement
    if len(password_check) >= 8:
        print("\033[1mPassword length >= 8 characters?: \033[32m✅\033[0m")
    else:
        print("\033[1mPassword length >= 8 characters?: \033[31m❌\033[0m")

    # Check for uppercase letter
    if any(char.isupper() for char in password_check):
        print("\033[1mPassword contains an uppercase letter?: \033[32m✅\033[0m")
    else:
        print("\033[1mPassword contains an uppercase letter?: \033[31m❌\033[0m")

    # Check for lowercase letter
    if any(char.islower() for char in password_check):
        print("\033[1mPassword contains a lowercase letter?: \033[32m✅\033[0m")
    else:
        print("\033[1mPassword contains a lowercase letter?: \033[31m❌\033[0m")

    # Check for digit
    if any(char.isdigit() for char in password_check):
        print("\033[1mPassword contains a digit?: \033[32m✅\033[0m")
    else:
        print("\033[1mPassword contains a digit?: \033[31m❌\033[0m")

    # Check for special character
    if any(char in string.punctuation for char in password_check):
        print("\033[1mPassword contains a special character?: \033[32m✅\033[0m")
    else:
        print("\033[1mPassword contains a special character?: \033[31m❌\033[0m")

    print("\n")

#Menu function to display the options and call the appropriate functions based on user input
def menu():

    while True: 
        print("Please select an option:")
        print("1. Generate a random password")
        print("2. Check a password")
        print("3. Generate a memorable random password with words")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            gen_password()
        elif choice == "2":
            # Call the password checker function
            password_check = input("Enter the password to check: ")
            check_password(password_check)

        elif choice == "3":
            # Call the memorable password generator function (to be implemented)
            gen_memorable_password()
        elif choice == "4":
            print("\033[1m\033[32mThanks for using the program! You are cool. 😎\033[0m")
            break
        else:

            #Bold text for invalid choice and red text for invalid choice
            print("\033[1m\033[31mInvalid choice. Please try again.\033[0m")
            
#Define the main function to display the welcome message and call the menu function
def main():
    print("\033[35m")
    print(r"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║        ██████╗  █████╗ ███████╗███████╗              ║
║        ██╔══██╗██╔══██╗██╔════╝██╔════╝              ║
║        ██████╔╝███████║███████╗███████╗              ║
║        ██╔═══╝ ██╔══██║╚════██║╚════██║              ║
║        ██║     ██║  ██║███████║███████║              ║
║        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝              ║
║                                                      ║
║              🔐 PASSWORD GENERATOR 🔐                ║
║                                                      ║
║        Create a strong and secure password           ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
    """)
    print("\033[0m")
    print("\033[32mWelcome to the Password Generator and Checker Program!\033[0m")
    menu()


#Needed to ensure that the main function is called when the script is run directly
if __name__ == "__main__":
    main()


