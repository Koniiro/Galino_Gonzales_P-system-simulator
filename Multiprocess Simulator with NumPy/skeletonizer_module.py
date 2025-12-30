from neighbor_gen_module import neighbor_gen
from image_proc_module import image_proc
from quadrant_gen_module import quadrant_gen
from image_recon_module import image_recon
from joiner_module import joiner
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
import multiprocessing
import time
import numpy as np
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


def multi_proc_skeletonization_handler(nodes, round_debug,input_symbol_debug,output_symbol_debug, verbose):
    multiproc = 1
    rule_debug=0
    checksum = 0
    rnd = 1
    final_arr = []
    temp_arr = []
    node_holder = nodes  # copy over nodes
    quadrant = ["Q1", "Q2", "Q3", "Q4"]
    if multiproc==1:
        print("MPS_NP")
    else:
        print("SPS_NP")
    # Print Initial Configuration
    if input_symbol_debug == 1:
        print("==Initial Configuration==")
        for i in nodes:
            for h in i:
                print(h,end=" ")
            print("")

    while True:
        if round_debug==1:
            print(f"Round {rnd}")  # Print Round Number
        neighbor_nodes = neighbor_gen(node_holder)  # Generate Neighbor Arrays
        neighbor_quad = quadrant_gen(
            neighbor_nodes, 0
        )  # Divide Neighbors into quadrants
        quad_arr = quadrant_gen(node_holder, 0)  # Divide Nodes into quadrants

        if verbose == 1:
            for i in range(0, len(quad_arr), 2):
                for i_r in range(len(quad_arr[i])):
                    print(f"{quad_arr[i][i_r]}||{quad_arr[i + 1][i_r]}")
                print("=========================================")
        checksum = 0
        if multiproc==0:
            temp_arr=mult_proc_skeletonizer(node_holder,neighbor_nodes,"qall",rule_debug)
            checksum+=temp_arr[1]
        else:
            args_list = [(quad_arr[q], neighbor_quad[q], quadrant[q], rule_debug) for q in range(4)]
            with multiprocessing.Pool(processes=4) as pool:
                temp_arr = pool.starmap(mult_proc_skeletonizer, args_list)
            checksums = [x[1] for x in temp_arr]  
            checksum = sum(checksums)
            cleaned_nodes = np.empty(4, dtype=object)
            for i in range(4):
                cleaned_nodes[i] = temp_arr[i][0]

            node_holder = joiner(cleaned_nodes)
 

 
        if checksum == 0:
            break
        checksum = 0
        rnd += 1

    print("=====Finished=====")
    print(f"Rounds Taken: {rnd}")
    if output_symbol_debug == 1:
        print("Final Configuration")
        for x in node_holder:
            if output_symbol_debug == 1:
                print(x)
        #final_arr.append(x)
    return node_holder, rnd


def mult_proc_skeletonizer(nodes, neighbors, label, rule_debug):
    active = 1
    checksum = 0

    for name, func in functions.items():
        if rule_debug == 1:
            print(f"Executing {name}- {label}:")

        if name == "rule_11":
            nodes, check = func(
                nodes, 0, 0, neighbors, active
            )
            checksum += check

        else:
            nodes = func(
                nodes, 0, 0, neighbors, active
            )
            
        if rule_debug == 1:
            for i in nodes:
                for h in i:
                    print(h,end=" ")
                print("")
    return nodes, checksum


if __name__ == "__main__":
    img_route = "4x5_test.png"
    NUM_PROCESSES = 4

    image_path = f"../Input-images/{img_route}"  # Replace with your image path
    rawImgMat = image_proc(image_path, 0, 0, 127, 0)
    #     for i in rawImgMat:
    #         print(i)
    #     for i in neighbor_gen(rawImgMat):
    #         print(i)

    start_time = time.time()
    output_array, rnd = multi_proc_skeletonization_handler(rawImgMat, 0, 0,0,0)
    end_time = time.time()
    elapsed = end_time - start_time
    print(
        f"Finished with {NUM_PROCESSES} processes in {elapsed:.2f} seconds in {rnd} rounds"
    )
    # debug=0
    # image_gen=1
    # image_save=0
    # image_recon(output_array,debug,image_gen,image_save,'')
