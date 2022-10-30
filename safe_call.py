def print_hi(name: str):
    print(f'Hi, {name}')


def plus(x: int, y: int):
    print(x + y)
    return


def trying(a: str, b: tuple):
    print(a + "hgh")
    return


def safe_call(func, **kwargs):
    """
    >>>safe_call(plus, x=9, y=32)
    41
    """
    func_types = func.__annotations__  # insert all the annotation into list
    for j in func_types:  # run through the entire list to see that the types of the variables match the input we received
        if func_types[j] != type(kwargs[j]):
            raise Exception("The arguments not in a right types")  # if not - throw exception
    func(*kwargs.values())  # if yes - activate the function


safe_call(plus, x=9, y=32)
safe_call(trying, a="nb", b=(7, 5, 1))
safe_call(print_hi, name="mmm")

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
#     doctest.testmod(verbose=True)


# for x in kwargs.keys():
#     if x == j and func_types[j] != type(kwargs[x]):
#         raise Exception("The arguments not in a right types")
