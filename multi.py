def foo( a, b , c= 4, d= 5):
    print(a*b+c+d)


foo(2,3)
# if default values are given we can call a function with less parameters

def foo(a, v, *args , **kwargs):
    