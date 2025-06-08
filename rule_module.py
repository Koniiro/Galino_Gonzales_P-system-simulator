# obj_list, x, y, neigh" need active
import re

trident = [
    6,
    12,
    14,
    18,
    24,
    26,
    28,
    30,
    36,
    38,
    44,
    46,
    48,
    50,
    56,
    58,
    60,
    62,
    66,
    72,
    74,
    96,
    98,
    104,
    106,
    112,
    114,
    120,
    122,
    124,
    126,
    132,
    134,
    140,
    142,
    144,
    146,
    152,
    154,
    156,
    158,
    164,
    166,
    172,
    174,
    176,
    178,
    184,
    186,
    188,
    190,
    192,
    194,
    200,
    202,
    224,
    226,
    232,
    234,
    240,
    242,
    248,
    250,
    252,
    258,
    262,
    264,
    266,
    270,
    286,
    288,
    290,
    294,
    296,
    298,
    302,
    318,
    384,
    386,
    390,
    392,
    394,
    398,
    414,
    416,
    418,
    422,
    424,
    426,
    430,
    448,
    450,
    454,
    456,
    458,
    462,
    480,
    482,
    486,
    488,
    490,
    496,
    498,
    504,
]


def rule_01(obj_list, i, h, neigh, active):
    if "s0" in obj_list and "pw" in obj_list:
        return list(map(lambda x: "s1" if x == "s0" else x, obj_list))
    else:
        return obj_list


def rule_02(obj_list, i, h, neigh, active):
    y = "s0"
    temp_list = []
    if y in obj_list:
        temp_list = list(map(lambda x: "s11" if x == y else x, obj_list))
        ij = i + h
        temp_list.append(f"h{ij}")
        return temp_list
    else:
        return obj_list


def rule_03(obj_list, i, h, neigh, active):
    y = "s1"
    if y in obj_list:
        # letter, number = re.match(r"([a-zA-Z]+)(\d+)", s)
        return list(map(lambda x: "s2" if x == y else x, obj_list))
    else:
        return obj_list


# no need to implement rule 03 as it simply replies s2 with s2 again
# def rule_04(obj_list, i, h, neigh, active):
#     y="s2"
#     if y in obj_list:
#         return list(map(lambda x: "s2" if x == y else x, obj_list))


def rule_05(obj_list, i, h, neigh, active):
    y = "h"
    h_holder = ""
    h_ind = 0
    pattern = r"^h\d+$"  # Matches "h" followed by one or more digits
    h_exists = any(re.match(pattern, item) for item in obj_list)

    if h_exists and "s11" in obj_list:
        # return list(map(lambda x: "s2" if x == y else x, obj_list))
        for i in range(len(obj_list)):
            if "h" in obj_list[i]:
                h_holder = obj_list[i]
                h_ind = i
                break
        val = int(h_holder[1:])
        while val > 1:
            val -= 2
        obj_list.pop(h_ind)
        obj_list.append(f"h{val}")
        return obj_list
    else:
        return obj_list


def rule_06(obj_list, i, h, neigh, active):
    y = "s11"
    if y in obj_list:
        return list(map(lambda x: "s12" if x == y else x, obj_list))
    else:
        return obj_list


# def rule_07(obj_list, i, h, neigh, active, active, active):
#     pass


def rule_08(obj_list, i, h, neigh, active):
    y = "s12"
    h_holder = ""
    h_ind = 0
    temp_list = []
    pattern = r"^h\d+$"  # Matches "h" followed by one or more digits
    h_exists = any(re.match(pattern, item) for item in obj_list)

    if h_exists and y in obj_list:
        temp_list = list(map(lambda x: "s13" if x == y else x, obj_list))
        for i in range(len(obj_list)):
            if "h" in obj_list[i]:
                h_holder = obj_list[i]
                h_ind = i
                break
        val = int(h_holder[1:])
        temp_list.pop(h_ind)
        if val == 0:
            temp_list.append(f"h{1}")
        else:
            temp_list.append(f"h{0}")
        return temp_list
    else:
        return obj_list


def rule_09(obj_list, i, h, neigh, active):
    y = "s13"
    h_ind = 0
    val = 0
    for i in obj_list:
        if "h" in i:
            val = int(i[1:])
            break

    if y in obj_list and val == active:
        return list(map(lambda x: "s14" if x == y else x, obj_list))
    else:
        return obj_list


def rule_10(obj_list, i, h, neigh, active):
    y = "s13"
    if y in obj_list:
        return list(map(lambda x: "s34" if x == y else x, obj_list))
    else:
        return obj_list


def rule_11(obj_list, i, h, neigh, active):
    y = "s14"
    tride = 0
    temp_list = []
    for x in range(9):
        if neigh[x] == "pw":
            tride += 2**x

    if y in obj_list and tride in trident and "pb" in obj_list:
        temp_list = list(map(lambda x: "s2" if x == y else x, obj_list))
        ind = temp_list.index("pb")
        temp_list.pop(ind)
        temp_list.append("pw")
        return temp_list, 1
    else:
        return obj_list, 0


# def rule_12(obj_list, i, h, neigh, active):
#    pass


def rule_13(obj_list, i, h, neigh, active):
    y = "s14"
    if y in obj_list:
        return list(map(lambda x: "s12" if x == y else x, obj_list))
    else:
        return obj_list


def rule_14(obj_list, i, h, neigh, active):
    y = "s34"
    if y in obj_list:
        return list(map(lambda x: "s12" if x == y else x, obj_list))
    else:
        return obj_list


# i=1
# h=0
# neigh=["pb","pb","pb","pb","pw","pw","pw","pw","pw"]
# x=["pw","s1"]
# active=1
# print(rule_03(x,i,h,neigh,active))
# functions = {
#     "rule_01": rule_01,
#     "rule_02": rule_02,
#     "rule_03": rule_03,
#     "rule_05": rule_05,
#     "rule_06": rule_06,
#     "rule_08": rule_08,
#     "rule_09": rule_09,
#     "rule_10": rule_10,
#     "rule_11": rule_11,
#     "rule_13": rule_13,
#     "rule_14": rule_14
# }
#
#
# for name, func in functions.items():
#     print(f"Executing {name}:")
#
#     x,neigh=func(x,i,h,neigh,active)
#     print(x)
#     print(neigh)


# x=0
# for i in range(len(neigh)):
#     if neigh[i]=="pw":
#         x+=2**i
# print(x)
# print(x in trident)
#
