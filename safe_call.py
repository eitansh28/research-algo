import doctest
def print_hi(name: str):
    print(f'Hi, my name is {name}')


def plus(x: int, y: int):
    print(x + y)
    return


def trying(a: str, b: tuple):
    print(a + "end")
    return


def minus(v, w):
    return v-w

def safe_call(func, **kwargs):  # A function that checks the types of arguments in a function's input match arguments that the function should receive
    """
    example
    >>> safe_call(plus, x=9, y=32)
    41
    >>> safe_call(trying, a="nb", b=(7, 5, 1))
    nbend
    >>> safe_call(print_hi, name=5)
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm 2021.2.2\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest safe_call.safe_call[2]>", line 1, in <module>
        safe_call(print_hi, name=5)
      File "C:/Users/eitan/PycharmProjects/pythonProject18/safe_call.py", line 32, in safe_call
        raise Exception("The arguments not in a right types")  # if not - throw exception
    Exception: The arguments not in a right types
    """

    func_types = func.__annotations__  # insert all the annotation into list
    for j in func_types:  # run through the entire list to see that the types of the variables match the input we received
        if func_types[j] != type(kwargs[j]):
            raise Exception("The arguments not in a right types")  # if not - throw exception
    func(*kwargs.values())  # if yes - activate the function


safe_call(plus, x=2, y=67)
safe_call(trying, a="This is the ", b=(7, 5, 1))
safe_call(print_hi, name="eitan")


if __name__ == "__main__":
    doctest.testmod(verbose=True)



