class Student:
    def __init__(self, name, major, gpa, on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.on_probation = on_probation

    def on_honor_roll(self):
        if self.gpa >= 8.0:
            return True
        else:
            return False
