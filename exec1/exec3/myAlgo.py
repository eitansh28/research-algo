from typing import Callable, Any
import output as out
from MyStruct import *
def mySort(algorithm: Callable, items: MyStruct, res: out.return_result, **kwargs):
    """
    >>> mySort(algorithm=insertionSort, items=MyList([7, 2, 3, 6, 5, 1, 4]), res = out.return_sort_list )
    [1, 2, 3, 4, 5, 6, 7]
    >>> mySort(algorithm=bubbleSort, items=MyList([7, 2, 3, 6, 5, 1, 4]), res = out.return_sort_list )
    [1, 2, 3, 4, 5, 6, 7]
    >>> mySort(algorithm=insertionSort, items=MyList([7, 2, 3, 6, 5, 1, 4]), res = out.return_dist_average)
    1.0
    >>> mySort(algorithm=bubbleSort, items=MyList([4, 7, 1, 8]), res = out.return_dist_average)
    2.3333333333333335
    >>> mySort(algorithm=insertionSort, items=MyDict({"a":7, "b": 2, "c": 43, "d":86, "e":95, "f":11, "g":4}), res = out.return_sort_list)
    [2, 4, 7, 11, 43, 86, 95]
    >>> mySort(algorithm=bubbleSort, items=MyDict({"a":1, "b": 2, "c": 143, "d":86, "e":15, "f":11, "g":4}), res = out.return_sort_list)
    [1, 2, 4, 11, 15, 86, 143]
    >>> mySort(algorithm=insertionSort, items=MyDict({"a":7, "b": 2, "c": 43, "d":86, "e":95, "f":11, "g":4}), res = out.return_dist_average)
    15.5
    >>> mySort(algorithm=bubbleSort, items=MyDict({"a":1, "b": 2, "c": 143, "d":86, "e":15, "f":11, "g":4}), res = out.return_dist_average)
    23.666666666666668
    """
    item_names = items
    func_res = algorithm(item_names, res)  #Running the selected algorithm on the specific input to get a result of the selected type
    return func_res


def insertionSort(ms: MyStruct, res: out.return_result):  #insertion sort function taken from geeksforgeeks (with appropriate syntax changes for 'mystruct')
    # Traverse through 1 to len(arr)
    for i in range(1, ms.length()):
        key = ms.get_item(i)
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < ms.get_item(j):
            ms.swap(j+1, j)
            j -= 1
        ms.set_item(j + 1, key)
    return res.result(res, ms.struct)


def bubbleSort(ms: MyStruct, res: out.return_result):   #bubble sort function taken from geeksforgeeks (with appropriate syntax changes for 'mystruct')
    n = ms.length()
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if ms.get_item(j) > ms.get_item(j+1):
                swapped = True
                temp = ms.get_item(j)
                ms.swap(j,j+1)
                ms.set_item(j+1, temp)

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            break
    return res.result(res, ms.struct)



m= MyList([4, 7, 1, 8])
p = MyList([88, 92, 54, 7324, 82, 77 ,32, 13,2412])
n = MyDict({"0": 45, "1": 72, "2": 13, "3": 86})
w = MyDict({"a":7, "b": 2, "c": 43, "d":86, "e":95, "f":11, "g":4})
# print(mySort(bubbleSort, m, out.return_dist_average))
# print(mySort(insertionSort, n, out.return_sort_list))
# print(mySort(insertionSort, w, out.return_dist_average))
# print(insertionSort({"1": 4, "2": 7, "3": 3, "4": 6}))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)