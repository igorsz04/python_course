import numpy as np

a1 = np.zeros(10)
print(a1)

a2 = np.ones(10)
print(a2)

a3 = np.ones(10)*5
print(a3)

a4 = np.arange(10,51)
print(a4)

a5 = np.arange(10,51,2)
print(a5)

print("funkcjee:")
def afunction_2(x, y):
    return int (x*y)

#wywołanie funkcji argumenty są tuple, a key-word-args są dictem
def afunction(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get('printthis'))
    step = afunction_2(args[2],1)
    new_step = kwargs.get('new_step')
    if new_step is not None:
        step = new_step

    return np.arange(args[0], args[1], step)


print(afunction(0,101,3, 'asd',keywordarg = 'anything', printthis = 'hello'))


print("\nnowe funkcje:\n")

def function_2(x, y):
    return int(x * y)


# wywolanie funkcji argumenty sa tuple, a key word argumenty sa dictem
def function(first_argument, *args, **kwargs):
    print('First required argument: {}'.format(first_argument))
    print('Args: {}'.format(args))
    print('Kwargs: {}'.format(kwargs))
    printthis = kwargs.get('printthis')
    if printthis:
        print('Printing value of print_this argument: {}'.format(kwargs.get('printthis')))
    else:
        print('no printthis kwarg provided')

    step = function_2(args[1], 1)
    new_step = kwargs.get('new_step')
    if new_step:
        step = new_step
    return np.arange(first_argument, args[0], step)


print(function(10, 101, 3, 'unused', keywordarg='anything', printthis='Hello', new_step=10))

arguments = [21, 10, 10, 10, 10]
kwarguments = {'new_step': 1, 'next': 'WOW'}
print("\nnowe wywołanie:\n")
print(function(*arguments, **kwarguments))


a6 = np.arange(9).reshape(3,3)
print('\na6:\n',a6)

a7 = np.identity(3)
print('\na7:\n',a7)


a9 = 2 * np.random.rand(5,5) - 1
print('\na9:\n',a9)

a10 = np.linspace(0,1,11)
print('\na10:\n',a10)

