from random import randint

class Seat:
    '''A seat is a place where a person can sit. It can be free or occupied by a person with a certain name'''
    seat_count = 0

    def __init__(self, free=True, ocupant=''):
        self.free = free
        self.ocupant = ocupant
        Seat.seat_count += 1
        self.seat_number = Seat.seat_count
        if self.seat_number == 4:
            Seat.seat_count = 0

    def set_occupant(self, name):
        if self.free:
            self.ocupant = name
            self.free = False
        else:
            print('This seat is already occupied!')
        
    def remove_occupant(self):
        if not self.free:
            removed, self.ocupant = self.ocupant, ''
            self.free = True
            return removed
        else:
            print('This seat is not occupied!')
            return None
    
class Table:
    '''A table is a place where a group of people can sit. It has a seat capacity and a list of seats'''
    table_count = 0
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]
        Table.table_count += 1
        self.table_number = Table.table_count
    
    def has_free_spot(self):
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name):
        if self.has_free_spot():
            while True:
                seat = self.seats[randint(0,3)]
                if seat.free:
                    seat.set_occupant(name)
                    break
            return True

    def capacity_left(self):
        return self.capacity - sum([not seat.free for seat in self.seats])

