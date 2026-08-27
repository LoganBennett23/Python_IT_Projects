#A simple program that prompts the user for a password and checks if it matches the one they entered. 

#This I found online, I like making cools labels!
print("\033[35m")
print(r"""
 ____                                    _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|

  ____ _               _             
 / ___| |__   ___  ___| | _____ _ __ 
| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| |___| | | |  __/ (__|   <  __/ |   
 \____|_| |_|\___|\___|_|\_\___|_|   
""")
print("\033[0m")


#Function that loops until the user inputs the correct password and checks if it matches the one they entered. If it does, it prints a message and exits the program. If not, it prompts the user to try again.
def check_password(password):
    while True:
        user_input = input("Please re-enter the password to check if it matches: ")
        if user_input == password:
            print(f"Good job! The password '{password}' matches.")
            print("Exiting the program. Goodbye!")
            break
        else:
            print("The passwords do not match. Please try again.")

#Function for the main program. Calls the check_password function and passes the password variable as an argument. This is a good practice to keep the code organized and readable.   
def main():   
    #Variable to store the password entered by the user.
    password = input("Please enter a password: ")
    #Calls the function
    check_password(password)   

#This is needed to run the main function when the program is executed. It checks if the script is being run directly (not imported as a module) and calls the main function. This is a common practice in Python to allow code to be reusable and modular.
if __name__ == "__main__":
    main()