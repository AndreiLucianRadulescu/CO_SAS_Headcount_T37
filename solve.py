input=[[1,1,0,0,0,0,1,1],

 [1,1,0,1,1,0,1,1],

 [0,0,0,1,1,0,0,0],

 [1,1,0,1,1,0,1,1],

 [1,1,0,0,0,0,1,1]]

def visit(matrix, i, j, rows, cols):
    if i < 0 or j < 0 or i > rows-1 or j > cols-1 or matrix[i][j] != 1:
        return 0
    
    matrix[i][j] = 2
    return 1 + visit(matrix,i+1,j,rows,cols) + visit(matrix,i,j+1,rows,cols)

def find_clusters(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    teams = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                temp = visit(matrix, i, j, rows, cols)
                teams.append(temp)

    return teams

if __name__ == "__main__":
    teams = find_clusters(input)
    print(teams)
    print(f'{len(teams)} teams of {teams} totalling {sum(teams)}')