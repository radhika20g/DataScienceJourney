#reading the whole file
fo = open(r"MyFile.txt", "r")
print(fo.read())
print("-"*50)
#reading 5 bytes only
fo.seek(0)
print(fo.read(5))
fo.close()