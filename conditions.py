p = True
q = False

if p and q:
    print('p and q')
else:
    print('not p and q')

if p or q:
    print('p or q')
else:
    print('not p or q')

if not (p and q):
    print('NAND p and q')
else:
    print('p and q')

# XOR (exclusive or)
if p ^ q:
    print('p XOR q')
else:
    print('not p XOR q')

if p:
    v= 10
else:
    v = 20
print(v)

# same but written differently:
v = 10 if p else 20
print(v)
