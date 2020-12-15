class Pet:

    Cujo = Pet(0)
    Benji = Pet(1)

    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
    self.name = name
    self.fullness = fullness
    self.happiness = happiness
   

# Define functions that increase a pet's attribute levels.
    def eat_food(self):
        self.fullness += 30


    def get_love(self):
        self.happiness += 30

# Decrease a pet's attribute levels.
    def be_alive(self):
        self.fullness -= 5
        self.mopiness -= 5


    def __str__(self):
        return """
        %s
        Fullness: %d
     Happiness: %d
     """ % (self.name, self.fullness, self.happiness)

benji = Pet("Benji", 50, 20, 20, 1)
lassie = Pet("Lassie", 50, 20, 20, 1)
clifford = Pet("Old Yeller", 50, 20, 20, 1)

print(benji.fullness, benji.happiness)
