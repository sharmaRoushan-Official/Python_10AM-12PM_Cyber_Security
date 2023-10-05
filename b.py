# readline
fname='Chandra_Shekhar_azad.txt'
with open(fname,'r') as f:
    print('The first line is:',f.readline())
    print('Second line is:',f.readline())
    print('Third line is:',f.readline())