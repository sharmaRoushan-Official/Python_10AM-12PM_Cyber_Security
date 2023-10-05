filename='Chandra_Shekhar_azad.txt'
file=open(filename,'r')
content=file.read()
print(content)

# print the file path
print(file.name)

# print the mode of file
print(file.mode)

print(type(content))

# close the file
file.close()

# Verification of the file 
file.closed