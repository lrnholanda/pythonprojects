squares = []
for value in range(1,11): 
    squares.append(value**2)

print(squares)    

# List Comprehensions
"""The following example builds the same list of square numbers"""

square = [valor**2 for valor in range(1,11)]
print(square)

#Execicios

for i in range(1,20):
    print(i)


#-2
milhao = list(range(1,100))  
for milho in milhao:    
    print(milho)


print(min(milhao))  
print(max(milhao))
print(sum(milhao))

#a list of the multiples of 3

tres = list(range(3,30,3))
for i in tres:
    print(i)


#cubes list
cubes = []
for value in range(1,10):
     cubes.append(value**3)

print(cubes)     

#cube list comprehension

cubes = [cube**3 for cube in range(1,10)]
print(cubes)
