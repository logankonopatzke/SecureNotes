import auth
import config
import database

def clear_console():
    print(('\n'*1000))

def get_user_input():
    print("{}@SecureNotes:~$ ".format(auth.get_current_user()), end='')
    user_input = input()

    clear_console()

    return user_input

## Displaying errors
def input_error():
    print("Error: Unknown input, please enter a valid command")

def auth_error():
    print("Error: You are not logged in")

def auth_fail_error():
    print("Error: Invalid username or password")

def auth_logged_in_error():
    print("Error: You are already logged in")

## Handle user input
def handle_input(user_input):
    ## Verify valid integer input
    try:
        user_input = int(user_input)
    except ValueError:
        user_input = 0


    if user_input == 1: ## Print help screen
        print_help_screen()

    elif user_input == 2: ## Log the user in
        if auth.get_logged_in(): ## The user is already logged in
            auth_logged_in_error()
            return

        print("Username: ", end='')
        username = input()

        print("Password: ", end='')
        password = input()

        clear_console()
        if auth.login(username, password): ## Attempt the login
            print("Welcome {}!".format(username))
        else:
            auth_fail_error()

    elif user_input == 3: ## Log the user out
        if not auth.get_logged_in(): ## User shouldn't be able to logout if they aren't logged in yet
            auth_error()
            return

        clear_console()

        print("Goodbye {}!".format(auth.get_current_user()))
        auth.logout()

    elif user_input == 4: ## Read data from the database
        if not auth.get_logged_in(): ## User shouldn't be able to read data if they aren't logged in yet
            auth_error()
            return

        data = database.read_data()
        print("Your data is: {}".format(data))

    elif user_input == 5: ## Write data into the database
        if not auth.get_logged_in(): ## User shouldn't be able to write data if they aren't logged in yet
            auth_error()
            return

        print("Data: ", end='')
        data = input()

        clear_console()

        if database.write_data(data):
            print("Data written successfully!")
        else:
            print("Error: Failed to write data!")

    elif user_input == 6: ## Exit the program
        print("Thank you for using {}!".format(config.PROGRAM_NAME))
        exit(0)

    else:
        input_error()

## Show the user the help screen
def print_help_screen():
    print("1. Help\n2. Login\n3. Logout\n4. Read Data\n5. Write Data\n6. Quit")

