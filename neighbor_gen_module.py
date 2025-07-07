from image_proc_module import image_proc
#from quadrant_gen_module import quadrant_gen
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import time


def neighbor_parse(windows,x,y):
    target=windows[x][y]
    neighbor_array=np.array([target[1][1],target[0][0],target[0][1],target[0][2],target[1][2],target[2][2],target[2][1],target[2][0],target[1][0]])
    
    return neighbor_array

def neighbor_gen(nodes):
    
    flat_nodes = np.ravel(nodes)
    filtered = flat_nodes[np.isin(flat_nodes, ['pw', 'pb'])]
    
    rows, cols,underhood = nodes.shape

    node_test = filtered.reshape(rows, cols)
  
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

    

    print(neighbor_parse(windowed_nodes,2,2))
    # End timer
    end_time = time.time()

    
    # Calculate and print elapsed time
    elapsed = end_time - start_time
    quadrant=elapsed/4
    print(f'{len(rawImgMat)},{len(rawImgMat[0])} = {len(rawImgMat[0])*len(rawImgMat)}')
    print(f"Function took {elapsed:.4f} seconds")
    print(f"Quadrants Approx: {quadrant:.4f} seconds")

    print("Neighbor Generation Successful")
