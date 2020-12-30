#ASSIGNMENT 1
# Print the numbers separated with commas divisible by 7 but not multiple of 5 between 2000 and 3200

for i in range(1999,3201):
    if (i%7==0 and i%5!=0):
        print(i,end=" ,")      # end is used to print the separated commas 
        i=i+1
    else:
        i=i+1
