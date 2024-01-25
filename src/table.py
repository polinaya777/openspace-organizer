class Seat:
    '''A seat is a place where a person can sit. It can be free or occupied by a person'''
    def __init__(self, free=True, ocupant=''):
        self.free = free
        self.ocupant = ocupant

    def set_occupant(self, name):
        if self.free:
            self.ocupant = name
        else:
            print('This seat is already occupied!')
        
    def remove_occupant(self):        
        removed, self.ocupant = self.ocupant, ''
        self.free = True
        return removed
    
class Table:
    '''A table is a place where a group of people can sit. It has a capacity and a list of seats'''
    def __init__(self, capacity, seats=[]):
        self.capacity = capacity
        self.seats = seats

    def has_free_spot(self):
        return True if seat.free in (seat for seat in self.seats) else False
    
    def assign_seat(self, name):
        pass

    def capacity_left(self):
        return self.capacity - len(self.seats)

