from image_proc_module import image_proc

def quadrant_gen(rawImageData, debug):
    quadrant=[[[],[]],[[],[]]]
    
    colCoord=[0]
    rowCoord=[0]
    colFinal=len(rawImageData[0])-1 # Gets last index for coloumns
    rowFinal=len(rawImageData)-1 # Gets last index for rows
    colCoord.append(round((colFinal-1)/2))
    colCoord.append(round((colFinal-1)/2)+1)
    colCoord.append(colFinal)
    
    rowCoord.append(round((rowFinal-1)/2))
    rowCoord.append(round((rowFinal-1)/2)+1)
    rowCoord.append(rowFinal)
    if debug==1:
        print("Image Index coord")
        print(colCoord)
        print(rowCoord)
    
    qRow=0 #r,c

        
    for i_r in range(0,len(rawImageData)):
        lSeg=[]
        rSeg=[]
        if i_r>=rowCoord[2]:
            qRow=1
        else:
            qRow=0
        row=rawImageData[i_r]

        for i_c in range(0,len(row)):
            cell=row[i_c]
            if i_c>=colCoord[2]:
                rSeg.append(cell)
            else:
                lSeg.append(cell)
        quadrant[qRow][0].append(lSeg)
        quadrant[qRow][1].append(rSeg)

    return quadrant

if __name__ == "__main__":
    img_route='4x5_test.png'
    image_path = f'../Input-images/{img_route}'  # Replace with your image path
    # row
    
    rawImgMat=image_proc(image_path,0,0,50,0)
    for i in rawImgMat:
        print(i)
    quad_arr=quadrant_gen(rawImgMat,0)
    for i_r in range(len(quad_arr)):
        for i_c in range(len(quad_arr[i_r][0])):
            print(f'{quad_arr[i_r][0][i_c]} ||| {quad_arr[i_r][1][i_c]}')
        print("==============")
