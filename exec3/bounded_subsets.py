def bounded_subsets(data: list, target: int):
    """
    >>> for s in bounded_subsets(range(1, 10), 10):print(s)
    [1]
    [2]
    [1, 2]
    [3]
    [1, 3]
    [1, 2, 3]
    [2, 3]
    [4]
    [1, 4]
    [3, 4]
    [2, 4]
    [1, 3, 4]
    [1, 2, 3, 4]
    [2, 3, 4]
    [5]
    [1, 5]
    [1, 2, 5]
    [2, 5]
    [4, 5]
    [1, 4, 5]
    [6]
    [1, 6]
    [1, 2, 6]
    [2, 6]
    [1, 3, 6]
    [7]
    [1, 7]
    [1, 2, 7]
    [2, 7]
    [8]
    [1, 8]
    [2, 8]
    [9]
    [1, 9]
    >>> for s in bounded_subsets(range(50, 150), 103): print(s)
    [50]
    [51]
    [50, 51]
    [52]
    [50, 52]
    [51, 52]
    [53]
    [50, 53]
    [54]
    [55]
    [56]
    [57]
    [58]
    [59]
    [60]
    [61]
    [62]
    [63]
    [64]
    [65]
    [66]
    [67]
    [68]
    [69]
    [70]
    [71]
    [72]
    [73]
    [74]
    [75]
    [76]
    [77]
    [78]
    [79]
    [80]
    [81]
    [82]
    [83]
    [84]
    [85]
    [86]
    [87]
    [88]
    [89]
    [90]
    [91]
    [92]
    [93]
    [94]
    [95]
    [96]
    [97]
    [98]
    [99]
    [100]
    [101]
    [102]
    [103]
    >>> for s in bounded_subsets([4, 5 ,6], 0):print(s)

    """
#the solution based on https://stackoverflow.com/questions/69999857/getting-all-subsets-from-subset-sum-problem-on-python-using-dynamic-programming
# initialize final result which is a list of all subsets summing up to target
    subsets = []
    # records the difference between the target value and a group of numbers
    differences = {}
    prospects = []
    for number in data:
        if number <= target:
            subsets.append([number])  #any number in the list that is smaller than the target is a subgroup in itself
        # iterate through every record in differences
        for diff in differences:
            # the number complements a record in differences, i.e. a desired subset is found
            if number - diff <= 0:
                new_subset = [number] + differences[diff]
                new_subset.sort() #sort to keep the order of the original list
                if new_subset not in subsets:
                    subsets.append(new_subset)
                if number - diff < 0:  # the number fell short to reach the target; add to prospect instead
                    prospects.append((number, diff))

        # update the differences record
        for prospect in prospects:
            new_diff = target - sum(differences[prospect[1]]) - prospect[0]  #Setting a new distance - the distance between the target and the previous subgroup plus the current number in the list
            differences[new_diff] = differences[prospect[1]] + [prospect[0]] #Inserting the new subgroup plus the new number to the key of the new distance
        differences[target - number] = [number]   #Entering the current number as a value for the key of its distance from the target

    return subsets


def bounded_subsets2(data: list, target: int):  #Exactly the same function, except that all subsets must be exactly equal to the target
    subsets = []
    differences = {}

    for number in data:
        prospects = []

        for diff in differences:

            if number - diff == 0:
                new_subset = [number] + differences[diff]
                new_subset.sort()
                if new_subset not in subsets:
                    subsets.append(new_subset)

            elif number - diff < 0:
                prospects.append((number, diff))

        for prospect in prospects:
            new_diff = target - sum(differences[prospect[1]]) - prospect[0]
            differences[new_diff] = differences[prospect[1]] + [prospect[0]]
        differences[target - number] = [number]
    if not subsets:
        return False
    return subsets


def bounded_subsets_sort(data: list, target: int):
    """"
    >>> for s in bounded_subsets_sort([3, 7, 6, 4], 14): print(s)
    [[3, 4]]
    [[3, 6]]
    [[3, 7], [4, 6]]
    [[4, 7]]
    [[6, 7], [3, 4, 6]]
    [[3, 4, 7]]
    >>> for s in bounded_subsets_sort([1,7,2,2,8],8): print(s)
    [[1, 2]]
    [[2, 2]]
    [[1, 2, 2]]
    [[1, 7]]
    """
    all_sub = []
    var = 1
    while var <= target:
        curr = bounded_subsets2(data, var)  #start from 1 to target to be sorted
        if curr:
            all_sub.append(curr)#add to list all subsets withsum less than target (or equal)
        var = var + 1
    return all_sub

# for s in bounded_subsets_sort([3,7,6,4], 14):
#     print(s)
# print(get_subsets(range(50, 150), 103))
(bounded_subsets([3,7,6,4], 14))

# for s in bounded_subsets([4, 5 ,6], 0):print(s)
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)