def neighbor_proc(i, j):
    return [
        (i - 1, j - 1),  # Upper-left
        (i - 1, j),  # Up
        (i - 1, j + 1),  # Upper-right
        (i, j + 1),  # Right
        (i + 1, j + 1),  # Bottom-right
        (i + 1, j),  # Down
        (i + 1, j - 1),  # Bottom-left
        (i, j - 1),  # Left
    ]


def neighbor_gen(nodes):
    temp_holder = []

    for i_x in range(len(nodes)):
        row = []
        for i_y in range(len(nodes[i_x])):
            hold = []
            if "pb" in nodes[i_x][i_y]:
                hold.append("pb")
            elif "pw" in nodes[i_x][i_y]:
                hold.append("pw")
            loc_neigh = neighbor_proc(i_x, i_y)
            # print(f'processing ({i_x},{i_y})')
            for x, y in loc_neigh:
                if x < 0 or y < 0 or x > len(nodes) - 1 or y > len(nodes[0]) - 1:
                    hold.append("pw")
                else:
                    if "pb" in nodes[x][y]:
                        hold.append("pb")
                    elif "pw" in nodes[x][y]:
                        hold.append("pw")
            row.append(hold)
        temp_holder.append(row)

    return temp_holder
