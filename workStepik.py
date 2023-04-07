n = 5
c = 0
matrix = [input().split() for i in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            c = abs(2 - i) + abs(2 - j)
print(c)
