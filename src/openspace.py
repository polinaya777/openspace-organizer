import pandas as pd
from random import randint
from .table import Table
from tabulate import tabulate 

class OpenSpace:
    '''An OpenSpace class is a place where a group of people can sit. 
Attributes of class: number of tables, number of seats for each of tables and a list of tables.'''
    openspace_count = 0
    def __init__(self, number_of_tables, table_capacity):
        self.number_of_tables = number_of_tables
        self.tables = [Table(table_capacity) for i in range(number_of_tables)]
        OpenSpace.openspace_count += 1

    def organize(self, names):
        '''Organize the people randomly in the open space'''
        print(f'\nOrganizing {len(names)} people in {self.number_of_tables} tables...\n')
        for name in names:                
            while True:
                table = self.tables[randint(0,self.number_of_tables-1)]
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
        print(f'All people have been assigned to a seat.\nYou can enjoy the event!\n')
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
        total_seats = self.number_of_tables*self.tables[0].capacity
        free_seats = sum([seat.free for table in self.tables for seat in table.seats])
        print(f'Open space with {self.number_of_tables} tables with total {total_seats} seats from which {total_seats - free_seats} are occupied:')
        print(tabulate(self.make_df(), headers='keys', tablefmt='fancy_grid'))
        if all(not table.has_free_spot() for table in self.tables):
            print(f'All tables are occupied!\n')
        elif any(not table.has_free_spot() for table in self.tables):
            print(f'We still have {free_seats} free seats!\n')
        else:
            print(f'All tables are free!\n')
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