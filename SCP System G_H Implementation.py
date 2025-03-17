from rule_module import rule_01, rule_02, rule_03, rule_05, rule_06, rule_08, rule_09, rule_10, rule_11, rule_13, rule_14
from neighbor_gen_module import neighbor_gen
from image_proc_module import image_proc
from image_recon_module import image_recon


#3x3
cross_nodes=[
   [["pw","s0"],["pb","s0"],["pw","s0"]],
   [["pb","s0"],["pb","s0"],["pb","s0"]],
   [["pw","s0"],["pb","s0"],["pw","s0"]]
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



def SCP_Skeletonizer(nodes,verbose):
    active=1
    check=0
    checksum=0
    rnd=1
    # Print Initial Configuration
    print("==Initial Configuration")
    for x in nodes:
       print(x)
        

    while(True):
        if verbose==1:
            print(f'Round {rnd}')
        
        for name, func in functions.items():
            if verbose==1:
                print(f"Executing {name}:")
            neyb=neighbor_gen(nodes)
            for i_x in range(len(nodes)):
               
                for i_y in range(len(nodes[i_x])):
                    if name=="rule_11":
                        nodes[i_x][i_y],check=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
                        checksum+=check
                        
                    else:
                        nodes[i_x][i_y]=func(nodes[i_x][i_y],i_x,i_y,neyb[i_x][i_y],active)
                if verbose==1:
                    print(nodes[i_x][i_y])
                    print("---------")
            
        if checksum==0:
            break
        checksum=0
        rnd+=1
    print("=====Finished=====\nFinal Configuration")
    print(f'Rounds Taken: {rnd}')
    final_arr=[]
    for x in nodes:
        print(x)
        final_arr.append(x)
    return final_arr

# ===== Choose Input Image =====
img_path = "pine_test.png"  # Replace with your image path
test_image=image_proc(img_path,0)
print(test_image)

# ===== Conduct Skeletonization ====
output_states=SCP_Skeletonizer(test_image,0)
print(output_states)

# ===== Reconstruct Image =====
save_path="reconstructed_image.png"
debug=1
image_gen=1
image_save=0
image_recon(output_states,debug,image_gen,image_save,save_path)
   