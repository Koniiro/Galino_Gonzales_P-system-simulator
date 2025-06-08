from neighbor_gen_module import neighbor_gen
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


def SCP_Skeletonizer(nodes, verbose, rule_debug):
    active = 1
    check = 0
    checksum = 0
    rnd = 1
    # Print Initial Configuration
    if verbose == 1:
        print("==Initial Configuration==")
        for x in nodes:
            print(x)

    while True:
        # if verbose==1:
        print(f"Round {rnd}")

        for name, func in functions.items():
            if rule_debug == 1:
                print(f"Executing {name}:")
            neyb = neighbor_gen(nodes)
            for i_x in range(len(nodes)):
                for i_y in range(len(nodes[i_x])):
                    if name == "rule_11":
                        nodes[i_x][i_y], check = func(
                            nodes[i_x][i_y], i_x, i_y, neyb[i_x][i_y], active
                        )
                        checksum += check

                    else:
                        nodes[i_x][i_y] = func(
                            nodes[i_x][i_y], i_x, i_y, neyb[i_x][i_y], active
                        )
                if rule_debug == 1:
                    print(nodes[i_x][i_y])
                    print("---------")

        if checksum == 0:
            break
        checksum = 0
        rnd += 1
    print("=====Finished=====")
    print(f"Rounds Taken: {rnd}")
    if verbose == 1:
        print("Final Configuration")
    final_arr = []
    for x in nodes:
        if verbose == 1:
            print(x)
        final_arr.append(x)
    return final_arr, rnd
