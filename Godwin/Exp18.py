d={3:9,0:1,2:4,5:25,4:16}
print(d)
sorted_d=sorted(d.items())
print("Items sorted in ascending order:", sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print("items in descending order:",sorted_d)