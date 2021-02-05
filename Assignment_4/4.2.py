'''
Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list. ''' 

def cal_integer( string ):
    a = []
    for i in range ( len(string) ):
        num = len( string[i] )
        a.append(num)
    return a  

def main():
    print("\n -> Input ------->")
    words = input(" -> Enter the words : ").split(",")
    words1 = cal_integer( words )
    print("\n -> Output ------->")
    print(" -> Length of strings : " + str(words) + " are : " + str(words1) + " . \n" )
main() 
