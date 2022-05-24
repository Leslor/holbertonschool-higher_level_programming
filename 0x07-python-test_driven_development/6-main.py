#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([-1, -3, float('nan'),-8]))
print(max_integer([1, 3, 8, float('inf'), float('nan')]))
#print(max_integer((1, 1.75, 1.5))) -> consultar
#print(max_integer({1:'Number', 3:'Recursion', 4:'python'})) -> Raise Error
print(max_integer(['1', '2', '3', '4']))
#print(max_integer([1, 'string1', '2', 4]))->no support < operator betwee an string
print(max_integer([None]))
print(max_integer())
print(max_integer(['string1', 'string0', 'string2', 'Hi']))
print(max_integer([1]))
#print(max_integer(None))-> TypeError: object of type 'NoneType' has no len()
print(max_integer([float('nan'), float('nan'), float('nan'), float('nan')]))
print(max_integer([float('inf'), float('inf'), float('inf'), float('inf')]))

