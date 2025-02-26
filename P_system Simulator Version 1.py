from rule_module import rule_01, rule_02, rule_03, rule_05, rule_06, rule_08, rule_09, rule_10, rule_11, rule_13, rule_14
from neighbor_gen_module import neighbor_gen

active=1

nodes=[
    [["pb","s0"],["pb","s0"],["pb","s0"]],
    [["pw","s0"],["pb","s0"],["pw","s0"]],
    [["pw","s0"],["pw","s0"],["pw","s0"]]
    ]
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
    "rule_14": rule_14
}



# Print Initial Configuration
for x in nodes:
    print(x)
    

for name, func in functions.items():
    print(f"Executing {name}:")
    neyb=neighbor_gen(nodes)
    for i_x in range(len(nodes)):
       
        for i_y in range(len(nodes[i_x])):
            nodes[i_x][i_y]=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
            print(nodes[i_x][i_y])
       

   