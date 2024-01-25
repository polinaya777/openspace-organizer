import pandas as pd
from numpy import ndarray
from src.openspace import OpenSpace

def excel_file_to_list(filename: str):
    try:
        df_names = pd.read_excel(filename)
        df_names.index = df_names.index + 1
        names_list = df_names.values.tolist()
        names_list = [name[1]+' '+name[0] for name in names_list]
        return names_list
    except:
        print('Error while importing file!')
        return None

def welcome():
    print('''
    Welcome to the OpenSpace Organizer!
    This program will help you organize your colleagues in an OpenSpace.
    You can import a list of names from an Excel file.
    You can also export the result to an Excel file.''')
    return None

def menu():    
    menu = """Please select one of the following options:
    1 - Check the OpenSpace.
    2 - Import a list of names from an Excel file.
    3 - Export the result to an Excel file.

    Your selection: """
    return menu

def handel_menu_choice(choice: int, openspace: OpenSpace):
    if choice == 1:
        openspace.display()
    elif choice == 2:
        names = excel_file_to_list('colleagues2.xlsx')
        print(f'Names list to assign: {names}')
        openspace.organize(names)
    elif choice == 3:
        pass

def main():
    openspace = OpenSpace(6)
    welcome()
    while True:
        try:
            user_choice = int(input(menu()))
            if user_choice in [1,2,3]:
                break
            else:
                print('Please select a valid option!')
        except:
            print('Please select a valid option!')
    handel_menu_choice(user_choice, openspace)


if __name__ == "__main__":
    main()