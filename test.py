import time


# 定义装饰器
def time_calc(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        f = func(*args, **kargs)
        exec_time = time.time() - start_time
        return f
    return wrapper

# 使用装饰器


@time_calc
def add(a, b):
    return a + b


@time_calc
def sub(a, b):
    return a - b


def main():
    print(sub(23, 34))
    print(add(34, 56))


if __name__ == '__main__':
    main()
