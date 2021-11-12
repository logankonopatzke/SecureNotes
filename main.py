import cli
import config

cli.clear_console()

print("Welcome to {}".format(config.PROGRAM_NAME))

print() ## Add some whitespace

cli.print_help_screen() ## Show the initial help screen

## Run until the user exits via the menu or force quits
while 1:
    user_input = cli.get_user_input()
    cli.handle_input(user_input)