#reading the whole file 
file = open(r"MyFile.txt", "r")
txt = file.read()
print(txt)

file.close()