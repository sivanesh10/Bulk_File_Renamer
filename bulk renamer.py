import os
def rename():
    i = 0
    path = str(input("enter your path"))
    path2 = str(input("enter your destination"))
    name = str(input("enter name to rename"))
    format = str(input("enter file format"))
    for l in os.listdir(path):
        source = path +"/" + l
        destination = name + str(i) + format
        destination = path2 + destination
        os.rename(source,destination)
        i = i + 1
if __name__ == "__main__":
    rename()