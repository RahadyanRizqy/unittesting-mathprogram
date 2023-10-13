var = {
            '1' : 'addition',
            '2' : 'substract'
        }


def addition():
    print('This is addition')

x = globals()[var['1']]
x()

print('1' in var.keys())

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))