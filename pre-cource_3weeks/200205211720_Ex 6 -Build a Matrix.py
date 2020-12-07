'''
Construct a function build_matrix(rows, cols) that gets 2 numbers representing
number of rows and number of columns, and returns a two dimensional array (you should
build a list of lists). The element value in the i-th row and j-th column of the array
should be i*j.
'''
def build_matrix(rows, cols):
    a = [[i * j for j in range(cols)] for i in range(rows)]
    return a
print(build_matrix(3,5))