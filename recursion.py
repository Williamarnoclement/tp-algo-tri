# def factorial(number: int)-> int:
#     result: int = 1
#     for i in range(2, number+1):
#         result = result*i
#     return result

#Et en méthode récursive cette fois !
def factorial(val: int)-> int:
    if(val == 0):
        return 1
    else:
        return val * factorial(val -1)
    
print(factorial(5))