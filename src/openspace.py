from table import Table 

class OpenSpace:
    '''An open space is a place where a group of people can sit. It has a capacity and a list of tables'''
    def __init__(self, number_of_tables, tables=[*Table]):
        self.number_of_tables = number_of_tables
        self.tables = [Table]*number_of_tables

    def organize(self, names):
        pass
    
    def display(self):
        print(f'Open space with {self.number_of_tables} tables:')
        for table in self.tables:
            print(f'Table{table.number} with {table.capacity} seats:')
            for seat in table.seats:
                print(f'Seat{seat.number} is occupied by {seat.ocupant}')

    def store(filename):
        pass