def print_dict_sorted(deep_dst):
    for key, val in sorted(deep_dst.items()):
        try:
            print("'{}': {}".format(key, sorted(val, key=lambda a: (str(a).split(',')))))
            # p_sort(val)
        except:
            print("'{}' : {}".format(key, val))


def print_tuple_set_list_sorted(deep_dst):
    for val in deep_dst:
        p_sort(val)


def p_sort(s):
    if type(s) == dict:
        print_dict_sorted(s)
    if type(s) == tuple or type(s) == set or type(s) == list:
        print_tuple_set_list_sorted(s)
    if type(s) == int or type(s) == str:
        print(s)




x = {"a": 6, "c": 7, "b": [3, 6, [4, 9], 2, 7, 0]}
y = [5, {"a": 9, "f": 7, "b": 4}, (9, 8)]
z = ("v", [4, 2], 1, {"w": 7, "a": 9, "b": 5})
p_sort(x)
p_sort(y)
p_sort(z)
# t = (1, 2)
# print(type(t))
# print_tuple_set_list_sorted(y)

