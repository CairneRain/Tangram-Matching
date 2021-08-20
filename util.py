import numpy as np
from matrixData import largeTri,smallTri,tinyTri,squareTri,parllTri,initialStates,more

# global variable
pieces = []
pieceLen = []
step = []
ijValues = []
initialState = initialStates[0]
currentState = np.zeros_like(initialState)
success_steps = []
iteration_depth = 7
iteration_counter = np.zeros([iteration_depth,4],dtype=int)
parameters = []
iteration_time = 0

# initialize data
def initialData(model):
    global pieces,pieceLen,step,ijValues,initialState,currentState,success_steps,iteration_counter,parameters,iteration_depth
    pieces = []
    pieceLen = []
    step = []
    ijValues = []
    initialState = initialStates[0]
    currentState = np.zeros_like(initialState)
    success_steps = []
    iteration_depth = 7
    iteration_counter = np.zeros([iteration_depth,4],dtype=int)
    parameters = []
    iteration_time = 0

    if model == 999:
        pieces = [largeTri,largeTri,parllTri,squareTri,smallTri,tinyTri,tinyTri,tinyTri]
        pieceLen = [4,4,2,2,2,3,2,2 * np.sqrt(2)]
        ijValues = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],
                    [0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        initialState = more
        iteration_depth = 8
        step = [np.ones([6,8],dtype=int) for i in range(iteration_depth+1)]

    else:
        pieces = [largeTri,largeTri,tinyTri,tinyTri,parllTri,squareTri,smallTri]
        # pieceLen = [4,4,2,2,2 * np.sqrt(2),2,3]
        pieceLen = [4,4,2,2,3,2,2 * np.sqrt(2)]

        step = [np.ones([6,8],dtype=int) for i in range(iteration_depth+1)]

        ijValues = [[0,0,0],[0,0,0],[0,0,0],
                    [0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        initialState = initialStates[model]


    currentState = np.zeros_like(initialState)
    currentState += initialState
    step[0] = initialState

    success_steps = []
    iteration_counter = np.zeros([iteration_depth,4],dtype=int)

    parameters = []


# result output
def getPid(piece):
    piece = piece[piece.sum(axis=1) != 0,:]
    piece = piece[:,piece.sum(axis=0) != 0]
    for t in range(len(largeTri)):
        if np.all(piece.shape == largeTri[t].shape) and np.all(piece == largeTri[t]):
            return t
    for t in range(len(smallTri)):
        if np.all(piece.shape == smallTri[t].shape) and np.all(piece == smallTri[t]):
            return t + 4
    for t in range(len(tinyTri)):
        if np.all(piece.shape == tinyTri[t].shape) and np.all(piece == tinyTri[t]):
            return t + 8
    for t in range(len(parllTri)):
        if np.all(piece.shape == parllTri[t].shape) and np.all(piece == parllTri[t]):
            return t + 12
    if np.all(piece.shape == squareTri[0].shape) and np.all(piece == squareTri[0]):
        return 16
    return -1


def getResult():
    global parameters,iteration_time
    x = 1
    number = 0
    for s in success_steps:
        print("solution ",x)
        x += 1
        for state in s:
           print(state)
        print("Insert:")
        # ppp = []
        for m in range(0,len(s) - 1):
            insertPiece = s[m] - s[m + 1]
            print(insertPiece)
            row = 0
            column = 0
            for c in range(insertPiece.shape[1]):
                match = False
                for r in range(insertPiece.shape[0]):
                    if insertPiece[r][c] != 0:
                        column = c
                        match = True
                        break
                if match:
                    break
            for r in range(insertPiece.shape[0]):
                match = False
                for c in range(insertPiece.shape[1]):
                    if insertPiece[r][c] != 0:
                        row = r
                        match = True
                        break
                if match:
                    break
            pid = getPid(insertPiece)
            parameters.append([row + 1,column + 1,pid,m])
    #         ppp.append([row + 1,column + 1,pid,m])
    #     if ppp not in parameters:
    #         parameters.append(ppp)
    #         number += 1
    # parameters = np.array(parameters).reshape([number,iteration_depth,4])
    parameters = np.array(parameters).reshape([len(success_steps),iteration_depth,4])
    print(parameters)
    # print(parameters)
    # try topology
    # print(iteration_counter)
    iteration_time = sum(sum(iteration_counter))
    print("iteration time: ",iteration_time)


def isMatch(window,piece):
    match = True
    for i in range(window.shape[0]):
        for j in range(window.shape[1]):
            if window[i][j] == piece[i][j]:  # continue the next square
                continue
            elif window[i][j] - piece[i][j] < 0:  # not match
                match = False
                break
            elif window[i][j] in [4,5,9] and piece[i][j] in [1,2,3]:  # not match
                match = False
                break
            elif (window[i][j] == 2 and piece[i][j] == 1) or (
                    window[i][j] == 5 and piece[i][j] == 4):  # cannot be minus
                match = False
                break
        if not match:
            break
    if not match:
        return False
    else:
        return True


def slidingWindow(inputDiagram,state,ijIndex):
    piece = inputDiagram[ijValues[ijIndex][2]]
    row = piece.shape[0]
    column = piece.shape[1]

    # continue the previous search
    i = ijValues[ijIndex][0]
    j = ijValues[ijIndex][1]
    if j == state.shape[1] - column:
        i += 1
        j = 0
    else:
        j += 1

    while i < state.shape[0] - row + 1:
        while j < state.shape[1] - column + 1:
            window = state[i:i + row,j:j + column]
            r = isMatch(window,piece)
            if r:
                state[i:i + row,j:j + column] -= piece

                # create new state and store in step
                newState = np.zeros(state.shape,dtype=int)
                newState += state
                step[ijIndex + 1] = newState

                # add back
                state[i:i + row,j:j + column] += piece

                ijValues[ijIndex][0] = i
                ijValues[ijIndex][1] = j
                return True
            j += 1
        j = 0
        i += 1
    return False


# reset ijValues from n to last
def clearIJ(n):
    for i in range(6 - n + 1):
        ijValues[6 - i] = [0,0,0]


def dfs(ijIndex):
    while True:
        # final match
        if ijIndex == iteration_depth and np.all(step[iteration_depth] == 0):
            success_steps.append(step.copy())
            step[ijIndex] = np.ones([6,8],dtype=int)
            return

        i = 0
        while i < 4:  # for 4 different angles


            ijValues[ijIndex][2] = i
            find = slidingWindow(pieces[ijIndex],step[ijIndex],ijIndex)
            # print("try piece ",ijIndex,"   ",ijValues[ijIndex])

            if find:
                iteration_counter[ijIndex][i] += 1  # record
                # print("ijIndex:",ijIndex)
                dfs(ijIndex + 1)  # continue next step

            else:  # not found, try other
                clearIJ(ijIndex)
                i += 1
                # for square only
                if i == 1 and pieces[ijIndex][i].shape == (2,2) and np.all(pieces[ijIndex][i] == squareTri[0]):
                    return
                if i == 4:  # the 4 conditions cannot match
                    return


def Dfs_start(model):
    initialData(model)
    # random order
    if iteration_depth == 7:
        pieces[0] = largeTri
        pieces[1] = smallTri
        pieces[2] = squareTri
        pieces[3] = tinyTri
        pieces[4] = largeTri
        pieces[5] = parllTri
        pieces[6] = tinyTri
    dfs(0)
    getResult()
    return parameters,iteration_time

# greedy / A* search
def search(ijIndex,seqIndex):
    while True:
        # final match
        if ijIndex == iteration_depth and np.all(step[iteration_depth] == 0):
            success_steps.append(step.copy())
            step[ijIndex] = np.ones([6,8],dtype=int)
            return

        i = 0
        while i < 4:  # for 4 different angles

            # print("try piece ",ijIndex,"   ",ijValues[ijIndex])

            ijValues[ijIndex][2] = i
            find = slidingWindow(pieces[seqIndex[ijIndex]],step[ijIndex],ijIndex)

            if find:
                iteration_counter[ijIndex][i] += 1  # record

                search(ijIndex + 1,seqIndex)  # continue next step
            else:  # not found, try other
                clearIJ(ijIndex)
                i += 1
                # only for square
                if i == 1 and np.all(pieces[seqIndex[ijIndex]][i] == squareTri[0]):
                    return
                if i == 4:  # the 4 conditions cannot match
                    return


# output the sequence
def decideGreedySequence():
    hn = np.zeros(len(pieces))
    hn += 32
    for i in range(len(pieces)):
        for k in pieces[i][0]:
            for j in k:
                if j in [3,9]:
                    hn[i] -= 2
                if j in [1,2,4,5]:
                    hn[i] -= 1
                else:
                    pass
    print(hn)
    out = np.argsort(hn)
    return out


# h(n) = the remaining area that is uncovered by the piece
# f(n) = h(n)
def Greedy_start(model):
    initialData(model)

    # decide the sequence
    seqIndex = decideGreedySequence()

    search(0,seqIndex)
    getResult()
    return parameters,iteration_time


# h(n) = the remaining area that is uncovered by the piece
# g(n) = cost of calculation
# f(n) = g(n) + h(n)
def decideAStarSequence(model):
    fn = np.zeros(len(pieces))

    # add h(n) value
    fn += 32
    for i in range(len(pieces)):
        for k in pieces[i][0]:
            for j in k:
                if j in [3,9]:
                    fn[i] -= 2
                elif j in [1,2,4,5]:
                    fn[i] -= 1
                else:
                    pass

    #  add g(n) value
    for t in range(len(pieces)):
        p = pieces[t][0]
        i = initialState.shape[0]
        j = initialState.shape[1]
        m = p.shape[0]
        n = p.shape[1]
        fn[t] += (i - m + 1) * (j - n + 1) / (m + n) * pieceLen[t]

    print(fn)
    out = np.argsort(fn)
    return out

# g(n) = cost of calculation
# h(n) = the remaining area that is uncovered by the piece
# f(n) = g(n) + h(n)
def A_star_start(model):
    initialData(model)
    seqIndex = decideAStarSequence(model)

    search(0,seqIndex)
    getResult()
    return parameters,iteration_time


# A_star_start(0)


# iterate deepening
def iterate(ijIndex,cutoff):
    while True:
        # final match
        if ijIndex == cutoff and np.all(step[cutoff] == 0):
            success_steps.append(step.copy())
            # for i in range(8):
            #     step[i] = np.ones([6,8],dtype=int)
            # step[0] = initialState
            step[iteration_depth] = np.ones([6,8],dtype=int)

            return True
        # return other function when the result is found
        if np.all(step[cutoff] == 0):
            return True

        if ijIndex > cutoff:
            return False

        i = 0
        while i < 4:  # for 4 different angles

            # print("try piece ",ijIndex,"   ",ijValues[ijIndex])

            ijValues[ijIndex][2] = i
            find = slidingWindow(pieces[ijIndex],step[ijIndex],ijIndex)

            if find:
                iteration_counter[ijIndex][i] += 1  # record

                iterate(ijIndex + 1,cutoff)  # continue next step
                # if get:
                #     return True
            else:  # not found, try other
                clearIJ(ijIndex)
                i += 1
                if i == 1 and np.all(pieces[ijIndex][i] == squareTri[0]):
                    return
                if i == 4:  # the 4 conditions cannot match
                    return False


def iterative_deepening_start(model):
    initialData(model)
    total_iteration_time = 0
    for cutoff in range(1,8):
        # random order
        pieces[0] = largeTri
        pieces[1] = largeTri
        pieces[2] = squareTri
        pieces[3] = tinyTri
        pieces[4] = smallTri
        pieces[5] = parllTri
        pieces[6] = tinyTri
        get = iterate(0,cutoff)
        if get or cutoff == iteration_depth:
            getResult()
            total_iteration_time += iteration_time
            break
        else:
            getResult()
            total_iteration_time += iteration_time
            initialData(model)
            # total_iteration_time += iteration_time
    return parameters,total_iteration_time


# cost = the calculation cost
def uniform_cost_sequence():
    cost = np.zeros(len(pieces))

    for t in range(len(pieces)):
        p = pieces[t][0]
        i = initialState.shape[0]
        j = initialState.shape[1]
        m = p.shape[0]
        n = p.shape[1]
        cost[t] += (i - m + 1) * (j - n + 1) / ((m + n) / pieceLen[t])

    print(cost)
    out = np.argsort(cost)
    return out


def uniform_cost_search(model):
    initialData(model)
    seqIndex = uniform_cost_sequence()

    search(0,seqIndex)
    getResult()
    return parameters,iteration_time


# algorithm start
def start(algorithm,model):
    if algorithm == 0:
        return Dfs_start(model)
    elif algorithm == 1:
        return Greedy_start(model)
    elif algorithm == 2:
        return A_star_start(model)
    elif algorithm == 3:
        return uniform_cost_search(model)
    elif algorithm == 4:
        return iterative_deepening_start(model)
