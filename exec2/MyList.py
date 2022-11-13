class mylist(list):
    """"
    >>> mylist = mylist([
    ...   [[1,2,3,33],[4,5,6,66]],
    ... [[7,8,9,99],[10,11,12,122]],
    ...    [[13,14,15,155],[16,17,18,188]],])
    >>> print(mylist[0, 1,3])
    66
    """
    def __init__(self, deep_list):  #Initialize an object by the parent's constructor
        super().__init__(deep_list)

    def __getitem__(self, index_list: list):   #Overriding the [] operator by the get_item function
        return rec(index_list[1:], super().__getitem__(index_list[0]))  #Enter the recursion with the first layer


def rec(List_of_index: list, orig_deep_level: list):  #A recursive function that goes deep into the list layers
    if len(List_of_index) == 1:   #If we have reached the last index then we will return the value found in it
        return orig_deep_level[List_of_index[0]]

    return rec(List_of_index[1:], orig_deep_level[List_of_index[0]])  #Calling the function with the rest of the indexes and with the next layer



mylist = mylist([
[[1,2,3,33],[4,5,6,66]],
[[7,8,9,99],[10,11,12,122]],
[[13,14,15,155],[16,17,18,188]],
]
)
# print(mylist[0, 1,3])
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)