from typing import NewType

Grid = NewType("Grid", list[list[str]])

test_grid_odd: Grid = Grid([
    ["1", "2", "3", "4", "5"],
    ["2", "2", "3", "4", "4"],
    ["3", "2", "3", "4", "3"],
    ["4", "2", "3", "4", "2"],
    ["5", "2", "3", "4", "1"],
])

test_grid_even: Grid = Grid([
    ["1", "2", "3", "4", "5", "6"],
    ["2", "2", "3", "4", "5", "5"],
    ["3", "2", "3", "4", "5", "4"],
    ["4", "2", "3", "4", "5", "3"],
    ["5", "2", "3", "4", "5", "2"],
    ["6", "2", "3", "4", "5", "1"],
])

def north_west_segment(grid: Grid) -> Grid:
    columns = "even" if len(grid[0]) % 2 == 0 else "odd"
    rows = "even" if len(grid) % 2 == 0 else "odd"
    columns_to_iterate_to = len(grid[0]) // 2 if columns == "even" else len(grid[0]) // 2 + 1
    rows_to_iterate_to = len(grid) // 2 if rows == "even" else len(grid) // 2 + 1

    result: Grid = Grid([])
    for y in range(rows_to_iterate_to):
        result.append([])
        for x in range(columns_to_iterate_to):
            result[-1].append(grid[y][x])

    return result

def north_east_segment(grid: Grid) -> Grid:
    rows = "even" if len(grid) % 2 == 0 else "odd"
    columns_to_iterate_from = len(grid[0]) // 2
    rows_to_iterate_to = len(grid) // 2 if rows == "even" else len(grid) // 2 + 1

    result: Grid = Grid([])
    for y in range(rows_to_iterate_to):
        result.append([])
        for x in range(columns_to_iterate_from, len(grid[0])):
            result[-1].append(grid[y][x])

    return result

def south_west_segment(grid: Grid) -> Grid:
    columns = "even" if len(grid[0]) % 2 == 0 else "odd"
    columns_to_iterate_to = len(grid[0]) // 2 if columns == "even" else len(grid[0]) // 2 + 1
    rows_to_iterate_from = len(grid) // 2

    result: Grid = Grid([])
    for y in range(rows_to_iterate_from, len(grid)):
        result.append([])
        for x in range(columns_to_iterate_to):
            result[-1].append(grid[y][x])

    return result

def south_east_segment(grid: Grid) -> Grid:
    columns_to_iterate_from = len(grid[0]) // 2
    rows_to_iterate_from = len(grid) // 2

    result: Grid = Grid([])
    for y in range(rows_to_iterate_from, len(grid)):
        result.append([])
        for x in range(columns_to_iterate_from, len(grid[0])):
            result[-1].append(grid[y][x])

    return result

def central_segment(grid: Grid) -> Grid:
    columns = "even" if len(grid[0]) % 2 == 0 else "odd"
    rows = "even" if len(grid) % 2 == 0 else "odd"
    center_column = len(grid[0]) // 2
    center_row = len(grid) // 2
    columns_to_save = [center_column - 2, center_column - 1, center_column, center_column + 1] if columns == "even" else [center_column - 1, center_column, center_column + 1]
    rows_to_save = [center_row - 2, center_row - 1, center_row, center_row, center_row + 1] if rows == "even" else [center_row - 1, center_row, center_row + 1]

    result = Grid(grid.copy())
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if y not in rows_to_save and x not in columns_to_save:
                result[y][x] = ""

    return result


