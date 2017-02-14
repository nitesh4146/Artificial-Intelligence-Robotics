# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
grid = [[0, 1],
        [0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]
    closed[0][0] = 1
    found = False
    failed = False
    temp = []
    goal = [len(grid)-1, len(grid[0])-1]
    print 'Goal is', goal

    while found is False and failed is False:
        if len(open) == 0:
            failed = True
            print 'Unsuccessful!!'
            print open
            break
        else:
            open.sort()
            open.reverse()
            temp = open.pop()
            print '---'
            print 'take list item:', temp
            x = temp[1]
            y = temp[2]
            g = temp[0]

            if x == goal[0] and y == goal[1] :
                found = True
                print 'Success!!!!!!!!!'
                print temp
                break

            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                # print x2, y2
                if x2 >= 0 and y2 >= 0 and x2 < len(grid) and y2 < len(grid[0]):
                    # print 'inside job'
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2, x2, y2])
                        closed[x2][y2] = 1
                    # else:
                        # print 'closed or blocked'
                # else:
                    # print 'outside grid'
        print 'new open list:', open

    return temp

search()