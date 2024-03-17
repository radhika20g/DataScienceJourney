#reading the whole file 
file = open(r"MyFile.txt", "r")
txt = file.read()
print(txt)
#replacing the double new line with a single space
txt = txt.replace("\n\n", " ")
print(txt)
file.close()