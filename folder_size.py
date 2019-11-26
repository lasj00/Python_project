import os


def folder_size(folder_dir):
    size = 0
    if os.path.isdir(folder_dir):
        for file in os.listdir(folder_dir):
            size += folder_size(os.path.join(folder_dir, file))
    else:
        size += os.path.getsize(folder_dir)
    return size



print(folder_size("/Users/honza/Desktop/Ahoj/"))


