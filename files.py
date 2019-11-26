import os

dir = "/Users/honza/Documents/Moje dokumenty/Xcode/Fast Mike"
files = os.listdir(dir)
print(files)

for file in files:
    # print(file)
    if os.path.isfile(os.path.join(dir, file)):
        print(file)

print()
print(os.getcwd())  # current working directory

in_file = '../Python Programming/t.txt'

with open(in_file, 'r') as in_f:
    for line in in_f.readlines():
        print(line)


#os.path.isdir
#os.path.isfile