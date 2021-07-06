from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print('入口函数的名称==>', func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y


if __name__=='__main__':
    res = add(3, 4)
    print(res)