# Assignment-3 
# list_comprehension

#______________________________________________________________________________________
### ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

input_list = ['x','y','z']                # item*num in input_list ranges from 1 to 5 
result = [item*num for item in input_list for num in range(1,5) ] 
print("['x','y','z'] => " +   str(result))
print("\r")

#______________________________________________________________________________________
### ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

input_list = ['x','y','z']
result = [item*num for num in range(1,5) for item in input_list ] 
print("['x','y','z'] => " +   str(result))
print("\r")

#______________________________________________________________________________________
### [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],

input_list1 = [2,3,4]
result1 =  [ [item+num] for item in input_list1 for num in range(0,3) ]
input_list2 = [2,3,4,5]
result2 =  [ [item+num for item in input_list2 ] for num in range(0,4) ]
print (str(result1) + " " + str(result2) )
print("\r")

#______________________________________________________________________________________
### [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

input_list = [1,2,3]
result = [ (b,a) for a in input_list for b in input_list ]
print("[1,2,3] => " +   str(result))
print("\r")