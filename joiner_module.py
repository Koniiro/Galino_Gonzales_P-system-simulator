from image_proc_module import image_proc
from quadrant_gen_module import quadrant_gen, quadrant_print
from neighbor_gen_module import neighbor_gen
import numpy as np


def joiner(node_array):
    recon_matrix = []

    firsthalf = np.concatenate((node_array[0], node_array[2]), axis=0)
    secondhalf = np.concatenate((node_array[1], node_array[3]), axis=0)
    recon_matrix =np.concatenate((firsthalf, secondhalf), axis=1)


    return recon_matrix


if __name__ == "__main__":
    img_route = "4x5_test.png"
    image_path = f"../Input-images/{img_route}"  # Replace with your image path

    rawImgMat = image_proc(image_path, 0, 0, 50, 0)
    for ir in  rawImgMat:
        for i in ir:
            print(i , end=",")
        print("")


    quad_arr = quadrant_gen(rawImgMat, 0)

    quadrant_print(quad_arr)

    joined_matrix = joiner(quad_arr)
    print(f"Joined Matrix: Row:{len(joined_matrix)}, Col: {len(joined_matrix[0])}")
    for ir in  joined_matrix:
        for i in ir:
            print(i , end=",")
        print("")

