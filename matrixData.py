import numpy as np

# tragram pieces
largeTriangle = np.array([[0,4,1,0],
                          [4,3,9,1]])
largeTriangleR = np.array([[1,0],
                           [9,1],
                           [3,5],
                           [5,0]])
largeTriangleD = np.array([[2,9,3,5],
                           [0,2,5,0]])
largeTriangleL = np.array([[0,4],
                           [4,3],
                           [2,9],
                           [0,2]])
largeTri = np.array([largeTriangle,largeTriangleR,largeTriangleD,largeTriangleL])

smallTriangle = np.array([[0,4],
                          [4,3]])
smallTriangleR = np.array([[1,0],
                           [9,1]])
smallTriangleD = np.array([[3,5],
                           [5,0]])
smallTriangleL = np.array([[2,9],
                           [0,2]])
smallTri = np.array([smallTriangle,smallTriangleR,smallTriangleD,smallTriangleL])

tinyTriangle = np.array([[4,1]])
tinyTriangleR = np.array([[1],
                          [5]])
tinyTriangleD = np.array([[2,5]])
tinyTriangleL = np.array([[4],
                          [2]])
tinyTri = np.array([tinyTriangle,tinyTriangleR,tinyTriangleD,tinyTriangleL])

square = np.array([[4,1],
                   [2,5]])
squareR = np.array([[4,1],
                    [2,5]])
squareD = np.array([[4,1],
                    [2,5]])
squareL = np.array([[4,1],
                    [2,5]])
squareTri = np.array([square,squareR,squareD,squareL])

parallelogram = np.array([[4,3,5]])
parallelogramR = np.array([[1],
                           [9],
                           [2]])
parallelogramD = np.array([[4],
                           [3],
                           [5]])
parallelogramL = np.array([[2,9,1]])
parllTri = np.array([parallelogram,parallelogramR,parallelogramD,parallelogramL])

# 13 initial states
otherState =    np.array([[0,0,0,0,0,0,0,0],
                          [0,0,4,1,4,1,0,0],
                          [0,4,3,9,3,9,1,0],
                          [0,2,9,3,9,3,5,0],
                          [0,0,2,9,3,5,0,0],
                          [0,0,0,2,5,0,0,0]])

more =          np.array([[0,0,0,0,0,0,0,0],
                          [0,0,4,3,9,1,0,0],
                          [0,4,3,9,3,9,1,0],
                          [0,2,9,3,9,3,5,0],
                          [0,0,2,9,3,5,0,0],
                          [0,0,0,2,5,0,0,0]])

initialState1 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,4,1,0,0,0],
                          [0,0,4,3,9,1,0,0],
                          [0,4,3,9,3,9,1,0],
                          [4,3,9,3,9,3,9,1]])

initialState2 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,3,9,3,9,0,0],
                          [0,0,9,3,9,3,0,0],
                          [0,0,3,9,3,9,0,0],
                          [0,0,9,3,9,3,0,0]])

initialState3 = np.array([[0,0,0,4,1,0,0,0],
                          [0,0,4,3,9,1,0,0],
                          [0,4,3,9,3,5,0,0],
                          [4,3,9,3,5,0,0,0],
                          [2,9,3,5,0,0,0,0],
                          [0,2,5,0,0,0,0,0]])

initialState4 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,4,3,9,3,5],
                          [0,0,4,3,9,3,5,0],
                          [0,4,3,9,3,5,0,0],
                          [4,3,9,3,5,0,0,0]])

initialState5 = np.array([[0,0,0,4,3,9,3,5],
                          [0,0,4,3,9,3,5,0],
                          [0,0,3,9,3,5,0,0],
                          [0,0,9,3,5,0,0,0],
                          [0,0,3,5,0,0,0,0],
                          [0,0,5,0,0,0,0,0]])

initialState6 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,4,1,0,0,0,0],
                          [0,4,3,9,1,0,0,0],
                          [4,3,9,3,5,0,0,0],
                          [3,9,3,5,0,0,0,0],
                          [9,3,5,0,0,0,0,0],
                          [3,5,0,0,0,0,0,0],
                          [5,0,0,0,0,0,0,0]])

initialState7 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [3,9,1,0,0,0,0,0],
                          [9,3,9,1,0,0,0,0],
                          [3,9,3,9,1,0,0,0],
                          [9,3,9,3,9,1,0,0]])

initialState8 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,4,3,9,3,9,0],
                          [0,4,3,9,3,9,3,0],
                          [4,3,9,3,9,3,5,0]])

initialState9 = np.array([[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [3,9,3,9,1,0,0,0],
                          [9,3,9,3,5,0,0,0],
                          [3,9,3,5,0,0,0,0],
                          [9,3,5,0,0,0,0,0],
                          [2,5,0,0,0,0,0,0]])

initialState10 = np.array([[0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,4,3,9,1,0,0,0],
                           [4,3,9,3,9,1,0,0],
                           [2,9,3,9,3,5,0,0],
                           [0,2,9,3,5,0,0,0]])

initialState11 = np.array([[0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,4,3,9,3,9,1,0],
                           [4,3,9,3,9,3,5,0],
                           [2,9,3,9,3,5,0,0]])

initialState12 = np.array([[0,0,0,0,0,0,0,0],
                           [4,3,9,1,0,0,0,0],
                           [3,9,3,9,1,0,0,0],
                           [9,3,9,3,5,0,0,0],
                           [2,9,3,5,0,0,0,0],
                           [0,2,5,0,0,0,0,0]])

initialState13 = np.array([[0,0,0,0,0,0,0,0],
                           [0,0,4,3,9,0,0,0],
                           [0,4,3,9,3,0,0,0],
                           [4,3,9,3,5,0,0,0],
                           [3,9,3,5,0,0,0,0],
                           [9,3,5,0,0,0,0,0]])

initialStates = [initialState1,initialState2,initialState3,initialState4,
                 initialState5,initialState6,initialState7,initialState8,
                 initialState9,initialState10,initialState11,initialState12,
                 initialState13,otherState]

convexShapes = [[4,8],[4,4],[6,6],[4,8],
                [6,6],[7,5],[4,6],[3,7],
                [5,5],[4,6],[3,7],[5,5],
                [5,5]]
