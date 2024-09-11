def pares_ate(n:int):
    
    for number in range(2, n + 1):
        
        if number % 2 == 0:
            yield number