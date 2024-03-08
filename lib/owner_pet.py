class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = [] 

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise ValueError(f"Invalid pet_type: {pet_type}")

        self.name = name
        self.owner = owner
        self.__class__.all_pets.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_owned = [] 

    def add_pet(self, pet):
       
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
       
        pet.owner = self
        self.pets_owned.append(pet)

    def pets(self):
        return self.pets_owned

    def get_sorted_pets(self):
      
        return sorted(self.pets_owned, key=lambda pet: pet.name)