
path = "results.txt"

with open("netflix.txt", "r", encoding ="utf-8" , errors = "ignore") as file :
    with open(path , "w",encoding ="utf-8" ) as result :
        
        for line in file :
            line.strip()
            if not line :
                continue
            line = line.split("|")
            if line[0] :
                line[0] = line[0].split(":")
                result.write(f"email : {line[0][0]} , password : {line[0][1]} , {line[3]}\n")
    print ("Done !")