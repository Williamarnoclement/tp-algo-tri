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

def merge(arr1: list[int], arr2: list[int]):

