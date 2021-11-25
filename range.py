import time
import random

# Execution times
# array with  1000000  entries ->  0,7604422569274902
# array with  2000000  entries ->  1,4301798343658447
# array with  3000000  entries ->  1,8408622741699219
# array with  4000000  entries ->  2,3821256160736084
# array with  5000000  entries ->  3,3159019947052
# array with  6000000  entries ->  3,841822385787964
# array with  7000000  entries ->  4,783858299255371
# array with  8000000  entries ->  5,38990330696106
# array with  9000000  entries ->  5,503363847732544
# array with  10000000  entries ->  5,874427318572998

#La courbe la plus représentative de ma situation est la courbe 0(n), car
#le temps de génération du tableau est proportionnel au nombre d'entrées dans
#notre tableau

#génère le tableau et mesure le temps nécéssaire à sa génération
def generate_array_and_get_execution_time(entries_number: int) -> int:
    start: float = time.time()
    array = [random.randint(0, 100) for i in range(entries_number)]
    end: float = time.time()
    #print("Temps écoulé :", end - start)
    return end - start


for i in range(1, 11):
    print("array with ", i * 1_000_000, " entries -> ", generate_array_and_get_execution_time(i * 1_000_000), " seconds")
