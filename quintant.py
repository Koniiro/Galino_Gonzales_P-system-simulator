from typing import NewType, Literal

from neighbor_gen_module import neighbor_gen

Grid = NewType("Grid", list[list[list[str]]])

test_grid_odd: Grid = Grid(
    [
        [["1"], ["2"], ["3"], ["4"], ["5"]],
        [["1"], ["2"], ["3"], ["4"], ["5"]],
        [["1"], ["2"], ["3"], ["4"], ["5"]],
        [["1"], ["2"], ["3"], ["4"], ["5"]],
        [["1"], ["2"], ["3"], ["4"], ["5"]],
    ]
)

test_grid_even: Grid = Grid(
    [
        [["1"], ["2"], ["3"], ["4"], ["5"], ["6"]],
        [["1"], ["2"], ["3"], ["4"], ["5"], ["6"]],
        [["1"], ["2"], ["3"], ["4"], ["5"], ["6"]],
        [["1"], ["2"], ["3"], ["4"], ["5"], ["6"]],
        [["1"], ["2"], ["3"], ["4"], ["5"], ["6"]],
        [["1"], ["2"], ["3"], ["4"], ["5"], ["6"]],
    ]
)


def north_west_segment(grid: Grid) -> Grid:
    columns = "even" if len(grid[0]) % 2 == 0 else "odd"
    rows = "even" if len(grid) % 2 == 0 else "odd"
    columns_to_iterate_to = (
        len(grid[0]) // 2 if columns == "even" else len(grid[0]) // 2 + 1
    )
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
    columns_to_iterate_to = (
        len(grid[0]) // 2 if columns == "even" else len(grid[0]) // 2 + 1
    )
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
    columns_to_save = (
        [center_column - 2, center_column - 1, center_column, center_column + 1]
        if columns == "even"
        else [center_column - 1, center_column, center_column + 1]
    )
    rows_to_save = (
        [center_row - 2, center_row - 1, center_row, center_row, center_row + 1]
        if rows == "even"
        else [center_row - 1, center_row, center_row + 1]
    )

    result = Grid(grid.copy())
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if y not in rows_to_save and x not in columns_to_save:
                result[y][x] = ["pw", "s0"]

    return result


def perform_one_skeletonization(grid: Grid, verbose: bool = False) -> tuple[Grid, bool]:
    from rule_module import (
        rule_01,
        rule_02,
        rule_03,
        rule_05,
        rule_06,
        rule_08,
        rule_09,
        rule_10,
        rule_11,
        rule_13,
        rule_14,
    )

    functions = {
        "rule_01": rule_01,
        "rule_02": rule_02,
        "rule_03": rule_03,
        "rule_05": rule_05,
        "rule_06": rule_06,
        "rule_08": rule_08,
        "rule_09": rule_09,
        "rule_10": rule_10,
        "rule_11": rule_11,
        "rule_13": rule_13,
        "rule_14": rule_14,
    }

    active = 1
    did_change = False
    grid = Grid(grid.copy())

    if verbose:
        print("==Initial configuration==")
        from pprint import pp

        pp(grid)

    for name, func in functions.items():
        if verbose:
            print(f"Executing {name}:")

        neyb = neighbor_gen(grid)
        for ix in range(len(grid)):
            for iy in range(len(grid[ix])):
                if name == "rule_11":
                    grid[ix][iy], check = func(  # pyright: ignore[reportArgumentType, reportCallIssue]
                        grid[ix][iy], ix, iy, neyb[ix][iy], active
                    )
                    if check != 0:
                        did_change = True

                else:
                    grid[ix][iy] = func(grid[ix][iy], ix, iy, neyb[ix][iy], active)  # pyright: ignore[reportArgumentType, reportCallIssue]

                if verbose:
                    print(grid[ix][iy])
                    print("-------------")

    return grid, did_change


def rejoin_segments(
    nw: Grid,
    ne: Grid,
    sw: Grid,
    se: Grid,
    central: Grid,
    row: Literal["odd", "even"],
    column: Literal["odd", "even"],
) -> Grid:
    result = Grid([])

    if row == "odd" and column == "odd":
        result = Grid(
            [[[""] for x in range(len(nw[0]) * 2 - 1)] for y in range(len(nw) * 2 - 1)]
        )

        # Add NW to result
        nw_forbidden_row = len(nw) - 1
        nw_forbidden_col = len(nw[0]) - 1

        for y in range(len(nw)):
            for x in range(len(nw[0])):
                if y != nw_forbidden_row and x != nw_forbidden_col:
                    result[y][x] = nw[y][x]

        # Add NE to result
        ne_forbidden_row = len(ne) - 1
        ne_forbidden_col = len(ne[0]) * -1

        for y in range(len(ne)):
            for x in range(-1, ne_forbidden_col - 1, -1):
                if y != ne_forbidden_row and x != ne_forbidden_col:
                    result[y][x] = ne[y][x]

        # Add SW to result
        sw_forbidden_row = len(sw) * -1
        sw_forbidden_col = len(sw[0]) - 1

        for y in range(-1, sw_forbidden_row - 1, -1):
            for x in range(len(sw[0])):
                if y != sw_forbidden_row and x != sw_forbidden_col:
                    result[y][x] = sw[y][x]

        # Add SE to result
        se_forbidden_row = len(se) * -1
        se_forbidden_col = len(se[0]) * -1

        for y in range(-1, se_forbidden_row - 1, -1):
            for x in range(-1, se_forbidden_col - 1, -1):
                if y != se_forbidden_row and x != se_forbidden_col:
                    result[y][x] = se[y][x]

        # Add Central to result
        central_row = len(central) // 2
        central_col = len(central[0]) // 2

        for y in range(len(central)):
            for x in range(len(central[0])):
                if y == central_row or x == central_col:
                    result[y][x] = central[y][x]

    if row == "even" and column == "even":
        result = Grid(
            [[[""] for x in range(len(nw[0]) * 2)] for y in range(len(nw) * 2)]
        )

        # Add NW to result
        nw_forbidden_row = len(nw) - 1
        nw_forbidden_col = len(nw[0]) - 1

        for y in range(len(nw)):
            for x in range(len(nw[0])):
                if y != nw_forbidden_row and x != nw_forbidden_col:
                    result[y][x] = nw[y][x]


if __name__ == "__main__":
    pass
    # from image_proc_module import image_proc

    # img_path = "Test-Cases/Test-A.png"
    # grid: Grid = Grid(image_proc(img_path, 0, 0, 180, 0))
    # print(perform_one_skeletonization(grid, True))
