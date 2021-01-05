# -> Assignment - 3.1
# -> myreduce function 

# -> Input the parameters 
print("-> Input")
number = int(input("-> Enter a Number : "))

# -> function defined
def myreduce(number):
    num_list = list(range(1,number+1))
    even_numbers = filter(lambda x:(x%2==0),num_list) 
    return even_numbers 

# -> Function Execution 
result = list(myreduce(number))

# -> Output
print("-> Output 'myreduce function' ")
# print("-> list of numbers :",num_list)
print("-> Even numbers : ", result ) 
