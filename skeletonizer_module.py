from neighbor_gen_module import neighbor_gen
from image_proc_module import image_proc
from quadrant_gen_module import quadrant_gen

from rule_module import rule_01, rule_02, rule_03, rule_05, rule_06, rule_08, rule_09, rule_10, rule_11, rule_13, rule_14
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
def SCP_Skeletonizer(nodes,verbose,rule_debug):
    active=1
    check=0
    checksum=0
    rnd=1
    # Print Initial Configuration
    if verbose==1:
        print("==Initial Configuration==")
        for x in nodes:
            print(x)
                

    while(True):
        #if verbose==1:
        print(f'Round {rnd}')
        
        for name, func in functions.items():
            if rule_debug==1:
                print(f"Executing {name}:")
            neyb=neighbor_gen(nodes)
            for i_x in range(len(nodes)):
               
                for i_y in range(len(nodes[i_x])):
                    if name=="rule_11":
                        nodes[i_x][i_y],check=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
                        checksum+=check
                        
                    else:
                        nodes[i_x][i_y]=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
                if rule_debug==1:
                    print(nodes[i_x][i_y])
                    print("---------")
            
        if checksum==0: # indicates if rule 11 was run
            break
        checksum=0
        rnd+=1
    print("=====Finished=====")
    print(f'Rounds Taken: {rnd}')
    if verbose==1:
        print("Final Configuration")
    final_arr=[]
    for x in nodes:
        if verbose==1:
            print(x)
        final_arr.append(x)
    return final_arr, rnd

def SCP_Skeletonizer_multithreaded(nodes,verbose,rule_debug):
    active=1
    check=0
    checksum=0
    rnd=1
    # Print Initial Configuration
    if verbose==1:
        print("==Initial Configuration==")
        for x in nodes:
            print(x)
                

    while(True):
        #if verbose==1:
        print(f'Round {rnd}')
        
        for name, func in functions.items():
            if rule_debug==1:
                print(f"Executing {name}:")
            neyb=neighbor_gen(nodes)
            for i_x in range(len(nodes)):
               
                for i_y in range(len(nodes[i_x])):
                    if name=="rule_11":
                        nodes[i_x][i_y],check=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
                        checksum+=check
                        
                    else:
                        nodes[i_x][i_y]=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
                if rule_debug==1:
                    print(nodes[i_x][i_y])
                    print("---------")
            
        if checksum==0:
            break
        checksum=0
        rnd+=1
    print("=====Finished=====")
    print(f'Rounds Taken: {rnd}')
    if verbose==1:
        print("Final Configuration")
    final_arr=[]
    for x in nodes:
        if verbose==1:
            print(x)
        final_arr.append(x)
    return final_arr, rnd

if __name__ == "__main__":
    img_route='4x5_test.png'
    image_path = f'../Input-images/{img_route}'  # Replace with your image path
    
    rawImgMat=image_proc(image_path,0,0,50,0)

    neighbor_nodesRaw=neighbor_gen(rawImgMat)

    neighbor_quad=quadrant_gen(neighbor_nodesRaw,0)
    
    quad_arr=quadrant_gen(rawImgMat,0)
    
        
    for i_r in range(len(quad_arr)):
        for i_c in range(len(quad_arr[i_r][0])):
            print(f'{quad_arr[i_r][0][i_c]} ||| {quad_arr[i_r][1][i_c]}')
        print("==============")

    #quad[row][col][row]
    for i in quad_arr[0][0]:
        print(i)
    for i in neighbor_quad[0][0]:
        print(i)

    #print(neighbor_nodesRaw[0])
