def sum(a,b):
    return a+b
print(sum(1,2))
print(sum(5,7))
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    d=2
    while d*d<=num:
        if num%d==0:
            return False
        d+=1
        return True
print(is_prime(2))
print(is_prime(5))
print(is_prime(7))
print(is_prime(8))

def greeting(name):
    return f'Hello {name}, how are you?'
print(greeting('Jim'))

