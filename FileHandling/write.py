#writing a word in data.txt file
fo = open(r"MyFile.txt","w")
fo.write("Hello\n Radhika")
fo.close()

#reading after making changes as previously the access mode we have used is just w
fo = open(r"MyFile.txt", "r")
print(fo.read())
fo.close()

