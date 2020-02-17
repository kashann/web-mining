s = 'hello world'
print('LENGTH:')
print(len(s))

myList = [1, 2 , 3, 4, 5]
myList.append(6)
myList.extend([7, 8])

print(myList)

print(myList[3])
print(myList[1:4])
print(myList[1:])
print(myList[:4])
print(myList[:])
print(myList[:-1])

for item in myList:
    print(item)

t = (1, 'cat')
print(t)
print(t[1])

for index, item in enumerate(myList):
    print("a[{index}]={item}".format(index = index, item = item))

print("DOUBLES")
doubles = list(map(lambda x: x * 2, myList))
print(doubles)

double_doubles = [x * 2 for x in doubles if x > 0]
print("DOUBLE DOUBLES")
print(double_doubles)

print("range")
for i in range(0, 10):
    print(i)