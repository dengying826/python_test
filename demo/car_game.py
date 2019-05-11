# car game
started = False
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started.")
        else:
            print("Car started.")
            started = True

    elif command == "stop":
        if not started:
            print("Car already stopped.")
        else:
            print("Car stopped.")
            started = False
    elif command == "quit":
        break
    elif command == "help":
        print("""start - to start the car\nstop - to stop the car\nquit - to exit""")
    else:
        print("Sorry, I don't understand that...")
