import doctest
def last_call(func):
    """"
    >>> plus_2(num=9)
    11
    >>> plus_2(num=7)
    9
    >>> plus_2(num=22)
    24
    >>> plus_2(num=0)
    2
    >>> plus_2(num=9)
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm 2021.2.2\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest last_call.last_call[4]>", line 1, in <module>
        plus_2(num=9)
      File "C:/Users/eitan/PycharmProjects/pythonProject18/exec2/last_call.py", line 29, in wrap
        raise Exception(f'halas!! the answer is {val}')
    Exception: halas!! the answer is 11

    >>> connect_dict_value({"a": 10, "b": 20, "c": 30})
    '102030'
    >>> connect_dict_value({"a": 12, "b": 21, "c": 30})
    '122130'
    >>> connect_dict_value({"a": 13, "b": 20, "c": 30})
    '132030'
    >>> connect_dict_value({"a": 12, "b": 21, "c": 30})
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm 2021.2.2\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest last_call.last_call[8]>", line 1, in <module>
        connect_dict_value({"a": 12, "b": 21, "c": 30})
      File "C:/Users/eitan/PycharmProjects/pythonProject18/exec2/last_call.py", line 45, in wrap
        raise Exception(f'halas!! the answer is {val}')
    Exception: halas!! the answer is 122130
    >>> lists([4, 8, 7, 2])
    448
    >>> lists([4, 8, 6, 2])
    384
    >>> lists([4, 99, 6, 85])
    201960
    >>> lists([4, 8, 6, 2])
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm 2021.2.2\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest last_call.last_call[12]>", line 1, in <module>
        lists([4, 8, 6, 2])
      File "C:/Users/eitan/PycharmProjects/pythonProject18/exec2/last_call.py", line 62, in wrap
        raise Exception(f'halas!! the answer is {val}')
    Exception: halas!! the answer is 384
    >>> lists([4, 8, 7, 2])
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm 2021.2.2\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest last_call.last_call[13]>", line 1, in <module>
        lists([4, 8, 7, 2])
      File "C:/Users/eitan/PycharmProjects/pythonProject18/exec2/last_call.py", line 62, in wrap
        raise Exception(f'halas!! the answer is {val}')
    Exception: halas!! the answer is 448
    """
    rem_list = {}

    def wrap(*args, **kwargs):
        var = 0
        if kwargs:    #Checking if we received args or kwargs
            var = kwargs
        elif args:
            var = args
        if func not in rem_list.keys():  #If this is the first time we use the current function, then we enter it as a key in the dictionary and its value is a list into which we enter the current parameter
            rem_list.setdefault(func, []).append(var)
        elif var not in rem_list.get(func, []):  #If the current function has never operated on the current parameter then we will put it in the values in the dictionary
            rem_list[func].append(var)
        else:       #If it already appears we will throw an exception
            val = func(*args, **kwargs)
            raise Exception(f'halas!! the answer is {val}')
        return func(*args, **kwargs)   #In case we didn't throw an error we will run the current function with the current parameter

    return wrap


@last_call
def plus_2(num: int):
    return num + 2


@last_call
def name(n: str):
    x = f'my name is {n}'
    return x


@last_call
def lists(num_list: list):
    multi = 1
    for i in num_list:
        multi = multi * i
    return multi


@last_call
def convert_to_int(num: float):
    return int(num)


@last_call
def connect_dict_value(d: dict):
    x = ""
    for i in d.values():
        x = x + str(i)
    return x


# Running examples:
# print(connect_dict_value({"a": 10, "b": 20, "c": 30}))
# print(connect_dict_value({"a": 12, "b": 20, "c": 30}))
# print(connect_dict_value({"a": 14, "b": 20, "c": 30}))
# print(connect_dict_value({"a": 13, "b": 20, "c": 30}))

# print(plus_2(num=9))
# print(plus_2(num=7))
# print(plus_2(num=22))
# print(plus_2(num=0))
# print(plus_2(num=9))

# print(name(n="eitan"))
# print(name(n="tamar"))
# print(name(n="ori"))
# print(name(n="tamar"))
# print(name(n="ori"))
# print(name(n="eitan"))

# print(lists([4, 8, 7, 2]))
# print(lists([4, 8, 6, 2]))
# print(lists([4, 99, 6, 85]))
# print(lists([4, 8, 6, 2]))
# print(lists([4, 8, 7, 2]))

# print(convert_to_int(7.8))
# print(convert_to_int(1.1))
# print(convert_to_int(7.6))
# print(convert_to_int(1.1))

if __name__ == "__main__":
    doctest.testmod(verbose=True)