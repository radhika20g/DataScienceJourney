#reading multiples lines from the file and returning them in a list containing various lines as strings
fo = open(r"MyFile.txt", "r")
print(fo.readlines())
fo.close()