from search.algorithms.breadth_first_search import Queue


def search(start, get_frontier, is_goal, successors):
    frontier = get_frontier(start)
    explored = set()
    while frontier:
        path = frontier.pop()
        current_state = path[-1]
        if is_goal(current_state):
            return path
        for state in successors(current_state):
            if state not in explored:
                explored.add(state)
                new_path = path + [state]
                frontier.push(new_path)
    raise ValueError('No path found')


def bfs_frontier(start):
    frontier = Queue()
    frontier.push([start])
    return frontier


