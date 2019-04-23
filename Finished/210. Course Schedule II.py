'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
4, [[1,0],[2,0],[3,1],[3,2]]

Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

Hints:

This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''


def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    # first need to convert the prerequisites into adjucent list
    adj_list = [[i] for i in range(numCourses)]
    for [x, y] in prerequisites:
        adj_list[y].append(x)
    route = []
    visited = [0 for _ in range(numCourses)]
    # rec_stack = [0 for _ in range(numCourses)]
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            if visited[adj_list[i][j]] == 0:
                dfs(adj_list[i][j], visited, adj_list)

def dfs(m, visited, adj_list):
    visited[m] = 1
    




    print("here I am")



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
findOrder(numCourses, prerequisites)