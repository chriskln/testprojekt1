import os
import glob

my_dir = 'C:\\Users\\klein\\Downloads'
csv_files = glob.glob(my_dir + "/**/*.csv", recursive = True)
print(csv_files)

