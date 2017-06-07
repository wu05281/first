

def log(f):
    def fn(x):
        print('call ' + f.__name__)
        return f(x)
    return fn


@log
def fx(y):
    return y*y

print(fx(5))