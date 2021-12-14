import os

print(__file__) # unix way of representing a file path

my_file_path = __file__

my_parent_dir = os.path.dirname(my_file_path)
my_file_name = os.path.basename(my_file_path)
print(my_parent_dir)
print(my_file_name)

# in_path = os.path.join(os.getcwd(), 'data', '.keep') # join directory with a file

in_path = os.path.join(os.getcwd(), 'data', '.keep')

print(in_path)

print(os.listdir(my_parent_dir))# printing list of all files I have
print(os.listdir('C:\\Users')) # printing list of users

my_dir = 'C:\\Users\\klein'
for f in os.listdir(my_dir):
    print(f)
