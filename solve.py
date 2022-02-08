from kociemba import solver

# colors1 = [[[0, 255, 255], [255, 255, 255], [0, 255, 0], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 0]], [[0, 0, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 0], [255, 255, 255]], [[0, 255, 0], [0, 165, 255], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 255], [0, 165, 255], [0, 0, 255], [0, 165, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 165, 255], [255, 255, 255], [255, 255, 255], [0, 255, 255]], [[0, 165, 255], [0, 165, 255], [0, 165, 255], [0, 255, 0], [0, 165, 255], [0, 255, 0], [0, 0, 255], [0, 165, 255], [0, 255, 255]], [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]]]

def solve_string(colors):
    check_lst = [['F', colors[0][4]], ['U', colors[1][4]], ['L', colors[2][4]], ['B', colors[3][4]], ['D', colors[4][4]], ['R', colors[5][4]]]
    s = ""
    # Upper
    for i in range(2, -1, -1):
        for j in range(6):
            if colors[1][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(5, 2, -1):
        for j in range(6):
            if colors[1][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(8, 5, -1):
        for j in range(6):
            if colors[1][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    # Right
    for i in range(2, -1, -1):
        for j in range(6):
            if colors[5][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(5, 2, -1):
        for j in range(6):
            if colors[5][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(8, 5, -1):
        for j in range(6):
            if colors[5][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    # Front
    for i in range(2, -1, -1):
        for j in range(6):
            if colors[0][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(5, 2, -1):
        for j in range(6):
            if colors[0][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(8, 5, -1):
        for j in range(6):
            if colors[0][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    # Down
    for i in range(8, -1, -3):
        for j in range(6):
            if colors[4][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(7, -2, -3):
        for j in range(6):
            if colors[4][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(6, -3, -3):
        for j in range(6):
            if colors[4][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    #Left
    for i in range(0, 9, 3):
        for j in range(6):
            if colors[2][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(1, 10, 3):
        for j in range(6):
            if colors[2][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(2, 11, 3):
        for j in range(6):
            if colors[2][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    #Back
    for i in range(0, 9, 3):
        for j in range(6):
            if colors[3][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(1, 10, 3):
        for j in range(6):
            if colors[3][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    for i in range(2, 11, 3):
        for j in range(6):
            if colors[3][i] == check_lst[j][1]:
                s = s + check_lst[j][0]
                break
    R = solver.solve(cubestring=s, max_length=12, timeout=5)
    solution = list(map(str,R.split()))
    print("SOLUTION")
    print(R)
    print(f"no. of moves = {len(solution)}")
    return(solution)













