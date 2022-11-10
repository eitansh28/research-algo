class mylist(list):

    def __init__(self, deep_list):
        super().__init__(deep_list)

    def __getitem__(self, index_list: list):
        return rec(index_list[1:], super().__getitem__(index_list[0]))


def rec(List_of_index: list, orig_deep_level: list):
    if len(List_of_index) == 1:
        return orig_deep_level[List_of_index[0]]

    return rec(List_of_index[1:], orig_deep_level[List_of_index[0]])


m = mylist([[4, 6, 2], [2, 7, 6], [9, 8, 1]])
print(m[0, 2] + m[1, 1])

mylist = mylist([
[[1,2,3,33],[4,5,6,66]],
[[7,8,9,99],[10,11,12,122]],
[[13,14,15,155],[16,17,18,188]],
]
)
print(mylist[0, 1,3])