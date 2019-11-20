'''

visit: list of tuples
result: list with all moves made so far
link: http://web.cecs.pdx.edu/~edam/Reports/2001/DWillardson.pdf?utm_source=rb-community&utm_medium=forum&utm_campaign=maze-solving-robot-flood-fill-algorithm-updated-w-video
'''





def floodfill(mazeSize):

    # target = self.helper.get_goal_state()
    target = (3 * 0.36, 2 * 0.36)
    # start = self.helper.get_initial_state()
    state_rep = {target: 0}
    # get matrix with values
    matrix = gen(mazeSize, target)
    print matrix


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




