from random import randint
from .table import Table 

class OpenSpace:
    '''An open space is a place where a group of people can sit. It has a capacity and a list of tables'''
    def __init__(self, number_of_tables=6):
        self.number_of_tables = number_of_tables
        self.tables = [Table() for x in range(number_of_tables)]

    def organize(self, names):
        if len(names) > sum([table.capacity for table in self.tables]):
            raise Exception('There are not enough seats for all the people!\nUse other OpenSpace or remove some people!\n')
        else:
            print(f'Organizing {len(names)} people in {self.number_of_tables} tables...\n')
            for name in names:                
                while True:
                    table = self.tables[randint(0,5)]
                    if table.has_free_spot():
                        table.assign_seat(name)
                        break
            print(f'All people have been assigned to a seat!\n')
            self.display()
            return True
    
    def display(self):
        print(f'Open space with {self.number_of_tables} tables:')
        if any(not table.has_free_spot() for table in self.tables):
            for table in self.tables:
                print(f'Table_{table.table_number} with {table.capacity} seats has {table.capacity_left()} free seats:')
                for seat in table.seats:
                    if not seat.free:
                        print(f'\tSeat_{seat.seat_number} is occupied by {seat.ocupant}')
                    else:
                        print(f'\tSeat_{seat.seat_number} is free')
        else:
            print(f'All tables are empty!\n')                
        return None

    def store(filename):
        pass