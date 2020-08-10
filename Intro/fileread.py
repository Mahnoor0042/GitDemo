file = open('text.txt')
#print(file.read(12))
#line = file.readline()
#while line!="":
    #print(line)
    #line=file.readline()

print("****************************")
for line in file.readlines():
    print(line)


file.close()
