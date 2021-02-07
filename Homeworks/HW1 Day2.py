#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#created list
mylist = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 5 :   #swapped the second half of the list with the first half of the list 
    x = mylist[i]
    mylist[i] = mylist[i+5]
    mylist[i+5]=x
    i+=1
print(mylist)    #printed list 


# In[ ]:

#asked to user to write a number
n = int(input("Please write a single digit integer"))
for i in range (0,n+1,2):
    print(i)
#then printed all the even numbers even from 0 to n (if n even number,it is included)

# In[ ]:




