#reading just the first line
fo = open(r"MyFile.txt", "r")
print("Reading using readline:",fo.readline())
print('-'*50)
#reading 10 bytes
fo.seek(0)
print("Reading 10 bytes using read:",fo.read(10))
print('-'*50)
#reading 10 bytes using readline - if n exceeds the single line bytes, still prints only first line
fo.seek(0)
print("Reading 10 bytes using readline:",fo.readline(10))
fo.close()