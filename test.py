def try_repeat(func):
    def wrapper(*args, **kwargs):
        count = 10

        while count:
            try:
                print('ok')
                return func(*args, **kwargs)
            except Exception as e:
                print('Error:', e)
                count -= 1

    return wrapper

@try_repeat
def exception_func():
    import random
    if random.randint(0, 1):
        raise Exception('!!!')


exception_func()