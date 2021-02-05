'''
Assignment 4.1.2
A function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
'''

def filter_long_words( string , n ):
    a = []
    for i in range(len(string)):
        if len( string[i] ) > n :
            a.append ( string[i] )
    return a

def main():
    print("\n -> Input ------>")
    n = int(input(" -> Enter the integer : "))
    words = (input(" -> Enter the list of words : ").split(" "))
    word1 = filter_long_words( words , n )
    print("\n -> Output ------>")
    print(" -> List of words : " + str(word1) + " , greater than integer " + str(n) + " . \n")
main()
        
