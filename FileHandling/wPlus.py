#writing in a file and reading it in the next file
fo = open(r"MyFile.txt","w+")
fo.write("16/03/2024")
fo.seek(0) # Move the file pointer back to the beginning
print(fo.read())
fo.close()
