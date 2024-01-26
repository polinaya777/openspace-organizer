import pandas as pd
from numpy import ndarray
from src.openspace import OpenSpace

def excel_file_to_list(filename: str):
    '''Import an Excel file and return a list of names'''
    df_names = pd.read_excel(filename)
    df_names.index = df_names.index + 1
    names_list = df_names.values.tolist()
    names_list = [name[1]+' '+name[0] for name in names_list]
    return names_list


def welcome():
    '''Display the welcome message'''
    print('''
    Welcome to the OpenSpace Organizer!
    This program will help you organize your colleagues in an OpenSpace.
    You can import a list of names from an Excel file.
    You can also export the result to an Excel file.\n''')
    return None

def menu():
    '''Display the menu'''
    menu = """Please select one of the following options:
    1 - Display the OpenSpace.
    2 - Import a list of persons names from an Excel file to organize them randomly in OpenSpace.
    3 - Add person/persons to the OpenSpace.
    4 - Remove a person from the OpenSpace.
    5 - Export the result to an Excel file.
    6 - Exit.

    Your selection: """
    return menu

def handel_menu_choice(choice: int, openspace: OpenSpace):
    '''Handle the user choice from the menu'''
    
    if choice == 1:
        openspace.display_df()
    
    elif choice == 2:        
        while True:
            try:
                path = input('Please indicate the path to an Excel file or press Enter for using default file: ')
                if path:
                    names = excel_file_to_list(path)
                    break
                else:
                    names = excel_file_to_list('colleagues2.xlsx')
                    break
            except:
                print('Please enter a valid path!\n')
        print(f'\nNames list to assign: {names}')
        openspace.organize(names)
    
    elif choice == 3:
        add_list = input('You want to add a person/persons to the OpenSpace.\nPlease enter the names separated by comma: ').split(",")
        add_list = [name.strip() for name in add_list]
        print(f'\nNames list to assign: {add_list}')
        openspace.organize(add_list)
    
    elif choice == 4:
        while True:
            try:
                table_num = int(input('You want to remove a person from the OpenSpace.\nPlease enter the number of the table: '))
                seat_num = int(input('Please enter the number of the seat: '))
                if openspace.tables[table_num-1].seats[seat_num-1].free:
                    print('This seat is already free!\n')
                    break
                else:
                    removed = openspace.tables[table_num-1].seats[seat_num-1].remove_occupant()
                    print(f'\n{removed} has been removed from the OpenSpace!\n')
                    break
            except:
                print('Please enter the valid option!\n')
    
    elif choice == 5:
        openspace.make_df().to_excel('result.xlsx')
        print('The result has been exported to an Excel file "result.xlsx"!\n')

    return None


def main():
    '''Main function'''
    openspace = OpenSpace(6)
    welcome()
    while True:
        try:
            user_choice = int(input(menu()))
            if user_choice in range(1,6):
                handel_menu_choice(user_choice, openspace)
            elif user_choice == 6:
                break
            else:
                print('Please select a valid option!')
        except:
            print('Please select a valid option!')    


if __name__ == "__main__":
    main()