array = ['a','b','c','d','e','f','g','h','i','j','k']
c = 1
l = len(array)
z = 0
while (array.count('-')<l-1):
    if z == l:
        z = 0
    if array[z] != '-':
        if c % 4 == 0 or c %10 == 4:
            c += 1
            array[z] = '-'
        if array[z] != '-':
            c += 1
    z += 1
for x in array:
    if x != '-':
        print(f"'{x}'")
