numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    k = 0
    for j in range(2, i // 2 + 1):
       if i % j == 0:
           k = k + 1

    if k <= 0:
        print('число простое', i)
    else:
        print('число не простое', i)


















