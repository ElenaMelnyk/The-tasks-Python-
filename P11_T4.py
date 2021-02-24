##Modify the Door class adding a class method 'paint' that accepts  a 'colour'
##argument and changes the class attribute 'colour’.
##
##Modify the Door class adding both a class method 'paint' and a  standard method
##'paint'. What happens?

class Door:
    def __init__ (self, colour, status):
        self.colour = colour
        self.status = status

    def paint (self, colour):
        self.colour = colour

    @classmethod
    def paint (cls,colour):
        cls.colour = colour
