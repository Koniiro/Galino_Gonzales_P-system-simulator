from image_proc_module import image_proc
from quadrant_gen_module import quadrant_gen

def neighbor_proc(i,j):
    return  [
        (i-1, j-1),  # Upper-left
        (i-1, j),    # Up
        (i-1, j+1),  # Upper-right
        (i, j+1),    # Right
        (i+1, j+1),  # Bottom-right
        (i+1, j),    # Down
        (i+1, j-1),  # Bottom-left
        (i, j-1)     # Left
    ]

def neighbor_gen(nodes):
    temp_holder=[]
    
    for i_x in range(len(nodes)):
        row=[]
        for i_y in range(len(nodes[i_x])):
            hold=[]
            if "pb" in nodes[i_x][i_y]:
                hold.append("pb")
            elif "pw" in nodes[i_x][i_y]:
                hold.append("pw")
            loc_neigh= neighbor_proc(i_x,i_y)
            #print(f'processing ({i_x},{i_y})')
            for x,y in loc_neigh:
                if x <0 or y <0 or x > len(nodes)-1 or y > len(nodes[0])-1:
                    hold.append("pw")
                else:
                    if "pb" in nodes[x][y]:
                        hold.append("pb")
                    elif "pw" in nodes[x][y]:
                        hold.append("pw")
            #hold.append(f'{i_x},{i_y}')
            row.append(hold)
        temp_holder.append(row)
   
    return temp_holder

    
if __name__ == "__main__":
    img_route='4x5_test.png'
    image_path = f'../Input-images/{img_route}'  # Replace with your image path
    
    rawImgMat=image_proc(image_path,0,0,50,0)

    neighbor_nodesRaw=neighbor_gen(rawImgMat)

    neighbor_quad=quadrant_gen(neighbor_nodesRaw,0)
    
    quad_arr=quadrant_gen(rawImgMat,0)
    
        
    for i_r in range(len(quad_arr)):
        for i_c in range(len(quad_arr[i_r][0])):
            print(f'{quad_arr[i_r][0][i_c]} ||| {quad_arr[i_r][1][i_c]}')
        print("==============")


    for i in quad_arr[1][0]:
        print(i)
    for i in neighbor_quad[1][0]:
        print(i)
    print(neighbor_quad[1][0])