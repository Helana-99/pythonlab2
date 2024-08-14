# q2

def character_locator():
    sentence = input("Enter a sentence: ")
    letter = input("Enter the letter: ")

    find = [i for i, char in enumerate(sentence) if char == letter]
    print(f"The letter '{letter}' is found at find: {find}")
character_locator()

# q3

def multi_table(n):
    table = []
    for i in range(1, n + 1):
        row = [i * j for j in range(1, i + 1)]
        table.append(row)
    return table

num = int(input("Enter a number: "))
result = multi_table(num)
print(result)

# q4

def name(names):
    dictionary = {}
    for name in names:
        key = name[0]
        
        if key in dictionary:
            dictionary[key].append(name)
        else:
            dictionary[key] = [name]
        dictionary = dict(sorted(dictionary.items()))
    
    return dictionary
names_input = input("Enter a list of names:")

names_list = [name.strip() for name in names_input.split(",")]

result = name(names_list)
print("Sorted Dictionary:")
print(result)

# q1

import math
def calculate_area(shape, dim1, dim2=0, dim3=0):
    if shape == 'circle':
        return math.pi * (dim1 ** 2)
    elif shape == 'rectangle':
        return dim1 * dim2
    elif shape == 'triangle':
        if dim3 == 0:
            return 0.5 * dim1 * dim2
        else:
            s = (dim1 + dim2 + dim3) / 2
            return math.sqrt(s * (s - dim1) * (s - dim2) * (s - dim3))
    elif shape == 'square':
        return dim1 * dim1
    else:
        return 'Invalid shape'
    
shape = input("Enter the shape (circle, rectangle, triangle, square): ").lower()

if shape == 'circle':
    dim1 = float(input(f"Enter the radius: "))
    area = calculate_area(shape, dim1)
elif shape == 'square':
    dim1 = float(input(f"Enter the side length: "))
    area = calculate_area(shape, dim1)
elif shape == 'rectangle':
    dim1 = float(input("Enter the length: "))
    dim2 = float(input("Enter the width: "))
    area = calculate_area(shape, dim1, dim2)
elif shape == 'triangle':
    dim1 = float(input("Enter the first side length: "))
    dim2 = float(input("Enter the second side length: "))
    dim3 = float(input("Enter the third side length: "))
    area = calculate_area(shape, dim1, dim2, dim3)
else:
    area = "Invalid shape"

print(f"The area of the {shape} is: {area}")

