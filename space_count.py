import os

my_dir = 'C:\\Temp\\t'

#def sum_space(folder):
#    sum = 0
#    for f in os.listdir(folder): # f will return names of files
#        #type = "d" if os.path.isdir(os.path.join(my_dir, f)) else "-"
#        if os.path.isfile(os.path.join(my_dir, f)):
#            size = os.path.getsize(os.path.join(my_dir, f))
#            sum = sum + size
#        return sum

# print("Space occupied by {}: {}".format(my_dir, sum_space(my_dir)))

# like this, it does not take subfolders into account

# to do: include the size of files in subfolders and their subfolders ...

def sum_space(folder):
    sum = 0
    for f in os.listdir(folder): # f will return names of files
        #type = "d" if os.path.isdir(os.path.join(my_dir, f)) else "-"
        if os.path.isdir(os.path.join(folder, f)):
            sum = sum + sum_space(os.path.join(folder, f))
        else:
            size = os.path.getsize(os.path.join(folder, f))
            sum = sum + size
        #else:
        #    sum += sum_space(os.path.join(folder, f))
        return sum

print("Space occupied by {}: {}".format(my_dir, sum_space(my_dir)))