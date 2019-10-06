
class Node:
    def __init__(self):
        pass
n1 = Node()
n1.val = 1
n1.num = 0
n1.neighbors = set([3,1,2])

n2 = Node()
n2.val = 4
n2.num = 1
n2.neighbors = set([3,0,2])

n3 = Node()
n3.val = 6
n3.num = 2
n3.neighbors = set([1,0])

n4 = Node()
n4.val = 2
n4.num = 3
n4.neighbors = set([1,0])

G = {0:n1, 1:n2, 2:n3, 3:n4}
import math
def pathsp(graph,n1,n2):
    paths = []
    def dfs(n, curpath):
        nonlocal paths
        nonlocal n2
        nonlocal graph
        if n.num == n2.num:
            curpath.append(n2.num)
            paths.append(curpath)
            return
        curpath.append(n.num)
        temp = n.val
        n.val = float('nan')
        for neigh in n.neighbors:
            if not math.isnan(graph[neigh].val): dfs(graph[neigh], curpath.copy())
        n.val = temp
    dfs(n1,[])
    for path in paths: print(path)

pathsp(G,n1,n4)