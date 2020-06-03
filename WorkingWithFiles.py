i = 1
for line in open('TestFile.txt','r'):
    if i%2 == 0:
        print (line)
    i += 1
