from PIL import Image
import numpy as np

def image_proc(input_path, bg, negative, threshold, debug):
    if debug==1:
        print("(1/5) Opening Image")
    r_image = Image.open(input_path).convert("RGBA")  # Convert to rgba array

    # preprocess to convert any transparent bg to white
    if debug==1:
        print("(2/5) Creating BG")
    if bg == 0:  # white background
        mid_image = Image.new("RGB", r_image.size, (255, 255, 255))
    elif bg == 1:  # black background
        mid_image = Image.new("RGB", r_image.size, (0, 0, 0))
    mid_image.paste(r_image, mask=r_image.split()[3])
    
    if debug==1:
        print("(3/5) Converting to BW")
    bw_image = mid_image.convert("L")
    if debug==1:
        print("(4/5) Thresholding")
    binary_array = (
        np.array(bw_image) > threshold
    )  # transparent = white, major lines should be black

    # True = white, transparent ; False = Black
    if debug==1:
        print("(5/5) Binarizing")
    if negative == 0:  # normal view
        binary_array = np.array(binary_array.astype(int), dtype=np.uint8)
    elif negative == 1:  # negative
        binary_array = np.array(binary_array.astype(int), dtype=np.uint8) ^ 1

    if debug == 1:
        print("Binary NP Array Information")
        print(binary_array)
        print(binary_array.shape)
    

    binary_hold=np.array([["pb","s0","hx"],["pw","s0","hx"]], dtype=object )
    holder = np.array(binary_hold[binary_array], )


    return holder


if __name__ == "__main__":
    image_path = "../Input-images/image.png"  # Replace with your image path
 
    rawImgMat = image_proc(image_path, 0, 0, 50, 1)
    print("=========Output=========")
    print(f'Shape:{rawImgMat.shape}')
    print(rawImgMat)



