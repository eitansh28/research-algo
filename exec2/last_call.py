def last_call(func):
    rem_list = {}

    def wrap(*args, **kwargs):
        var = 0
        if kwargs:
            var = kwargs
        elif args:
            var = args
        if func not in rem_list.keys():
            rem_list.setdefault(func, []).append(var)
        elif var not in rem_list.get(func, []):
            rem_list[func].append(var)
        else:
            val = func(*args, **kwargs)
            raise Exception(f'halas!! the answer is {val}')
        return func(*args, **kwargs)

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
        x = x + str(i)+""
    return x

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
