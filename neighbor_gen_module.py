from image_proc_module import image_proc
#from quadrant_gen_module import quadrant_gen
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

def neighbor_parse(windows,x,y):
    target=windows[x][y]
    neighbor_array=np.array([target[1][1],target[0][0],target[0][1],target[0][2],target[1][2],target[2][2],target[2][1],target[2][0],target[1][0]])
    
    return neighbor_array

def neighbor_gen(nodes):
   
    flat_nodes = np.ravel(nodes)
    filtered = flat_nodes[np.isin(flat_nodes, ['pw', 'pb'])]
    node_test = filtered.reshape(len(rawImgMat), len(rawImgMat[0]))
  
    padded = np.pad(node_test, pad_width=1, mode='constant', constant_values='pw')
    neighbor_windows = sliding_window_view(padded, (3, 3))
          
   
    return neighbor_windows


if __name__ == "__main__":
    img_route = "4x5_test.png"
    image_path = f"../Input-images/{img_route}"  # Replace with your image path
    rawImgMat = image_proc(image_path, 0, 0, 50, 0)


    start_time = time.time()

    # Run your function
    print("Beginning Neighbor Gen")
    windowed_nodes=neighbor_gen(rawImgMat)



    print(neighbor_parse(windowed_nodes,0,0))
    # End timer
    end_time = time.time()
    
    # Calculate and print elapsed time
    elapsed = end_time - start_time
    quadrant=elapsed/4
    print(f'{len(rawImgMat)},{len(rawImgMat[0])} = {len(rawImgMat[0])*len(rawImgMat)}')
    print(f"Function took {elapsed:.4f} seconds")
    print(f"Quadrants Approx: {quadrant:.4f} seconds")

    print("Neighbor Generation Successful")
