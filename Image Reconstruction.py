from PIL import Image
import numpy as np

# Example binary data (replace with your actual data)



def image_recon(input_array,debug,image_gen):
    holder=[]
    for i_x in input_array:
        temp=[]
        for i_y in i_x:
            
            if 'pw'in i_y:
                temp.append(0)
            elif 'pb' in i_y:
                temp.append(1)
          
            
        holder.append(temp)
    binary_array=np.array(holder, dtype=np.uint8)
    if debug==1:
        print("Binary NP Array")
        print(binary_array)
    if image_gen==1:
        # # Convert 0s (black) and 1s (white) into 255 grayscale values
        image_array = binary_array * 255  # 0 -> 0 (black), 1 -> 255 (white)
        # 
        # # Create and save the image
        image = Image.fromarray(image_array, mode="L")  # "L" = grayscale mode
        image.save("reconstructed_image.png")
        image.show()  # Opens the image
        
nodes=[
[['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2']],
[['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2']],
[['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2']],
[['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pb', 's12', 'h0'], ['pw', 's2'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2']],
[['pw', 's2'], ['pw', 's2'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['pw', 's2'], ['pw', 's2'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['pw', 's2'], ['pw', 's2']],
[['pw', 's2'], ['pw', 's2'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pw', 's2'], ['pw', 's2']],
[['pw', 's2'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pw', 's2'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw'], ['pw', 's2']],
[['pw', 's2'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pb', 's12', 'h1'], ['pw', 's2']],
[['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['s2', 'h1', 'pw'], ['pb', 's12', 'h1']],
[['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2'], ['pw', 's2']]
]
image_recon(nodes,1,0)