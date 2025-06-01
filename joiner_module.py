from image_proc_module import image_proc
from quadrant_gen_module import quadrant_gen
from neighbor_gen_module import neighbor_gen

def joiner(node_array):
    recon_matrix=[]
    for i in range(0,len(node_array),2):
        for i_r in range(len(node_array[i])):
            dump_1=node_array[i][i_r]+node_array[i+1][i_r]
            recon_matrix.append(dump_1)

    return recon_matrix

if __name__ == "__main__":
    img_route='4x5_test.png'
    image_path = f'../Input-images/{img_route}'  # Replace with your image path
    
    rawImgMat=image_proc(image_path,0,0,50,0)

    neighbor_nodesRaw=neighbor_gen(rawImgMat) # Neighbor Nodes on per row: [row:[cell-neighbor:[]...],...,row:[]]

    neighbor_quad=quadrant_gen(neighbor_nodesRaw,0)
    
    quad_arr=quadrant_gen(rawImgMat,0)    
    
    print("Quadrant Diagram")
    for i in range(0,len(quad_arr),2):
        for i_r in range(len(quad_arr[i])):
            print(f'{quad_arr[i][i_r]}||{quad_arr[i+1][i_r]}')
        print("=========================================")

    joined_matrix= joiner(quad_arr)
    print(f'Joined Matrix: {len(joined_matrix)}, Col: {len(joined_matrix[0])}')
    for i_quadr in range(len(neighbor_quad)):
        print(f'Quad {i_quadr} Rows:')
        print(f'Rows: {len(neighbor_quad[i_quadr])}; Cols: {len(neighbor_quad[i_quadr][0])}')
        for i_quadc in neighbor_quad[i_quadr]:
            print(i_quadc)
    
    joined_neighbor_mtrx = joiner(neighbor_quad)
    print(f'Joined Neighbor Matrix: {len(joined_neighbor_mtrx)}, Col: {len(joined_neighbor_mtrx[0])}')
