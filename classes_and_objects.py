class greetings:
    def __init__(self, name):
        self.name = name
    def morning(self):
        print("Good Morning " + self.name + "!")
    def noon (self):
        print("Good Afternoon" + self.name + "!")
    def evening(self):
        print("Good Evening" + self.name + "!")

# Creating class object 
obj = greetings("Lalasa Sathish")
# Calling class method
obj.morning()  
          