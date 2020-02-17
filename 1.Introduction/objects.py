class MyClass():
    def __init__(self, content):
        self.content = content
    def print_me(self):
        print('content is : ', self.content)

o = MyClass('some content')
o.print_me()

def my_generator():
    for i in range(0, 10):
        yield i

for item in my_generator():
    print(item)