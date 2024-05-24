mark = 1

rows, columns = map(int, input().split())

current_r = 0
current_c = 0
column_index = 0
row_index = 0

list0 = [
    [-1 for _ in range(columns)]
    for _ in range(rows)
]

for row in range(rows):
    for column in range(columns):
        list0[current_r][current_c] = mark
        current_r += 1
        current_c -= 1
        mark += 1
        # 대각선 처음으로 오면 새로줄이 다시 뒤로 가야함
        if current_c < 0 or current_r == rows:
            column_index += 1
            if column_index == columns:
                row_index += 1
                if row_index == rows:
                    row_index = rows - 1
                column_index = columns - 1
            current_c = column_index
            current_r = row_index


for row in range(rows):
    for column in range(columns):
        print(list0[row][column], end=" ")
    print()