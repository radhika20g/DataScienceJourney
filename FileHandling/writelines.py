#writing multiple lines simulateneously
fo = open("MyFile.txt", "w+")
lst = ["Hello\n", "My Name is:\n", "Radhika", "Gupta"]
fo.writelines(lst)
fo.seek(0)
print(fo.read())
fo.close()