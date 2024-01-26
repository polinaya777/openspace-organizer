import pandas as pd
from random import randint
from .table import Table
from tabulate import tabulate 

class OpenSpace:
    '''An open space is a place where a group of people can sit. It has a capacity and a list of tables'''
    def __init__(self, number_of_tables=6):
        self.number_of_tables = number_of_tables
        self.tables = [Table() for x in range(number_of_tables)]

    def organize(self, names):
        if len(names) > sum([table.capacity for table in self.tables]):
            raise Exception('There are not enough seats for all the people!\nUse other OpenSpace or remove some people!\n')
        else:
            print(f'\nOrganizing {len(names)} people in {self.number_of_tables} tables...\n')
            for name in names:                
                while True:
                    table = self.tables[randint(0,5)]
                    if table.has_free_spot():
                        table.assign_seat(name)
                        break
            print(f'\nAll people have been assigned to a seat.\nYou can enjoy the event!\n')
            self.display_df()
            return True
    
    def make_df(self):
        '''Make a Pandas DataFrame of the open space'''
        dict_of_seats = {'Seat_'+str(i+1): [table.seats[i].ocupant for table in self.tables] for i in range(self.tables[0].capacity)}
        columns_seats = ['Seat_'+str(i) for i in range(1,self.tables[0].capacity+1)]
        index_seats = ['Table_'+str(i) for i in range(1,self.number_of_tables+1)]
        openspace_seats_df = pd.DataFrame(dict_of_seats, columns=columns_seats, index=index_seats)
        return openspace_seats_df

    def display_df(self):
        '''Display the open space through a Pandas DataFrame and dictionary of seats'''        
        print(f'Open space with {self.number_of_tables} tables with total {self.number_of_tables*self.tables[0].capacity} seats:')
        print(tabulate(self.make_df(), headers='keys', tablefmt='fancy_grid'))
        if not any(not table.has_free_spot() for table in self.tables):
            print(f'All tables are free!\n')
        elif all(not table.has_free_spot() for table in self.tables):
            print(f'All tables are occupied!\n')
        else:
            print(f'We still have free seats!\n')
        return None
    
    def display_print(self):
        '''Display the open space through a print statement'''
        print(f'Open space with {self.number_of_tables} tables with total {self.number_of_tables*self.tables[0].capacity} seats:')
        if any(not table.has_free_spot() for table in self.tables):
            for table in self.tables:
                print(f'Table_{table.table_number} with {table.capacity} seats has {table.capacity_left()} free seats:')
                for seat in table.seats:
                    if not seat.free:
                        print(f'\tSeat_{seat.seat_number} is occupied by {seat.ocupant}')
                    else:
                        print(f'\tSeat_{seat.seat_number} is free')
        else:
            print(f'All tables are free!\n')
        return None 

    def store(filename):
        pass