from time import time
start=time()

#Python program to create an acronyms
word="Super Sport Car Races"
text=word.split()
a=" "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
exec_time = end - start
print("Exec Time : ", exec_time)