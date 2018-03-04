def has_conflict(arr, row, col, n):
    if arr[row][col] != 0:
        return True

    # Same row
    c = col - 1
    while c >= 0:
        if arr[row][c] == 2:
            break
        if arr[row][c] == 1:
            return True
        c -= 1

    # Same Column
    r = row - 1
    while r >= 0:
        if arr[r][col] == 2:
            break
        if arr[r][col] == 1:
            return True
        r -= 1

    # Upper Diagonal
    counter = 1
    while row - counter >= 0 and col - counter >= 0:
        if arr[row - counter][col - counter] == 2:
            break
        if arr[row - counter][col - counter] == 1:
            return True
        counter += 1

    # Lower Diagonal
    counter = 1
    while row + counter < n and col - counter < n:
        if arr[row + counter][col - counter] == 2:
            break
        if arr[row + counter][col - counter] == 1:
            return True
        counter += 1
    return False


def assign_child_dfs(zoo_matrix, r, col, n, count):
    if count <= 0:
        return True
    if col >= n or r >= n:
        return count <= 0
    row = r
    while row < n and zoo_matrix[row][col] == 2:
        row += 1
    if row >= n:
        return assign_child_dfs(zoo_matrix, r, col + 1, n, count)
    all_conflicts = True
    for row in range(r, n):
        if not has_conflict(zoo_matrix, row, col, n):
            all_conflicts = False
            zoo_matrix[row][col] = 1
            count -= 1
            if assign_child_dfs(zoo_matrix, r, col + 1, n, count) or assign_child_dfs(zoo_matrix, row + 1, col, n, count):
                return True
                zoo_matrix[row][col] = 0
            count += 1
    if all_conflicts:
        return assign_child_dfs(zoo_matrix, r, col + 1, n, count)
    return False
