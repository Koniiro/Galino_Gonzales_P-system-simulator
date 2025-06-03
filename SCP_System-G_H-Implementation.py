from skeletonizer_module import multi_proc_skeletonization_handler
from image_proc_module import image_proc
from image_recon_module import image_recon
from log_generator import log_maker
import time
import sys

if __name__ == "__main__":
    # Default values
    file_name = "Pasig_City_Seal_Logo.png"  # Input your image file name
    threshold = 127  						# Midpoint is 128
    neg = 0									# 1 if negative b/w 0 otherwise
    multiproc=1 							# 1 if multiprocess 0 otherwise
    log=0 									# 1 if logs to be made
    
    img_path = f'../Input-images/{file_name}'  # Replace with your image path

    debug=0
    bg=0 #1: White BG; 0:Black BG
    #===== inputs =====
    # command line input: python
    # image_path;theshold;negative;log
    if len(sys.argv) > 1:
        if len(sys.argv) != 5:
            print("Usage: python script.py <file_name> <threshold> <negative>")
            sys.exit(1)
        
        file_name = sys.argv[1]
        
        try:
            threshold = int(sys.argv[2])
            neg = int(sys.argv[3])
            log = int(sys.argv[4])
        except ValueError:
            print("Error: threshold and negative must be integers.")
            sys.exit(1)
    assert threshold>=0 or threshold<=255, "threshold should be fro mthe range 0-255"
    assert neg==0 or neg==1, "neg value should be either 1 or 0"
    assert log==0 or log==1, "log value should be either 1 or 0"

    img_name=file_name.split(".")[0]

    st=time.time() # Start Timer
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f'Starting Time: {current_time}')

    # ===== Choose Input Image =====
    
    BW_Image=image_proc(img_path,bg,neg,threshold,debug)


    # ===== Reconstruct BW Image =====
    if neg==0:
        save_pathbw=f'../Output-Images/Ver2/{img_name}-TR{threshold}-BW.png'
    elif neg==1: #negative image
        save_pathbw=f'../Output-Images/Ver2/{img_name}-TR{threshold}-BW-neg.png'

    debug_recon=0
    image_gen=1  #1: Generate an Image; 0 otherwise 
    image_save=0 #1: Save Image to path; 0 otherwise 
    image_recon(BW_Image,debug,image_gen,image_save,save_pathbw)

    # ===== Conduct Skeletonization ====
    if multiproc==1:
        output_states,rnd =multi_proc_skeletonization_handler(BW_Image,0,0)


    # ===== Reconstruct SKL Image =====
    if neg==0:
        if multiproc==1:
            save_pathproc=f'../Output-Images/Ver2/{img_name}-TR{threshold}-SKL-multiproc.png'
        else:
            save_pathproc=f'../Output-Images/Ver2/{img_name}-TR{threshold}-SKL.png'
    elif neg==1: #negative image
        if multiproc==1:
            save_pathproc=f'../Output-Images/Ver2/{img_name}-TR{threshold}-SKL-neg-multiproc.png'
        else:
            save_pathproc=f'../Output-Images/Ver2/{img_name}-TR{threshold}-SKL-neg.png'
            
    image_recon(output_states,debug_recon,image_gen,image_save,save_pathproc)
    
    et = time.time()
    elapsed=et-st
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f'End Time: {current_time}')
    print('Execution time:', elapsed, 'seconds')

    if log==1:
        log_maker(file_name,threshold,st,et,elapsed,rnd,neg,multiproc)
