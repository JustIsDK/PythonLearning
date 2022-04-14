def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print('%d*%d=%d' % (col, row, col * row), end='\t')
            col = col + 1

        print('')
        row = row + 1

multiple_table()
