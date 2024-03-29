import pandas as pd
from numpy import ndarray
from src.openspace import OpenSpace

def create_openspace():
    '''Create an OpenSpace'''
    print('First we need to create an OpenSpace.')
    while True:
        user_input = input('Do you want to create your own OpenSpace (Y) or use the default one (N)? ').lower()
        if user_input == 'y':
            while True:
                try:
                    number_of_tables = int(input('Please enter the number of tables: '))
                    table_capacity = int(input('Please enter the number of seats for each table: '))
                    break
                except:
                    print('Please enter a valid number!\n')
            openspace = OpenSpace(number_of_tables, table_capacity)
            break
        elif user_input == 'n':
            openspace = OpenSpace(6, 4)
            break
        else:
            print('Please enter Y or N!\n')
    print(f'OpenSpace with {openspace.number_of_tables} tables and {openspace.tables[0].capacity} seats for each table has been created!\n')
    return openspace

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
    Default OpenSpace has 6 tables with 4 seats each. 
    But you can create your own OpenSpace with any set up.
    You can import a list of names from an Excel file to organize them randomly in OpenSpace.
    You can also export the result to an Excel file.\n''')
    return None

def menu():
    '''Display the menu'''
    menu = """Please select one of the following options:
    1 - Display the OpenSpace.
    2 - Import a list of persons names from an Excel file.
    3 - Add person/persons to the OpenSpace.
    4 - Remove a person from the OpenSpace.
    5 - Export the result to an Excel file.
    6 - Exit.

    Your selection: """
    return menu

def handel_menu_choice(choice: int, openspace: OpenSpace):
    '''Handle the user choice from the menu'''
    match choice:
        case 1:
            openspace.display_df()
    
        case 2:        
            while True:
                try:
                    path = input('Please indicate the path to an Excel file or press Enter for using default file: ')
                    if path:
                        names_list = excel_file_to_list(path)
                        break
                    else:
                        names_list = excel_file_to_list('colleagues2.xlsx')
                        break
                except:
                    print('Please enter a valid path!\n')
            free_seats = sum([seat.free for table in openspace.tables for seat in table.seats])
            total_seats = openspace.number_of_tables*openspace.tables[0].capacity
            print(f'\nWe have {free_seats} free seats in the OpenSpace.')
            print(f'\nNames list to assign: {names_list}')
            try:                
                if len(names_list) > total_seats:
                    print(f'''\nThere are not enough seats for {len(names_list)} people in this OpenSpace! You need to use the bigger one.\n''')
                elif len(names_list) <= free_seats:
                    openspace.organize(names_list)
                    return True            
                else:
                    print(f'''\nThere are not enough free seats for {len(names_list)} people!
    You can add maximum {free_seats} people or at first remove people from the OpenSpace.\n''')
            except:
                print('\nSomething went wrong with organizing people\n')
    
        case 3:        
            while True:
                try:
                    add_list = input('''You want to add a person/persons to the OpenSpace.
    Please enter the names separated by comma: ''').split(",")
                    add_list = [name.strip() for name in add_list]
                    break
                except:
                    print('Your enter is not valid!\n')
            free_seats = sum([seat.free for table in openspace.tables for seat in table.seats])
            total_seats = openspace.number_of_tables*openspace.tables[0].capacity
            print(f'\nWe have {free_seats} free seats in the OpenSpace.')
            print(f'Names list to assign: {add_list}')        
            try:                
                if len(add_list) > total_seats:
                    print(f'''\nThere are not enough seats for {len(add_list)} people in this OpenSpace! You need to use the bigger one.\n''')
                elif len(add_list) <= free_seats:
                    openspace.organize(add_list)
                    return True
                else:
                    print(f'''\nThere are not enough free seats for {len(add_list)} people!
    You can add maximum {free_seats} people or at first remove people from the OpenSpace.\n''')
            except:
                print('Something went wrong with adding people\n')
    
        case 4:
            while True:
                try:
                    table_num = int(input('''You want to remove a person from the OpenSpace.
    Please enter the number of the table: '''))
                    seat_num = int(input('Please enter the number of the seat: '))
                    if openspace.tables[table_num-1].seats[seat_num-1].free:
                        print('This seat is already free!\n')
                        break
                    else:
                        removed = openspace.tables[table_num-1].seats[seat_num-1].remove_occupant()
                        print(f'\n{removed} has been removed from the OpenSpace!')
                        print(f'Now we have {sum([seat.free for table in openspace.tables for seat in table.seats])} free seats in the OpenSpace.\n')
                        break
                except:
                    print('Please enter a valid number of table and/or seat!\n')
    
        case 5:
            openspace.make_df().to_excel('result.xlsx')
            print('The result has been exported to an Excel file "result.xlsx"!\n')

    return None


def main():
    '''Main function'''    
    welcome()
    openspace = create_openspace()
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