import math



def dot_product(vector1,vector2):

    result = 0 
    for value1,value2 in zip(vector1,vector2):
        result += value1 * value2 
    return result 


def magnitude(vector):

    total = 0
    for value in vector:

        total += value**2 
    return math.sqrt(total) 


def cosine_similarity(vector1,vector2):
    
    dot = dot_product(vector1,vector2) 
    magnitude1 = magnitude(vector1) 
    magnitude2 = magnitude(vector2) 

    similarity = (dot/(magnitude1*magnitude2)) 

    return similarity 


# print(dot_product([1, 2, 3], [4, 5, 6]))
# print(magnitude([3, 4])) 
# print(cosine_similarity([1, 2, 3], [4, 5, 6]))