def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError('Różna kształt')
    for row_i in range(len(a)): #po indeksach ponieważ range
        print(f'Wiersze: {row_i} z obu macierzy:')
        print('a:', a[row_i])
        print('b:', b[row_i])
        for col_i in range(len(a[row_i])):
            #print(a[row_i][col_i])
            #print(b[row_i][col_i])
            #print(a[row_i][col_i]+b[row_i][col_i])
            new_row = []
            for col_i in range(len(a[row_i])):
                new_row.append(a[row_i][col_i] + b[row_i][col_i])


def sub_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError('Różna kształt')
    for row_i in range(len(a)): #po indeksach ponieważ range
        for col_i in range(len(a[row_i])):
            new_row = []
            for col_i in range(len(a[row_i])):
                new_row.append(a[row_i][col_i] - b[row_i][col_i])

if __name__ == '__main__':
    a = [
        [1,2,3],
        [4,5,6],
    ]
    b = [
        [9,8,7],
        [6,5,4],
    ]

    results = add_matrices(a, b)