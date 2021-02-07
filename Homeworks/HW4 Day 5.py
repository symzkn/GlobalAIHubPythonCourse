#!/usr/bin/env python
# coding: utf-8

# In[4]:


#created three class and defined functions and used inheritance
class Animals:
    def __init__(self, name, species_name, legs_number, tail_feature):
        self.name = name
        self.species = species_name
        self.legs = legs_number
        self.tail = tail_feature
    
    def print_name(self):
        print(self.name)
    
    def print_species(self):
        print(self.name + " is " +  self.species)
    
    def print_legs(self):
        print(self.name + " has got " + self.legs + " legs. "  )

    def showInfo(self):
        print("{} is {} . It has {} legs. It has got {} tail. ".format(self.name,self.species,self.legs,self.tail))

class Dogs(Animals):
    pass
class Cats(Animals):
    pass


# In[5]:


#added system to information about dog1 and cat1
Cat1 = Cats("Yabani", "Van cat", "4", "long")
Dog1 = Dogs("Hussley", "Siberian Husky", "4", "long")

