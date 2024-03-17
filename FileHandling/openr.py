#opening a file present in different folder
#use r
fo = open(r"MyFile.txt", "r")
print(fo.read())
fo.close()  