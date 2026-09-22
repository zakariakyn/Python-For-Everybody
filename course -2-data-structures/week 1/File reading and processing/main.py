fname = input("print the name of file")
try :
    file = open(fname,"r")
except :
    print("file cannot open")
    quit()

for line in file :
    line = line.strip().upper()
    print(line)