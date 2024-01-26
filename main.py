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
    2 - Import a list of persons names from an Excel file to organize them randomly.
    3 - Add a person to the OpenSpace.
    4 - Remove a person from the OpenSpace.
    5 - Export the result to an Excel file (result.xlsx).
    6 - Exit.

    Your selection: """
    return menu

def handel_menu_choice(choice: int, openspace: OpenSpace):
    if choice == 1:
        openspace.display_df()
    elif choice == 2:
        names = excel_file_to_list('colleagues2.xlsx')
        print(f'Names list to assign: {names}')
        openspace.organize(names)
    elif choice == 3:
        pass
    elif choice == 4:
        while True:
            try:
                table_num = int(input('You want to remove a person from the OpenSpace.\nPlease enter the number of the table: '))
                seat_num = int(input('Please enter the number of the seat: '))
                if openspace.tables[table_num-1].seats[seat_num-1].free:
                    print('This seat is already free!')
                    break
                else:
                    removed = openspace.tables[table_num-1].seats[seat_num-1].remove_occupant()
                    print(f'{removed} has been removed from the OpenSpace!')
                    break
            except:
                print('Please enter the valid option!\n')
    elif choice == 5:
        openspace.make_df().to_excel('result.xlsx')
    elif choice == 6:
        exit()

def main():
    openspace = OpenSpace(6)
    welcome()
    while True:
        try:
            user_choice = int(input(menu()))
            if user_choice in range(1,6):
                break
            else:
                print('Please select a valid option!')
        except:
            print('Please select a valid option!')
    handel_menu_choice(user_choice, openspace)


if __name__ == "__main__":
    main()