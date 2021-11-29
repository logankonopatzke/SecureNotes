import database
import crypt
import config

logged_in = False
current_username = config.DEFAULT_USER
current_password = ""

## Check if the current user is logged in
def get_logged_in():
    return logged_in

## Set the current user's authentication status
def set_logged_in(status):
    global logged_in
    logged_in = status

## Get the current user's username
def get_current_user():
    return current_username

## Set the current user's username
def set_current_user(username):
    global current_username
    current_username = username

## Get the current user's password
def get_current_pass():
    return current_password

## Set the current user's password
def set_current_pass(password):
    global current_password
    current_password = password

## Check through the database to check if the user exists
def user_exists(username, password):
    db = database.read()
    encrypted_password = crypt.encrypt(password, password)
    print("encp: {}".format(encrypted_password))
    for row in db:
        if row[0] == username and row[1] == encrypted_password:
            global logged_in
            logged_in = True
            return logged_in

## Attempt to log the user in assuming the credentials are valid
def login(username, password):
    if not user_exists(username, password):
        return False

    set_logged_in(True)
    set_current_user(username)
    set_current_pass(password)

    return True

## Log the user out and wipe local login credentials
def logout():
    set_logged_in(False)
    set_current_user("unknown")
    set_current_pass("")

    return True