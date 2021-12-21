n = 10

#using loop
def bowls_loop(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum


#using sequence
def bowls_sequence(n):
    sum = n * (n+1)/2
    return int(sum)


print('Enter the rows : ') # Requesting user input
limit = input()
bowl = 0
print('Bowls: {}'.format(bowls_loop(int(limit))))
