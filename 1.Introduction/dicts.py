my_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

for k, v in my_dict.items():
    print('dict[{key}]={value}'.format(key = k, value = v))

if 'a' in my_dict:
    print('a exists in dict')

def my_func(a, b, c, d = 10, e = 11):
    return a + b + c + d + e

print(my_func(1, 2, 3))
print(my_func(1, 2, 3, 4))
print(my_func(1, 2, 3, e = 4))