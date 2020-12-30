# ASSIGNMENT_2 - A
# PRINT THE PATTERN USING FOR LOOP

for i in range (0,8):                              # ROWS INITIALIZATION 
    if(i<5):                                       # PATTERN CHANGE
            for j in range(0,i+1):                 # COLUMN IMPLIMENTATION 
                 print("* ",end=" ")
    else:
          for j in range(0,9-i):
              print("* ",end=" ")

    print("\r")                                     # CHANGE THE ROW 

    






           
 