'''
Assumptions: n x n maze. All positive number values in maze coordinates
param: mazeSize : int
returns: empty action list if goal state and a list of all moves to be made if otherwise
link: http://web.cecs.pdx.edu/~edam/Reports/2001/DWillardson.pdf?utm_source=rb-community&utm_medium=forum&utm_campaign=maze-solving-robot-flood-fill-algorithm-updated-w-video
'''





def floodfill(mazeSize):

    target = self.helper.get_goal_state()
    a_target = (3 * 0.36, 2 * 0.36)
    current = self.helper.get_initial_state()
    # state_rep = {target: 0}
    # get matrix with values
    matrix = gen(mazeSize, a_target)
    action_list = list()
    visited = list()
    print matrix
    while(not self.helper.is_goal_state(current)):
        if current not in visited:
            visited.append(current)
            # get next states
            # assumes only valid
            next_states = self.helper.get_successor(current)
            a_dict = {}
            for action in next_states:
                next_state, cost = next_states[action]
                x = int(next_state[0])
                y = int(next_state[1])
                cost = matrix[x][y]
                a_dict[action] = cost

            next_move = min(a_dict.keys(), key=(lambda k: a_dict[k]))
            action_list.append(next_move)
            current = next_states[next_move]

    return action_list

def gen(size, goal):
    x = int(goal[0]/0.36)-1
    y = int(goal[1]/0.36)-1
    result = [[0]*size for a in range(size)]

    for i in range(len(result)):
        for j in range(len(result[i])):
            if (x == i) and (y == j):
                continue
            else:
                result[i][j] = flood_manhattan(x, i, y, j)

    return result


def flood_manhattan(x, x1, y, y1):
    return abs(x - x1) + abs(y - y1)



floodfill(5)




