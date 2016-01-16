def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

tri = triangle(40)
lastlen = len(tri[-1])
if lastlen % 2 == 0:
    print tri[-1][lastlen / 2] + tri[-1][lastlen / 2 - 1]
else:
    print tri[-1][lastlen / 2 + 1]