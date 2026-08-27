#A program that is built to help understand networking ports and users will be quizzed.

import random

#Dictionary of common networking protocols and their corresponding port numbers and if its a TCP or UDP protocol
protocols = {
    "HTTP": (80, "TCP"), "HTTPS": (443, "TCP"), "FTP": (21, "TCP"), "SSH": (22, "TCP"), "Telnet": (23, "TCP"),
    "SMTP": (25, "TCP"), "DNS": (53, "UDP"), "POP3": (110, "TCP"), "IMAP": (143, "TCP"), "SNMP": (161, "UDP"), 
    "LDAP": (389, "TCP"), "RDP": (3389, "TCP"), "TFTP": (69, "UDP"), "SFTP": (22, "TCP"), "NTP": (123, "UDP"),
}

#Fancy label for the quiz
print("\033[35m Welcome to the Networking Ports Quiz! \033[0m")

#Until the user enters exit, this will indefinitely loop. If the user input isn't 1, it will prompt the user to try again.
while True:
    user_input = input("Type '1' to start the quiz or 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Exiting the quiz. Goodbye!")
        break

    if user_input != "1":
        print("Invalid input. Please try again.")
        continue


# Start the quiz
    protocol, (port, proto_type) = random.choice(list(protocols.items()))
    user_answer = input(f"What is the port number for {protocol}?: ")

    #If the user input is a digit and it equals the randomly selected port number (from the dict code above), it will print correct. Same with the protocol type
    #If it is incorrect, it will give feedback on the correct answer!
    if user_answer.isdigit() and int(user_answer) == port:
        print("Correct!")
        proto_type_answer = input("What is the protocol type for this port? (TCP/UDP): ")
        if proto_type_answer.upper() == proto_type:
            print("Correct!")
        else:
            print(f"Incorrect. The correct protocol type for {protocol} is {proto_type}.")
    else:
        print(f"Incorrect. The correct port number for {protocol} is {port}.")    

