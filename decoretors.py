

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

x= is_called()
print(x())

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")