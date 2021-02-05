'''
Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.  '''

def character( char ):
    if char == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
        return True
    else:
        return False
def main():
    print("\n -> Input ------->")
    char = input(" -> Enter the Character : ")
    print(" \n -> Output -------->")
    print(" -> " + str( character(char) ) + "\n" )
main()