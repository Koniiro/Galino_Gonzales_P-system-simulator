from PIL import Image
import numpy as np


def image_proc(input_path, bg, negative, threshold, debug):
    r_image = Image.open(input_path).convert("RGBA")  # Convert to rgba array
    # preprocess to convert any transparent bg to white
    if bg == 0:  # white background
        mid_image = Image.new("RGB", r_image.size, (255, 255, 255))
    elif bg == 1:  # black background
        mid_image = Image.new("RGB", r_image.size, (0, 0, 0))
    mid_image.paste(r_image, mask=r_image.split()[3])

    bw_image = mid_image.convert("L")
    binary_array = (
        np.array(bw_image) > threshold
    )  # transparent = white, major lines should be black

    # True = white, transparent ; False = Black
    if negative == 0:  # normal view
        binary_array = np.array(binary_array.astype(int), dtype=np.uint8)
    elif negative == 1:  # negative
        binary_array = np.array(binary_array.astype(int), dtype=np.uint8) ^ 1

    if debug == 1:
        print("Binary NP Array")
        print(binary_array)

    holder = []
    for i_x in binary_array:
        temp = []
        for i_y in i_x:
            temp_y = []
            if i_y == 0:
                temp_y.append("pb")
            else:
                temp_y.append("pw")
            temp_y.append("s0")
            temp.append(temp_y)
        holder.append(temp)

    if debug == 1:
        print("SCP System Compatible")
        print(holder)

    return holder


if __name__ == "__main__":
    image_path = f"../Input-images/Pasig_Wordmark.png"  # Replace with your image path
    print(image_proc(image_path, 0, 0, 50, 0))
