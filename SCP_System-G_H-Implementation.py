from skeletonizer_module import SCP_Skeletonizer
from image_proc_module import image_proc
from image_recon_module import image_recon
from log_generator import log_maker
import time
import sys


# Default values
file_name = "skl_test.png"
threshold = 127  # Midpoint is 128
neg = 0
#===== inputs =====
# command line input: python 
if len(sys.argv) > 1:
    if len(sys.argv) != 4:
        print("Usage: python script.py <file_name> <threshold> <negative>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    
    try:
        threshold = int(sys.argv[2])
        neg = int(sys.argv[3])
    except ValueError:
        print("Error: threshold and negative must be integers.")
        sys.exit(1)
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
output_states,rnd =SCP_Skeletonizer(BW_Image,1,0)
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
log_maker(file_name,threshold,st,et,elapsed,rnd,neg)
print(f'End Time: {current_time}')
print('Execution time:', elapsed, 'seconds')
