# obj_list, x, y, neigh" need active
import re
import numpy as np
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


def rule_01(nodes, i, h, neigh, active):
    mask = (nodes[..., 0] == 'pw') & (nodes[..., 1] == 's0')
    nodes[mask, 1] = 's1'
    return nodes


def rule_02(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's0')
    nodes[mask, 1] = 's11'
    coords = np.argwhere(mask)
    for x, y in coords:
        nodes[x, y, 2] = f"h{x+y}"
    return nodes

def rule_03(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's1') 
    nodes[mask, 1] = 's2'
    return nodes


# no need to implement rule 04 as it simply replies s2 with s2 again
# def rule_04(obj_list, i, h, neigh, active):
#     y="s2"
#     if y in obj_list:
#         return list(map(lambda x: "s2" if x == y else x, obj_list))


def rule_05(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's11') 
    w=nodes[mask, 2]

    val=np.char.lstrip(nodes[mask, 2].astype(str), 'h').astype(int) % 2
    res=np.char.add("h",val.astype(str))
 
    nodes[mask, 2]=res
 
    return nodes


def rule_06(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's11') 
    nodes[mask, 1] = 's12'
    return nodes


# def rule_07(obj_list, i, h, neigh, active, active, active):
#     pass


def rule_08(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's12') 
    nodes[mask, 1] = 's13'
    
    val=np.char.lstrip(nodes[mask, 2].astype(str), 'h').astype(int)

    res= np.where(val==0,1,0)

    res=np.char.add("h",res.astype(str))
    nodes[mask, 2]=res
    
    return nodes
    


def rule_09(nodes, i, h, neigh, active):
    h_active=f'h{active}'
    mask = (nodes[..., 1] == 's13') & (nodes[..., 2] == h_active)
    nodes[mask,1]='s14'

    return nodes



def rule_10(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's13') 
    nodes[mask, 1] = 's34'
    
    return nodes

def rule_11_checker(n_matrix):
    powers= np.array([1,2,4,8,16,32,64,128,256])
    #print(n_matrix[:, 1, 1])
    flat = np.stack([
        n_matrix[:, 1, 1],  # center
        n_matrix[:, 0, 0],  # top-left
        n_matrix[:, 0, 1],  # top-center
        n_matrix[:, 0, 2],  # top-right
        n_matrix[:, 1, 2],  # right
        n_matrix[:, 2, 2],  # bottom-right
        n_matrix[:, 2, 1],  # bottom-center
        n_matrix[:, 2, 0],  # bottom-left
        n_matrix[:, 1, 0],  # left
    ], axis=1)  # Shape: (N, 9)

    # Mask where 'pw' appears
    mask = (flat == 'pw') 
    weighted = mask * powers  # shape: (N, 9)
    values = weighted.sum(axis=1)

    vals = np.isin(values, list(trident))
    return vals

def rule_11(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's14') & (nodes[..., 0] == 'pb') 


    trident_mask=rule_11_checker(neigh[mask])

    check=trident_mask.sum()
    ind1=np.argwhere(mask)
 
    nodes[ind1[trident_mask, 0], ind1[trident_mask, 1],0]='pw'
    nodes[ind1[trident_mask, 0], ind1[trident_mask, 1],1]='s2'


    return nodes ,check
    


# def rule_12(obj_list, i, h, neigh, active):
#    pass


def rule_13(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's14') 
    nodes[mask, 1] = 's12'
    
    return nodes


def rule_14(nodes, i, h, neigh, active):
    mask = (nodes[..., 1] == 's34') 
    nodes[mask, 1] = 's12'
    
    return nodes
