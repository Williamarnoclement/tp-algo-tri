import random
import time

# Execution times
# array with  1000  entries ->  0,0030167102813720703  seconds
# array with  2000  entries ->  0,00495600700378418  seconds
# array with  3000  entries ->  0,00697636604309082  seconds
# array with  4000  entries ->  0,01196146011352539  seconds
# array with  5000  entries ->  0,014969587326049805  seconds
# array with  6000  entries ->  0,018938064575195312  seconds
# array with  7000  entries ->  0,021984577178955078  seconds
# array with  8000  entries ->  0,02689218521118164  seconds
# array with  9000  entries ->  0,03088855743408203  seconds
# array with  10000  entries ->  0,03587532043457031  seconds

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

#Enable merging between to arrays as inputs
#Behind this idea, this function has to receive kind of pre-sorted content,
#and will merge efficiently list of integers
def merge(arr1: list[int], arr2: list[int]) -> list[int]:#utiliser left_array et right_array la prochaine fois
    index_arr_1: int = 0
    index_arr_2: int = 0
    new_arr: list[int] = []
    while(index_arr_1 < len(arr1) and index_arr_2 < len(arr2)):
        if(arr1[index_arr_1] <= arr2[index_arr_2]):
            new_arr.append(arr1[index_arr_1])
            index_arr_1 = index_arr_1 + 1
        else:
            new_arr.append(arr2[index_arr_2])
            index_arr_2 = index_arr_2 + 1
    if index_arr_1 == len(arr1):
        return new_arr+arr2[index_arr_2:]
    else:
        return new_arr+arr1[index_arr_1:]


#Fusion sorting algorithm, powered by a recursive method
#this will allow you to divide as multiple parts your
#list of integers to sort it as sub-list of one elements.
#After this step, it will compute a merging function
def sort(l: list[int]) -> list[int]:
    if(len(l) <= 1):
        return l
    return merge(sort(l[0:(len(l)//2)]), sort(l[(len(l)//2):]))


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
