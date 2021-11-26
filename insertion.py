import random
import time

# Execution times
# array with  1000  entries ->  0,08770394325256348  seconds
# array with  2000  entries ->  0,3737215995788574  seconds
# array with  3000  entries ->  0,8502507209777832  seconds
# array with  4000  entries ->  1,487036943435669  seconds
# array with  5000  entries ->  2,3162457942962646  seconds
# array with  6000  entries ->  3,372101306915283  seconds
# array with  7000  entries ->  4,257158994674683  seconds
# array with  8000  entries ->  6,215287685394287  seconds
# array with  9000  entries ->  7,258023023605347  seconds
# array with  10000  entries ->  9,038335084915161  seconds

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

#Insertion sorting algorithm
def sort(array: list[int]) -> list[int]:
    for j in range(0,len(array)):
        while(j > 0 and array[j-1]<= array[j]):
            array = permutate_in_array(array, j, j-1)
            j=j-1
    return array

#Get execution time of algorithm
def get_execution_time(array: list[int]) -> float:
    start: float = time.time()
    sort(array)
    end: float = time.time()
    return end - start

arrays : list[list[int]] = []

#Generation of i * 1 000 arrays
for i in range(1, 11):
    arrays.append(generate_array(i * 1_000))

#Sorting algorithms and get execution times
for i in range(1, 11):
    print("array with ", i * 1000, " entries -> ", get_execution_time(arrays[i - 1]), " seconds")
