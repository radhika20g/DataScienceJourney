# Python program to illustrate
# Append vs write mode
file1 = open(r"MyFile.txt","w")
L = ["This is adding \n","Through \n","List \n", "using write as\n", "access mode.\n"] 
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt","a")#append mode
file1.write("Writing through append\n")
file1.close()

file1 = open(r"Myfile.txt","r")
print("Output of Readlines after appending") 
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after writing") 
print(file1.readlines())
print()
file1.close()