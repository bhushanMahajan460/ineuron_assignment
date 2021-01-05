# Assignment-3.2

############
# In Built filter function 

# Input the paramaters 
print("\r")
print("-> Input")
number = int(input("-> Insert a number : "))

num_list = list(range (1,number+1))

even_number = list (filter (lambda x :(x%2==0), list (filter (lambda y: (y%5==0) ,num_list ))))
odd_number = list (filter (lambda x :(x%2!=0), list (filter (lambda y: (y%5==0) ,num_list ))))

# output 
print("\r")
print("-> Output-1 (In Built Function )")
print("-> Even multiple of 5 : ",even_number)
print("-> Odd multiple of 5 : ",odd_number)

############
# myfilter function 

even_num = []
odd_num = []

def myfilter(number):
    for i in num_list :
        if i%2 == 0 :
            if i%5 == 0:
                even_num.append(i)
        else:
            if i%5 == 0 :
                odd_num.append(i)   
    
    return even_num , odd_num

# function execution 
even_result,odd_result = list(myfilter(number))

# output 
print("\r")
print("-> Output-2 (myfilter function) ")
print("-> Even multiple of 5 : ",even_result)
print("-> Odd multiple of 5 : ",odd_result)
#print("-> Odd multiple of 5 : ",odd_number)