file = open("file.txt","r")

###  print all the lines that start with "d" in the file
# for line  in file :
#     line = line.rstrip()
#     if not line.startswith("d"):
#         continue
#     print(line)

### print all the lines that start with "d" in the file and print the first word before the comma
# for line in file :
#     line = line.rstrip()
#     if not line.startswith("d"):
#         continue
#     x = line.find(",")
#     print(line[:x])


###  count the number of lines that contain the word "yahoo" in the file
num = 0
for line in file :
    line = line.rstrip()
    if not  "yahoo" in line :
        continue 
    num += 1        

print("the number of yahoo in file is : ", num)


