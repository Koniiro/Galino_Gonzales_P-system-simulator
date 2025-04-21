from rule_module import rule_01, rule_02, rule_03, rule_05, rule_06, rule_08, rule_09, rule_10, rule_11, rule_13, rule_14
from neighbor_gen_module import neighbor_gen
from image_proc_module import image_proc
from image_recon_module import image_recon
import time
import sys
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
    return final_arr

#===== inputs =====
# command line input: python 
if len(sys.argv)==1:
    file_name="file_name"
    threshold=100 #180 is midpoint
    neg=0
else:
    assert len(sys.argv)==4, "Too many arguments. Arguments are as follows file_name, threshold, negative"
    file_name=sys.argv[1]
    threshold=int(sys.argv[2])
   
    neg=int(sys.argv[3])
assert threshold>=0 or threshold<=255, "Threshold should be fro mthe range 0-255"
assert neg==0 or neg==1, "neg should be either 1 or 0"
img_name=file_name.split(".")[0]


st=time.time()

current_time = time.strftime("%H:%M:%S", time.localtime())
print(f'Starting Time: {current_time}')

# ===== Choose Input Image =====
img_path = f'../Input-images/{file_name}'  # Replace with your image path
debug=0
bg=0

BW_Image=image_proc(img_path,bg,neg,threshold,debug)


# ===== Reconstruct BW Image =====
if neg==0:
    save_pathbw=f'../Output-Images/Ver2/{img_name}-TR{threshold}-BW.png'
elif neg==1: #negative image
    save_pathbw=f'../Output-Images/Ver2/{img_name}-TR{threshold}-BW-neg.png'

debug=0
image_gen=1
image_save=1
image_recon(BW_Image,debug,image_gen,image_save,save_pathbw)

# ===== Conduct Skeletonization ====
output_states=SCP_Skeletonizer(BW_Image,1,0)
#print(output_states)

# ===== Reconstruct SKL Image =====
if neg==0:
    save_pathproc=f'../Output-Images/Ver2/{img_name}-TR{threshold}-SKL.png'
elif neg==1: #negative image
    save_pathproc=f'../Output-Images/Ver2/{img_name}-TR{threshold}-SKL-neg.png'


debug=0
image_gen=1
image_save=1

image_recon(output_states,debug,image_gen,image_save,save_pathproc)
et = time.time()
elapsed=et-st
current_time = time.strftime("%H:%M:%S", time.localtime())
print(f'End Time: {current_time}')
print('Execution time:', elapsed, 'seconds')
