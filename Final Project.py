#!/usr/bin/env python
# coding: utf-8

# In[1]:


#company management system
class employees():    
    def __init__(self, first_name, last_name, age, language):
        self.name = first_name
        self.lname = last_name
        self.age = age
        self.language = language

    def showName(self):
        print (self.name + " " + self.lname)
        
#with this function we show person can speak which language    
    def showlanguage(self):
        print(self.name + " " + self.lname,"can speak:", self.language)

class company_managers(employees):   
    pass


# In[2]:


Employee1 = employees("Mehmet","Selim",30,"French")
Employee2 = employees ("Mehmet","Selim",30,"French")
Manager1 = company_managers ("Johny","Deep",25,"French")

#with this function we show any of the person can speak which language   
Employee1.showlanguage()

