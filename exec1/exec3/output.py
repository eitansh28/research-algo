from abc import ABC, abstractmethod
from typing import Any, List, Callable



#outputTypes
class return_result(ABC):   #A class of some result type
    def __init__(self):
        self.li = []

    def result(self, l):
        pass

    def __str__(self):
        return self.li


class return_sort_list(return_result):  #A class that returns the sorted list
    def __init__(self):
        super().__init__()

    def result(self, l):
        return l

    def __str__(self):
        return super.__str__()


class return_dist_average(return_result):  #A class that returns the average distance between the members of the list after sorting
    def __init__(self):
        super().__init__()


    def result(self, l):
        dist_sums = []
        for i in range(len(l) - 1):
            dist_sums.append(l[i+1] - l[i])
        return sum(dist_sums)/len(dist_sums)



