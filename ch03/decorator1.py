def foo(f):
    print("foo output")
    return f

def bar(f):
    print("bar output")
    return f

@foo
@bar
def incr():
    print("incr output")

incr()
