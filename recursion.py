def factorial(number: int)-> int:
    result: int = 1
    for i in range(2, number+1):
        result = result*i
    return result
    
print(factorial(5))