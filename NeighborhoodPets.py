# Author: Kristin Towns
# GitHub: kristinlashun
# Date: 2/7/2024
# Description: This class manages pet data, allowing addition, deletion, and look-up of pets,
# and saving/loading the data to and from a JSON file.

import json

class DuplicateNameError(Exception):
    """Exception raised when a duplicate pet name is encountered."""
    pass

class NeighborhoodPets:
    def __init__(self):
        """Initialize the NeighborhoodPets object."""
        self.__pets = {}

    def add_pet(self, name, species, owner):
        """Add a pet to the collection."""
        if name in self.__pets:
            raise DuplicateNameError(f"A pet with the name '{name}' already exists.")
        self.__pets[name] = {'species': species, 'owner': owner}

    def delete_pet(self, name):
        """Delete a pet from the collection."""
        if name in self.__pets:
            del self.__pets[name]

    def get_owner(self, name):
        """Return the name of the owner of the pet."""
        return self.__pets.get(name, {}).get('owner')

    def save_as_json(self, filename):
        """Save the pets data to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.__pets, file)

    def read_json(self, filename):
        """Read pet data from a JSON file."""
        with open(filename, 'r') as file:
            self.__pets = json.load(file)

    def get_all_species(self):
        """Return a set of the species of all pets."""
        return set(pet['species'] for pet in self.__pets.values())

