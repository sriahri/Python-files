class Alien: # Class Alien along with members
    def __init__(self, color, number_of_eyes, size): #Constructor
        self.color = color # Color of the Alien
        self.number_of_eyes = number_of_eyes # Number of eyes of the Alien
        self.size = size # Size of the Alien
    def toString(self):
        print('The Alien with',self.color,'has',self.number_of_eyes,'eyes and is a',self.size)

class Maritan(Alien):
    def __init__(self, color, number_of_eyes, size, blood_color):
        self.blood_color = blood_color # Blood color of the Maritan
        Alien.__init__(self, color, number_of_eyes, size) # Calling the constructor Alien

class Jupiterian(Alien):
    def __init__(self, color, number_of_eyes, size, face_shape):
        self.face_shape = face_shape # Face shape of the Jupiterian
        Alien.__init__(self, color, number_of_eyes, size) # Calling the constructor

maritan_obj = Maritan('red', 3, 'micro','green') # Creating the instance for Maritan class.
maritan_obj.toString() # Calling the toString() method
jupiterian_obj = Jupiterian('black', 4, 'macro', 'oval') # Creating the instance for Jupiterain class
jupiterian_obj.toString() # Calling the toString() method.