from console_app_functions import clear_console, user_choice_handler

def main():
    while True:
        clear_console()
        print("1 - Add note")
        print("2 - Show notes")
        print("3 - Update note")
        print("4 - Delete note")
        print("5 - Search note")
        print("6 - Exit")
        user_choice = input("Enter your choice: ")
        user_choice_handler(user_choice)

if __name__ == "__main__":
    main()