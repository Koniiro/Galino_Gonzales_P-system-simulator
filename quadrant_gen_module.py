from image_proc_module import image_proc
import time


def quadrant_gen(rawImageData, debug):
    colFinal = len(rawImageData[0]) - 1  # Gets last index for coloumns
    rowFinal = len(rawImageData) - 1  # Gets last index for rows
    colCoord = [0,round((colFinal - 1) / 2),round((colFinal - 1) / 2) + 1,colFinal]
    rowCoord = [0,round((rowFinal - 1) / 2),round((rowFinal - 1) / 2) + 1,rowFinal]

    if debug == 1:
        print("Image Index coord")
        print(colCoord)
        print(rowCoord)
        row_print(rawImageData)

    q0=rawImageData[:rowCoord[1]+1,:colCoord[1]+1]
    q1=rawImageData[:rowCoord[1]+1,colCoord[2]:,:colCoord[3]+1]
    q2=rawImageData[rowCoord[2]:rowCoord[3]+1,:colCoord[1]+1]
    q3=rawImageData[rowCoord[2]:rowCoord[3]+1,colCoord[2]:,:colCoord[3]+1]
   
    quadrant=[q0,q1,q2,q3]


    return quadrant

def row_print(quad):
    for ir in  quad:
        for i in ir:
            print(i , end=",")
        print("")
def quadrant_print(quad):
    print("Quadrant Diagram")
    for i in range(0, len(quad), 2):
        for i_r in range(len(quad[i])):
            print(f"{quad[i][i_r].tolist()} || {quad[i + 1][i_r].tolist()}")
        print("=========================================")
if __name__ == "__main__":
    img_route = "../medium_image_test/MTEST-0001.png"
    image_path = f"../Input-images/{img_route}"  # Replace with your image path
    debug=0

    rawImgMat = image_proc(image_path, 0, 0, 50, 0)

    st1 = time.time()  # Start Timer
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"Starting Time: {current_time}")

    quad_arr = quadrant_gen(rawImgMat, debug)
    
    et1 = time.time()
    elapsed = et1 - st1
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"End Time: {current_time}")
    print("Execution time:", elapsed, "seconds")
    
    if debug==1:
        print("Quad Array:")
        quadrant_print(quad_arr)
        
    
