def printBoard(queen):
  for n in queen:
    print("- "*n+"Q"+" -"*(len(queen)-n-1))
    
def countAttack(queen):
    count = 0
    for row1 in range( 0, len(queen) ):
        for row2 in range( row1 + 1, len( queen ) ):
            if queen[row1] == queen[row2]:
                count += 1
            elif abs(queen[row1] - queen[row2]) == (row2 - row1):
                count += 1
    return count

def printMatrix (queen):
    matrix = list(queen);
    for n in range(len(queen)):
        for num in range(len(queen)):
            if (queen[n] != num):
                matrix[n] = num;
                print("{:<3}".format(countAttack(matrix)), end="")
                matrix[n] = queen[n];
            else:
                print("{:<3}".format("-"), end="")
        print();

def moveOne (queen):
    matrix = list(queen);
    ans=64;
    row=0;
    col=0;
    for n in range(len(queen)):
        for num in range(len(queen)):
            if (queen[n] != num):
                matrix[n] = num;
                if ans>countAttack(matrix):
                    ans = countAttack(matrix);
                    row = num;
                    col = n;
                matrix[n] = queen[n];
    matrix[col] = row;
    return matrix;
    
def printMatrix2(queen):
    matrix = list(queen);
    for i in range(len(queen)):
        for j in range(len(queen)):
            if i!=j:
                matrix[i] = queen[j];
                matrix[j] = queen[i];
                print("{:<3}".format(countAttack(matrix)), end="")
                matrix[i] = queen[i];
                matrix[j] = queen[j];
            else:
                print("{:<3}".format("-"), end="")
        print();

def moveTwo (queen):
    matrix = list(queen);
    ans=64;
    row=0;
    col=0;
    for i in range(len(queen)):
        for j in range(len(queen)):
            if i!=j:
                matrix[i] = queen[j];
                matrix[j] = queen[i];
                if countAttack(matrix)<ans:
                    ans = countAttack(matrix);
                    row = i
                    col = j
                matrix[i] = queen[i];
                matrix[j] = queen[j];
    matrix[row] = queen[col];
    matrix[col] = queen[row];
    return matrix;