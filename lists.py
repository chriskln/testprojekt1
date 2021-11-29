l1 = [1213, 12344, 134, 345465, 3464, 2355]

print(l1[0])
print(l1[5]) # last element also called by "-1"
print(l1[-1])

l2 = l1[1:5]
print(l2)
l2.append(238439)
print(l2)
l2.insert(2, 2345)
l2[1] = 32453
print(l2)

l3 = l2
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)

print("________")

l4 = [35456, 234, 3254, 235.343, "Hello Python 3", 23432]
print(l4)

# extract word "Python" form l4

print(l4[4][6:12]) # option 1
print(l4[4].split(" ")[1]) # option 2

print("-----------")
# sum all number values of l4

l5 = l4[0:4] + l4[5:] # option 1
print(sum(l5))

my_sum = 0 # option 2
for el in l4:
    if type(el) == int or type(el) == float:
        my_sum += el
print(my_sum)

l6 = [el for el in l4 if type(el) == int or type(el) == float] # option 3
sum_l6 = sum([el for el in l4 if type(el) == int or type(el) == float])
print(l6)
print(sum_l6)

print("________")

l1 = [1213, 12344, 134, 345465, 3464, 2355]
l1i = [el*2 for el in l1]
print(l1i)

l1ii = []
for el in l1:
    l1ii.append(el*2)
print(l1ii)

