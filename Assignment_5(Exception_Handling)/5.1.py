'''
Assignment 5.1 
A function to compute 5/0 and use try/except to catch the exceptions. '''

def div():
    return 5/0 

try:
    div()
except ZeroDivisionError as zd :
    print("\n -> Oops! Invalid Division .")
    print( zd )
except:
    print("\n -> Any Other error ocurrred .")
finally :
    print(" -> Exception Hnadling Assignment \n")


