import os
from getch import getch
import requests

URL = 'http://127.0.0.1:5000/notes'

def clear_console():
    os.system('clear')

def press_any_key():
    getch()

def user_choice_add_new_note():
    pass

def user_choice_show_all_notes():
    data = requests.get(URL)
    print(data.text)
    press_any_key()

def user_choice_update_note():
    pass

def user_choice_delete_note():
    pass

def user_choice_search_note():
    pass

def user_choice_handler(user_choice: str):
    valid_input = ['1', '2', '3', '4', '5', '6']

    clear_console()
    if user_choice not in valid_input:
        print("Error, invalid input. Please try again.")
        print("Press any key.")
        press_any_key()
        return
    elif user_choice == '1':
        user_choice_add_new_note()
        return
    elif user_choice == '2':
        user_choice_show_all_notes()
        return
    elif user_choice == '3':
        user_choice_delete_note()
        return
    elif user_choice == '4':
        user_choice_update_note()
        return
    elif user_choice == '5':
        user_choice_search_note()
        return
    elif user_choice == '6':
        clear_console()
        print("Goodbye!")
        press_any_key()
        exit()