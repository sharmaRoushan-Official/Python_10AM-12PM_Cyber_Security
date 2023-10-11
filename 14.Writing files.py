def write(cow,n):
    with open(cow,'w') as f:
        for i in range(n):
            s=input()
            f.write(s)
            f.write('\n')

cow=input('Enter text file name.')
cow=cow+'.txt'
n=int(input('Enter number of lines:'))
write(cow,n)