
def fib():



    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2, m):
        c = a + b
        a = b
        b = c
        print(c)




m = ''

while m != 'exit':
    m = input('Enter a number for Fibonacci: ')
    m = int(m)
    fib()
    print('Type exit to exit')
