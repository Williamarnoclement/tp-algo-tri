import random
import time

# Execution times
# array with  1000  entries ->  0,0  seconds
# array with  2000  entries ->  0,0009560585021972656  seconds
# array with  3000  entries ->  0,0  seconds
# array with  4000  entries ->  0,0010304450988769531  seconds
# array with  5000  entries ->  0,0  seconds
# array with  6000  entries ->  0,0010089874267578125  seconds
# array with  7000  entries ->  0,0009222030639648438  seconds
# array with  8000  entries ->  0,0009961128234863281  seconds
# array with  9000  entries ->  0,0009963512420654297  seconds
# array with  10000  entries ->  0,000997781753540039  seconds

#Enable generation of array with entries_number
def generate_array(entries_number: int) -> list[int]:
    array = [random.randint(0, 100) for i in range(entries_number)]
    return array

#Get execution time of algorithm
def get_execution_time(array: list[int]) -> float:
    start: float = time.time()
    list.sort(array)
    end: float = time.time()
    return end - start


arrays : list[list[int]] = []

#Generation of i * 1 000 arrays
for i in range(1, 11):
    arrays.append(generate_array(i * 1_000))

#Sorting algorithms and get execution times
for i in range(1, 11):
    print("array with ", i * 1000, " entries -> ", get_execution_time(arrays[i - 1]), " seconds")
