
##Modify the Door class adding a class attribute 'status' with  value 'undefined'.
##Does it work? What happens to instances?
##
##Modify the Door class adding a class attribute 'status' with  value 'closed'
##and remove status from __init__. Does it work?
##
##Add a toggle() method to the previous class. What happens if  you call toggle()
##on a fresh instance? Why?

class Door:
    status = "closed"
    def __init__ (self, color):
        self.color = color
        #self.status = status

    def open (self):
        self.status = "Opened"

    def close (self):
        self.status = "Closed"

    def toggle (self):
       togl_dict = {"opened" : "closed", "closed" : "opened"}
       self.status = togl_dict[self.status]
    
door1 = Door ("black")
print (door1.status)
print (Door.status)
door1.toggle ()
print (door1.status)
door1.toggle ()
print (door1.status)
