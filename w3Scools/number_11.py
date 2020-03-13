m = int(input('Rows:\n'))
n = int(input('Columns:\n'))
two_d_array = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i*j)
    two_d_array.append(row)
print(two_d_array)