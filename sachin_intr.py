""" Assuming the matrix is square matrix then the diagonals are a[i][i]"""

sum = 0
mat = [[11,33,11],[23,4,2],[5,6,22]]
for i in range(0,len(mat)):
    sum = sum + mat[i][i]
print (sum)
