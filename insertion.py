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

def insertion_sorting(array: list[int]) -> list[int]:
    for j in range(0,len(array)):
        incr: int = j
        while(j > 0):
            if(array[j-1]> array[j]):
                array = permutate_in_array(array, j, j-1)
            print("--", array)
            j=j-1
    return array

def insertion_sorting_and_get_execution_time(array: list[int]) -> int:
    start: float = time.time()
    for j in range(0,len(array)):
        incr: int = j
        while(j > 0):
            if(array[j-1]> array[j]):
                array = permutate_in_array(array, j, j-1)
            #print("--", array)
            j=j-1
    end: float = time.time()
    return end - start
    

arrays : list[list[int]] = []

#Generation of i * 1 000 arrays
#for i in range(1, 11):
#    arrays.append(generate_array(i * 1_000))

#Sorting algorithms and get execution times
#for i in range(1, 11):
#    print("array with ", i * 1_000, " entries -> ", insertion_sorting_and_get_execution_time(arrays[i]), " seconds")

arr_test: list[int] = generate_array(7)

print(arr_test)
print(insertion_sorting(arr_test))