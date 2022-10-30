class Node:         #class that represent Node
    def __init__(self, x, y):  #init function
        self.x = x
        self.y = y

    def __str__(self):       #print function
        ans = "({}, {})".format(self.x, self.y)
        return ans

    def __eq__(self, other):  #equal function
        return self.x == other.x and self.y == other.y


def between(curr, one, two):    #A function that checks that we have not deviated from the path
    if (curr.x < one.x and curr.x < two.x) or (curr.x > one.x and curr.x > two.x):
        return False
    if (curr.y < one.y and curr.y < two.y) or (curr.y > one.y and curr.y > two.y):
        return False
    return True


def four_nei(curr: Node) -> list[Node]:     #A function that finds the four neighbors
    l, d, r, u = Node(curr.x + 1, curr.y), Node(curr.x, curr.y + 1), Node(curr.x - 1, curr.y), Node(curr.x, curr.y - 1)
    return [l, d, r, u]


def breadth_first_search(start: Node, end: Node, neighbor_func):
    queue = []
    visited = []
    path = []
    queue.append(start)
    visited.append(start)
    path.append(start)
    while queue:
        curr = queue.pop(0)
        if curr == end:
            return path
        for neighbor in neighbor_func(curr):
            if neighbor not in visited:
                if between(neighbor, start, end):
                    path.append(neighbor)
                    start = neighbor
                queue.append(neighbor)
                visited.append(neighbor)


s = Node(-7, 8)
e = Node(-5, -4)
print(*breadth_first_search(s, e, four_nei))
