'''
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"]. 

Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.   '''

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]     

result =  [( sub + " " +  verb + " " + obj + "." ) for sub in subjects for verb in verbs for obj in objects ]

print("\n -> Output : ")

for changeline in result :
    print(changeline)





