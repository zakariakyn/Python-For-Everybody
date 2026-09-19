
tab = []
cond = False

largest = None
smallest = None

while True :
    
    x = input("Enter a number (or 'done'): ")
    
    if x == 'done':
        break
    else :
        try :
            num = int(x)
            tab.append(num)
        except :
            print("Invalid input.")

largest = max(tab)
smallset = min(tab)

print("Maximum is", largest)
print("Minimum is", smallset)

