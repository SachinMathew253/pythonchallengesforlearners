# find squares of a number using lamda function

square = lamda x: x**2
for i in range(1,16):
    print(square(i))
    
 
 # finda square of numbers 1-15 using map and list
 
 a_map = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
 nw_map = list(map(lamda x:x**2 , a_map))
 print (nw_map)
