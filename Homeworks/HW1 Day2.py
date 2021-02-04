#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mylist = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 5 :
    x = mylist[i]
    mylist[i] = mylist[i+5]
    mylist[i+5]=x
    i+=1
print(mylist)


# In[ ]:


x = int(input("Please write a number"))
for i in range (0,x+1,2):
    print(i)


# In[ ]:




