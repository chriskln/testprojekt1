a = 236284523745362457324712647614325265472472452645273
print(type(a))
b = 10
c = a + b
print('a:{}'.format(a))
print('c:{}'.format(c))

d = 6245.98978987987
d = 29837329486348632847326429187194236484628637674347363.0
print(type(d))
print(d)
e = 20
print(type(e))
f = d + e
print('f:{}'.format(f))

max_int = 1.793374289423483459435e308
# limit of int
max_int = 1.8e308
print(max_int)

g = 0.0000000000037286482346
print(g)

bb = 0b101
print(bb)
xx = 0x101
print(xx)
xx = 0xf1
print(xx)

a1 = 3249
b1 = 439
c1 = a1 / b1
print('c1:'+ str(c1))
print('c1:{}'.format(c1))
# man kann beide versionen gleichermaßen verwenden
c2 = int(c1)
print('c2:{}'.format(c2))
c3 = round(c1, 2)
print('c3:{}'.format(c3))

s = '344387594375293794732892.34'
print('______________')
print('s is digit: {}'.format(s.isdigit()))
print('s is numeric: {}'.format(s.isnumeric()))
print('s is alpha: {}'.format(s.isalpha()))
print('s is alnum: {}'.format(s.isalnum()))
print('______________')
print('type of s: {}'.format(type(s)))
f1 = float(s)
print(type(f1))
print(f1)
print('______________')
s1 = '101'
# hexdecimal
h_s1 = int(s1, 2)
h_s1 = int(s1, 16)
print(h_s1)
# result depends on what the basis is (16 or 2, in this case)

# binary
b_s1 = int(s1, 3)
print(b_s1)





