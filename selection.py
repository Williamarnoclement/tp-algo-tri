import random
import time

#Enable generation of array with entries_number
def generate_array(entries_number: int) -> list[int]:
    array = [random.randint(0, 100) for i in range(entries_number)]
    return array

def permutate_in_array(l: list[int], a: int , b: int)-> list[int]:
    tmp: int = l[a]
    l[a] = l[b]
    l[b] = tmp
    return l

def selection_sorting(array: list[int]) -> list[int]:
    for i in range(0, len(array)):
        min: int = i
        for j in range(i+1+1, len(array)):
            if(array[j] < array[min]):
                array = permutate_in_array(array, j, min)
    return array
            
def selection_sorting_and_get_execution_time(array: list[int]) -> int:
    start: float = time.time()
    for i in range(0, len(array)):
        min: int = i
        for j in range(i+1+1, len(array)):
            if(array[j] < array[min]):
                array = permutate_in_array(array, j, min)
    end: float = time.time()
    return end - start;
    

arrays : list[list[int]] = []

#Generation of i * 1 000 arrays
for i in range(1, 11):
    arrays.append(generate_array(i * 1_000))

#Sorting algorithms and get execution times
for i in range(1, 11):
    print("array with ", i * 1_000, " entries -> ", selection_sorting_and_get_execution_time(arrays[i]), " seconds")
