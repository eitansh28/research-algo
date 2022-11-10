class Node:         #class that represent Node
    def __init__(self, x, y):  #init function
        self.x = x
        self.y = y

    def __str__(self):       #print function
        ans = "({}, {})".format(self.x, self.y)
        return ans

    def __eq__(self, other):  #equal function
        return self.x == other.text and self.y == other.y


def between(curr, one, two):    #A function that checks that we have not deviated from the path
    if (curr.text < one.text and curr.text < two.text) or (curr.text > one.text and curr.text > two.text):
        return False
    if (curr.y < one.y and curr.y < two.y) or (curr.y > one.y and curr.y > two.y):
        return False
    return True


def four_nei(curr: Node) -> list[Node]:     #A function that finds the four neighbors
    l, d, r, u = Node(curr.x + 1, curr.y), Node(curr.x, curr.y + 1), Node(curr.x - 1, curr.y), Node(curr.x, curr.y - 1)
    return [l, d, r, u]


def breadth_first_search(start: Node, end: Node, neighbor_func):
    """
    >>> print(*breadth_first_search(Node(-7, 8), Node(-5, -4), four_nei))
    (-7, 8) (-6, 8) (-5, 8) (-5, 7) (-5, 6) (-5, 5) (-5, 4) (-5, 3) (-5, 2) (-5, 1) (-5, 0) (-5, -1) (-5, -2) (-5, -3) (-5, -4)
    >>> print(*breadth_first_search(Node(0, -1), Node(-2, 7), four_nei))
    (0, -1) (0, 0) (0, 1) (0, 2) (0, 3) (0, 4) (0, 5) (0, 6) (0, 7) (-1, 7) (-2, 7)
    >>> print(*breadth_first_search(Node(9, -8), Node(9, -7), four_nei))
    (9, -8) (9, -7)
    """
    queue = []   #Creating a queue that will store and release the nodes in the desired order
    visited = []  #Creating a list that will store all the nodes we have already visited
    path = []   #Creating a list that will save the requested path
    queue.append(start)
    visited.append(start)
    path.append(start)
    while queue:
        curr = queue.pop(0)
        if curr == end:  #We have reached our destination, so we can stop
            return path
        for neighbor in neighbor_func(curr): #Go through the neighbors
            if neighbor not in visited:
                if between(neighbor, start, end):  #add to the path only the nodes that advance us to the destination
                    path.append(neighbor)
                    start = neighbor
                queue.append(neighbor)
                visited.append(neighbor)


s = Node(0, -1)
e = Node(-2, 7)
print(*breadth_first_search(s, e, four_nei))
a = Node(58, 76)
b = Node(62, 10)
print(*breadth_first_search(a, b, four_nei))
x = Node(2, 3)
y = Node(2, 3)
print(*breadth_first_search(x, y, four_nei))
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
