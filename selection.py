import random
import time

# Execution times
# array with  1000  entries ->  0,03189420700073242  seconds
# array with  2000  entries ->  0,12358450889587402  seconds
# array with  3000  entries ->  0,2661125659942627  seconds
# array with  4000  entries ->  0,499269962310791  seconds
# array with  5000  entries ->  0,7794046401977539  seconds
# array with  6000  entries ->  1,046515703201294  seconds
# array with  7000  entries ->  1,4871025085449219  seconds
# array with  8000  entries ->  1,8356246948242188  seconds
# array with  9000  entries ->  2,171797513961792  seconds
# array with  10000  entries ->  2,5783119201660156  seconds

#Enable generation of array with entries_number
def generate_array(entries_number: int) -> list[int]:
    array = [random.randint(0, 100) for i in range(entries_number)]
    return array

#Enable permutation in an array with two indexes as input
def permutate_in_array(l: list[int], a: int , b: int)-> list[int]:
    tmp: int = l[a]
    l[a] = l[b]
    l[b] = tmp
    return l

#Selection sorting algorithm
def sort(array: list[int]) -> list[int]:
    for i in range(0, len(array)):
        min: int = i
        for j in range(i+1+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array = permutate_in_array(array, i, min)
    return array

#Get execution time of algorithm
def get_execution_time(array: list[int]) -> float:
    start: float = time.time()
    sort(array)
    end: float = time.time()
    return end - start


arrays : list[list[int]] = []

print(sort(generate_array(1_000)))


#Generation of i * 1 000 arrays
for i in range(1, 11):
    arrays.append(generate_array(i * 1_000))

#Sorting algorithms and get execution times
for i in range(1, 11):
    print("array with ", i * 1000, " entries -> ", get_execution_time(arrays[i - 1]), " seconds")
