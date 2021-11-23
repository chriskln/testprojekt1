

start = 0
N = 100

print('the prime numbers from', start, 'to', N, 'are:')

for x in range(start, N + 1):
    if x > 1:
        for y in range(2, x):
            if (x % y) == 0:
                break
        else:
            print(x)
