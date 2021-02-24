##Create a ColouredDoor class that has the 'colour' attribute.
##
##Create a ClosedDoor class that has a default status of 'closed'.
##
##Create a ToggleDoor class that has a method toggle() that  toggles
##the status of the door.


class ColouredDoor1 :
    def __init__ (self, colour):
        self.colour = colour

door = ColouredDoor1 ("White")
print (door.colour)

class ColouredDoor2 :
    def __init__ (self, colour, status = "closed" ):
        self.colour = colour
        self.status = status

door = ColouredDoor2 ("White")
print (door.status)


class ToggleDoor:
    def __init__ (self, colour, status):
        self.colour = colour
        self.status = status

    def toggle(self):
        toggle_dict = {"opened" : "closed", "closed" : "opened"}
        self.status = toggle_dict [self.status]

door1 = ToggleDoor ("Red", "opened")
print (door1.status)
door1.toggle ()
print (door1.status)
door1.toggle()
print (door1.status)
        
