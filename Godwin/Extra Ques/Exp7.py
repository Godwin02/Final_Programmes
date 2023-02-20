items = ['Table ', 'Chair ', 'Mirror ', 'Curtain ', 'Almirah ']
file = open('items.txt','w')
file.writelines(items)
file.close()