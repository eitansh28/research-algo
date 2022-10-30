def print_sorted(deep_dst):
    for key, val in sorted(deep_dst.items()):
        try:
            print(key, sorted(val))
        except:
            print("'{}' : {},".format(key, val))
        # print(type(key))
        # print(type(val))
    print(deep_dst)

x = {"a":6, "c":7, "b": [3,6,2,7,0]}
y = (5, (7, 8), {"a": 9, "f": 7, "b": 4})
print_sorted(y)
# d = [2, 4, 5, 1 ,3]
# r = sorted(d) # sort list
# print(d)
# print(r)
# d1 = {}
# ds = sorted(d1) #sort dict
#
# s = set([3,7,1])
# s1 = sorted(s)  #sort set
# print(s1)
# t = (5,3)
# t1 = sorted(t)  #sort tuple
# print(t1)
#
# def ps(*args):
#     # argstype = args.__annotations__
#     # for x in args:
#     #     if
#     # e = sorted(args)
#     # print(e)
#     for a in args:
#         print(sorted(a))
#         print(type(a))
#         print(type(args))
#     # if type(args) is dict:
#     #     print("zzz")
#     # print(type(args))
# x = {"a":6, "c":7, "b": [3,6,2,0]}
# y = (2, 5, 1)
# print(sorted(y))
# # print(type(x))
# ps(y)
# c = {"s": 5, "w": 4}
# print(sorted(c.values()))