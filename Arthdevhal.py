
class very_original_name:
    def __init__(self, name = "Bob"):
        self.my_name = name
        
        
    def introduction(self):
        print("Hello, my name is", self.my_name)


class very_original_pet:
    def __init__(self, animal = "Dog", name = "Max"):
        self.pet_is = animal
        self.pet_name = name


    def pet_does(self, sound = "woof"):
        print(self.pet_is, self.pet_name, sound)
