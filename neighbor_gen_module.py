from image_proc_module import image_proc
from quadrant_gen_module import quadrant_gen
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import time

def neighbor_proc(i, j):
    i= np.array([
        i - 1,  # Upper-left
        i - 1,  # Up
        i - 1,  # Upper-right
        i,  # Right
        i + 1,  # Bottom-right
        i + 1,  # Down
        i + 1,  # Bottom-left
        i,  # Left
    ])
    j=np.array([
         j - 1,  # Upper-left
         j,  # Up
         j + 1,  # Upper-right
         j + 1,  # Right
         j + 1,  # Bottom-right
         j,  # Down
         j - 1,  # Bottom-left
         j - 1,  # Left
    ])
    return i,j


def neighbor_gen_2(window,x,y):
   
#     flat_nodes = np.ravel(nodes)
#     filtered = flat_nodes[np.isin(flat_nodes, ['pw', 'pb'])]
#     node_test = filtered.reshape(len(rawImgMat), len(rawImgMat[0]))
#     padded = np.pad(node_test, pad_width=1, mode='constant', constant_values=np.array('pw'))
#     windows = sliding_window_view(padded, (3, 3))
    target=window[x][y]
    neighbor_array=np.array([target[1][1],target[0][0],target[0][1],target[0][2],target[1][2],target[2][2],target[2][1],target[2][0],target[1][0]])
  
      
   
    return neighbor_array


if __name__ == "__main__":
    img_route = "/irl_test/irl_test-01.jpg"
    image_path = f"../Input-images/{img_route}"  # Replace with your image path
    rawImgMat = image_proc(image_path, 0, 0, 50, 0)
    mask = np.isin(rawImgMat, ['pw', 'pb'])
#     for i_x in rawImgMat:
#         for i_y in i_x:
#             print(i_y,end="")
#         print("")
    rawImgMat = np.array(rawImgMat)
    rawImgMat=rawImgMat.astype(np.str_)

    start_time = time.time()

    # Run your function
    print("Beginning Neighbor Gen")
    flat_nodes = np.ravel(rawImgMat)
    filtered = flat_nodes[np.isin(flat_nodes, ['pw', 'pb'])]
    node_test = filtered.reshape(len(rawImgMat), len(rawImgMat[0]))
    padded = np.pad(node_test, pad_width=1, mode='constant', constant_values=np.array('pw'))
    windows = sliding_window_view(padded, (3, 3))
#     neighbor_nodes = neighbor_gen(
#         rawImgMat,
#         1
#     )  # Neighbor Nodes on per row: [row:[cell-neighbor:[]...],...,row:[]]
    for i_x in range(len(rawImgMat)):
        for i_y in range(len(rawImgMat[0])):
            neighbor_nodes =neighbor_gen_2(windows,i_x,i_y)
    
    # End timer
    end_time = time.time()

    # Calculate and print elapsed time
    elapsed = end_time - start_time
    print(f"Function took {elapsed:.4f} seconds")
   # neighbor_nodes=neighbor_nodes.astype(str)


    

    print("Neighbor Generation Successful")
