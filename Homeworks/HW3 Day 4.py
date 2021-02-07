#!/usr/bin/env python
# coding: utf-8

# In[1]:


#finding prime number between 0-100 by using fumctions
def prime_numbers (a):
    for num in range(2,a):
        for i in range ( 2, 100):
            if (num % i == 0 and num !=i):
                break
            i+=1
        else:
            print(num,"is a prime number")  
prime_numbers(100)

