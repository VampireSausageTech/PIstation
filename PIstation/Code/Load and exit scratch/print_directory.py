import os
directory = raw_input("Type in a directory here.\n")
result = os.listdir(directory)
print("\n")
listlen = len(result)
num = 0
while num < listlen:
    print result[num]
    num = num + 1
