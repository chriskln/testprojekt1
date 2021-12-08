l2d = [[5, 5, 7],
       [9, 6, 4],
       [9, 14, 4],
       [1, 4, 5]]
print(l2d[1][2]) # show third element in second array

# to do
# 1. sum the rows of L2D: [17, 19. 27, 10]
# 2. sum the columns of L2D: [24, 29, 20]
# 3. sum all elements of L2D

#1 manual solution
rows = len(l2d);
cols = len(l2d[0]);
sum_rows = []
for i in range(rows):
    sumRow = 0;
    for j in range(cols):
        sumRow = sumRow + l2d[i][j];
    sum_rows.append(sumRow)
    print("sum of " + str(i + 1) + " row: " + str(sumRow));

print(sum_rows)

#1 simpler solution
sumRow = [sum(i) for i in l2d]
print(sumRow)

#2
colsum = []
for i in range(len(l2d[0])):
    sum_cols = 0
    for j in range(len(l2d)):
        sum_cols = sum_cols + l2d[j][i]
    print("Sum of column {} ".format(i+1), (sum_cols))
    colsum.append(sum_cols)
print(colsum)

#3
sum_all = 0
for el in colsum:
    sum_all += el
print(sum_all)

print(sum(sum_rows))
print(sum(colsum))
#for i in range(len(l2d))

# doesnt work

#import numpy as np
#s_rows = np.sum(l2d, axis=1)
#print(s_rows)
#s_cols = np.sum(l2d, axis=0)
#print(s_cols)