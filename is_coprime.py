'''Function to find co-prime numbers.'''
def is_coprime(a, b):
    """Function to returns output in boolean"""
    is_coprime = True
    for i in range(2, min(a, b)+1):
        if a%i == 0 and b%i == 0:
            is_coprime = False
            break
    return is_coprime
    
