#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#User login application
user_name = "Seyma"
password ="zKn6"

user_name1 = input("Please enter your user name")
password1 = input("Please enter your password.")

if (user_name == user_name1 and password == password1):
    print("Hi,",user_name1 +"." + " You are now logged in...")
elif (user_name != user_name1 or password != password1):
    print("Invalid user name or password")
    


# In[ ]:


#User login application with using dictionary
user_informations = {
                     "User1": {"name":"Seyma","password": "zKn6"}, 
                     "User2": {"name": "Marie","password": "gkh.5"}
                    }

user_name1 = input("Please enter your user name")
password1 = input("Please enter your password")

for x in user_informations:
    if  (user_informations.get(x).get("name") != user_name1 or user_informations.get(x).get("password") != password1):
        continue
    elif (user_informations.get(x).get("name") == user_name1 and user_informations.get(x).get("password") == password1):
            print("Hi,",user_name1 +"." + " You are now logged in...")
    break
if  (user_informations.get(x).get("name") != user_name1 or user_informations.get(x).get("password") != password1):
    print("Invalid user name or password")
        

