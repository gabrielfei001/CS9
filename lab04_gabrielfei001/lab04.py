from Stack import Stack
def solveMaze(maze, startX, startY):
    solved = False
    stack1 = Stack()
    steps = 1
    currX = startX
    currY = startY
    maze[currX][currY] = steps
    stack1.push([currX, currY])
    emptyCount = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == ' ' or maze[i][j] == 'G':
                emptyCount = emptyCount + 1
    while steps != emptyCount + 1:
        if maze[currX - 1][currY] == 'G':
            currX = currX - 1
            stack1.push([currX,currY])
            solved = True
            return solved
        if maze[currX][currY + 1] == 'G':
            currY = currY + 1
            stack1.push([currX,currY])
            solved = True
            return solved
        if maze[currX + 1][currY] == 'G':
            currX = currX + 1
            stack1.push([currX,currY])
            solved = True
            return solved
        if maze[currX][currY - 1] == 'G':
            currY = currY - 1
            stack1.push([currX,currY])
            solved = True
            return solved
        elif maze[currX - 1][currY] == ' ':
            steps = steps +  1
            currX = currX - 1
            maze[currX][currY] = steps
            stack1.push([currX,currY])
        elif maze[currX][currY + 1] == ' ':
            steps = steps + 1
            currY = currY + 1
            maze[currX][currY] = steps
            stack1.push([currX,currY])
        elif maze[currX + 1][currY] == ' ':
            steps = steps + 1
            currX = currX + 1
            maze[currX][currY] = steps
            stack1.push([currX,currY])
        elif maze[currX][currY - 1] == ' ':
            steps = steps + 1
            currY = currY - 1
            maze[currX][currY] = steps
            stack1.push([currX,currY])
        if maze[currX - 1][currY] != ' ' and maze[currX - 1][currY] != 'G':
            if maze[currX][currY + 1] != ' ' and maze[currX][currY + 1] != 'G':
                if maze[currX + 1][currY] != ' ' and maze[currX + 1][currY] != 'G':
                    if maze[currX][currY - 1] != ' ' and maze[currX][currY - 1] != 'G':
                        if stack1.size() > 1 and stack1.is_empty() == False:
                            stack1.pop()
                            previous = stack1.peek()
                            currX = previous[0]
                            currY = previous[1]
    return solved
