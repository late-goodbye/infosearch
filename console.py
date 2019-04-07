def mainloop():

    is_running = True
    print("Welcome to the app console!")

    while is_running:
        print(">", end=" ")
        command = input()

        if command in ('exit', 'close', 'quit'):
            is_running = False
        else:
            print("Command has not been recognized. Try again.")
            pass
    else:
        print("Thank you for using this app. Goodbye.")
