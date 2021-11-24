file_path = 'text.csv'

# 'r' is the mode to open the file (r = open for reading)
# 'b' = open files in binary mode

with open(file_path, 'r') as my_file:
    lines = my_file.readlines()
    i = 1
    for line in lines:
        print(line)
        line = float(line)
        print(type(line))
        print('{}: {}'.format(i, line), end='')
        i+=1

#my_file = open(file_path, 'r')
#lines = my_file.readline()
#i = 1
#for line in lines:
#        print('{}: {}'.format(i, line), end='')
#        i+=1
#my_file.close()


