def is_primo(n):
    for i in range(2, ((n // 2) + 1)):
        if n % i == 0:
            return False
    return True
    
for n in range(2,101):
    if is_primo(n):
        print(n)
    