import math
from queue import PriorityQueue

def shortest_path(graph, start, goal):
    print("shortest path called")
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)

    prev = {start: None}
    score = {start: 0}

    while not pathQueue.empty():
        curr = pathQueue.get()
        if curr == goal:
            generatePath(prev, start, goal)

        for node in graph.roads[curr]:
            update_score = score[curr] + \
                measure(graph.intersections[curr], graph.intersections[node])

            if node not in score or update_score < score[node]:
                score[node] = update_score
                totalScore = update_score + \
                    measure(graph.intersections[curr],
                            graph.intersections[node])
                pathQueue.put(node, totalScore)
                prev[node] = curr

    return generatePath(prev, start, goal)


def measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def generatePath(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path

