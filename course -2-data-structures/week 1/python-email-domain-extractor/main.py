message = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

swith = message.find("@")

print(swith+1)

word = message[ swith + 1: message.find(" ",swith)]

print(word)