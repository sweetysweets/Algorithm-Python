import copy

def print_matrix(visited):
    for i in range(len(visited)):
        print(visited[i])


def getResult(current,visited):
    global path,matrix,A,B,N,M
    x = current[0]
    y = current[1]
    visited[x][y] = True
    visitedcopy1 = copy.deepcopy(visited)
    visitedcopy2 = copy.deepcopy(visited)
    visitedcopy3 = copy.deepcopy(visited)
    visitedcopy4 = copy.deepcopy(visited)
    print("test23", x, y)
    print(x + 1, y)
    print_matrix(visitedcopy2)
    print(x,y+1)
    print_matrix(visitedcopy3)


    if x<0 or y<0 or x>=N or y>=M:
        return
    path[x][y] = path[x][y]
    if x-1>=0: #up
        if matrix[x-1][y] > matrix[x][y] and not visited[x-1][y]:
            path[x-1][y] += path[x][y]
            # visitedcopy1 = visited.copy()
            # visitedcopy1[x - 1][y] = True
            print("some", x, y)
            print(x-1, y)
            print_matrix(path)
            print_matrix(visitedcopy1)
            getResult((x-1,y),visitedcopy1)

    if x + 1 < N:  # down
        if matrix[x + 1][y] > matrix[x][y] and not visited[x+1][y]:
            path[x + 1][y] += path[x][y]

            # visitedcopy2[x +1][y] = True

            print("some", x, y)
            print(x+1, y)
            print_matrix(path)
            print_matrix(visitedcopy2)
            getResult((x + 1, y),visitedcopy2)

    if y + 1 < M:  # right
        if matrix[x ][y+1] > matrix[x][y] and not visited[x][y+1] :
            path[x ][y+1] += path[x][y]

            # visitedcopy3[x][y+1] = True
            print("some", x, y)
            print(x, y+1)
            print_matrix(path)
            print_matrix(visitedcopy3)
            getResult((x , y+1),visitedcopy3)
    if y - 1 >= 0 :  # left
        if matrix[x ][y-1] > matrix[x][y] and not visited[x][y-1]:
            path[x ][y-1] += path[x][y]
            # visitedcopy4[x][y - 1] = True
            print("some", x, y)
            print(x, y-1)
            print_matrix(path)
            print_matrix(visitedcopy4)
            getResult((x, y-1),visitedcopy4)





if __name__ == '__main__':
    global path,matrix,A,B,N,M
    inputs = input().strip().split()
    N = int(inputs[0])
    M = int(inputs[1])
    matrix = [[0 for i in range(M)] for j in range(N)]
    visited = [[False for i in range(M)] for j in range(N)]
    path = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        inputs = input().strip().split()
        for j in range(M):
            matrix[i][j] = int(inputs[j])
    inputs = input().strip().split()
    A = (int(inputs[0]),int(inputs[1]))
    B = (int(inputs[2]), int(inputs[3]))
    path[A[0]][A[1]] =1
    visited[A[0]][A[1]] =True
    getResult(A,visited)
    print(path[B[0]][B[1]]%(10**9))
    # for i in range(N):
    #     print(path[i])



matrix = []
path = []
B = None
A = None
N = 0
M = 0


