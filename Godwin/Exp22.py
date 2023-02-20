n = int(input("Enter the size of strings= "))
print("Enter the strings: ")
list = []
for i in range(0, n):
    ele = (input())
    list.append(ele)
print(list)
count = 0
for i in list:
    for j in i:
        if (j == "a"):
            count = count + 1
print(count)
