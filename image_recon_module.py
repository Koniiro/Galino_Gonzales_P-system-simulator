from PIL import Image
import numpy as np
from image_proc_module import image_proc
# Example binary data (replace with your actual data)


def image_recon(input_array, debug, image_gen, image_save, save_path):

 
    print(input_array)
    matches = input_array == "pb"      # shape: (5, 4, 2)
    result = np.any(matches, axis=2)
    binary_array=np.where(result==False,1,0)
    binary_array = binary_array.astype(np.uint8)
    
    if debug == 1:
        print("Binary NP Array")
        print(f'Shape: {binary_array.shape}')
        print(binary_array.dtype)
        print(binary_array)
    if image_gen == 1:
        # # Convert 0s (black) and 1s (white) into 255 grayscale values
        image_array = binary_array * 255  # 0 -> 0 (black), 1 -> 255 (white)
        if debug == 1:
            print("Image Array")
            print(image_array)

        # # Create and save the image
        image = Image.fromarray(image_array, mode="L")  # "L" = grayscale mode
        if image_save == 1:
            image.save(save_path)
        image.show()  # Opens the image


if __name__ == "__main__":
    # =======================DEBUG=======================
    test_nodes = [
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pb", "s12", "h0"],
            ["pw", "s2"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pw", "s2"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["s2", "h1", "pw"],
            ["pw", "s2"],
        ],
        [
            ["pw", "s2"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
        ],
        [
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["s2", "h1", "pw"],
            ["pb", "s12", "h1"],
        ],
        [
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
            ["pw", "s2"],
        ],
    ]
    cross_nodes = [
        [["pw", "s2"], ["pb", "s12", "h0"], ["pw", "s2"]],
        [["pb", "s12", "h0"], ["pb", "s12", "h1"], ["pb", "s12", "h0"]],
        [["pw", "s2"], ["pb", "s12", "h0"], ["pw", "s2"]],
    ]

    image_path = f"../Input-images/up_seal.png"  # Replace with your image path
    save_path = f"../Output-Images/test.png"

    # print(image_array)
    debug = 0
    image_array = image_proc(image_path, 0, 1, 127, debug)

    image_gen = 1
    image_save = 0
    image_recon(image_array, 1, image_gen, image_save, save_path)
