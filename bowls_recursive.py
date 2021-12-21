
def bowls_recursive(n):
    if n == 1:
        return 1
    else:
        return bowls_recursive(n-1) + n

print('Enter the rows : ') # Requesting user input
limit = input()
bowl = 0
print('Bowls: {}'.format(bowls_recursive(int(limit))))

# maximum recursion close to 1000 when using recursion
# in loops there is no limitation
# sequence is even faster because it just runs a formula, also without limitation

