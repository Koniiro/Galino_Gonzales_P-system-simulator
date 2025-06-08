from image_proc_module import image_proc


def quadrant_gen(rawImageData, debug):
    quadrant_raw = [[[], []], [[], []]]
    quadrant = []
    colCoord = [0]
    rowCoord = [0]
    colFinal = len(rawImageData[0]) - 1  # Gets last index for coloumns
    rowFinal = len(rawImageData) - 1  # Gets last index for rows
    colCoord.append(round((colFinal - 1) / 2))
    colCoord.append(round((colFinal - 1) / 2) + 1)
    colCoord.append(colFinal)

    rowCoord.append(round((rowFinal - 1) / 2))
    rowCoord.append(round((rowFinal - 1) / 2) + 1)
    rowCoord.append(rowFinal)
    if debug == 1:
        print("Image Index coord")
        print(colCoord)
        print(rowCoord)

    qRow = 0  # r,c

    for i_r in range(0, len(rawImageData)):
        lSeg = []
        rSeg = []
        if i_r >= rowCoord[2]:
            qRow = 1
        else:
            qRow = 0
        row = rawImageData[i_r]

        for i_c in range(0, len(row)):
            cell = row[i_c]
            if i_c >= colCoord[2]:
                rSeg.append(cell)
            else:
                lSeg.append(cell)
        quadrant_raw[qRow][0].append(lSeg)
        quadrant_raw[qRow][1].append(rSeg)
    quadrant.append(quadrant_raw[0][0])
    quadrant.append(quadrant_raw[0][1])
    quadrant.append(quadrant_raw[1][0])
    quadrant.append(quadrant_raw[1][1])

    return quadrant


if __name__ == "__main__":
    img_route = "4x5_test.png"
    image_path = f"../Input-images/{img_route}"  # Replace with your image path
    # row

    rawImgMat = image_proc(image_path, 0, 0, 50, 0)
    print("Raw Img Nodes:")
    for i in rawImgMat:
        print(i)
    quad_arr = quadrant_gen(rawImgMat, 0)
    print("Quad Array Raw:")
    print(quad_arr)
    print("Quad Array Organized:")
    for i in range(int(len(quad_arr))):
        print(f"Quadrant {i}:")
        print(quad_arr[i])
    print("Quadrant Diagram")
    for i in range(0, len(quad_arr), 2):
        for i_r in range(len(quad_arr[i])):
            print(f"{quad_arr[i][i_r]}||{quad_arr[i + 1][i_r]}")
        print("=========================================")
