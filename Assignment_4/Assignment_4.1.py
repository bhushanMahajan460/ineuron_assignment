"""
Assignment 4.1
Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""

class Parent:                                         # Parent class 
    def __init__( self , s1, s2, s3 ):                # internally get called and initialized when arguments are passed 
       self.s1 = s1 
       self.s2 = s2 
       self.s3 = s3

    def __str__(self):                                # internally get called when we try to print the object 
        return "\n -> I am Parent Class . Sides are : %d , %d , %d " % (self.s1,self.s2,self.s3)

parent_object = Parent( 1 , 2 , 3 )
print(parent_object)

class Subclass( Parent ):
    def __init__ ( self , triangle_id , *args ):
        super ( Subclass , self ). __init__ ( *args )      # "SUPER" , class of child class calling parent class objects 
        self.triangle_id = triangle_id 

    def area_cal( self , s1 , s2 , s3 ) :
        s = ( self.s1 + self.s2 + self.s3 ) / 2
        return ( (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5 )

subclass_object = Subclass ( 1 , 1 , 2 , 3 )
print( "\n -> triangle id = %d " % ( subclass_object.triangle_id ))

print ("\n -> I am Subclass . Area of triangle = " + str( subclass_object.area_cal( 1 , 2 , 3 )) + ' . \n')