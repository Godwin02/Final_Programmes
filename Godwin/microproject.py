file=open("mytext","r")
count=0
for i in file:
    words=i.split(" ")
    count += len(words)
print("The number of words in the file is:",count)