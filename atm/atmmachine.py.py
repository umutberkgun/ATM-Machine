#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("""

**********************
THIS IS AN ATM MACHINE

What you can do:

1) What's in my account?
2) Give me some money.
3) Let me put some money in it.

Press 'q' to exit.


**********************
""")


remainder = 100

while True:
    
    transaction = (input("watcha wanna do?"))
    
    
    if (transaction == "q"):
        print("come again some other time")
        break
        
        
        
    elif (transaction == "1"):
        print("here's what you have left {}" .format(remainder))
        
    elif (transaction == "2"):
        n = int(input("how much you wanna take?"))
        
        if n > 100:
            print("not happening")
            continue 
        
        remainder -= n
        print("here's whats left {}" .format(remainder))
        
    elif (transaction == "3"):
        n = int(input("how much you wanna add?"))
        remainder += n
        
        
        print("heres what you have {}" .format(remainder))
    
            
        



# In[ ]:





# In[ ]:





# In[ ]:




