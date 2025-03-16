from PIL import Image
import numpy as np

image_path = "Test-A.png"  # Replace with your image path
image = Image.open(image_path).convert("L")  # Convert to grayscale


threshold = 128  # Midpoint threshold for black/white conversion
binary_array = np.array(image) < threshold  # True = black, False = white


binary_array = np.array(binary_array.astype(int), dtype=np.uint8)
#3x3
#nodes=[
#    [["pw","s0"],["pb","s0"],["pw","s0"]],
#    [["pb","s0"],["pb","s0"],["pb","s0"]],
#    [["pw","s0"],["pb","s0"],["pw","s0"]]
#    ]
print(binary_array)
holder=[]
for i_x in binary_array:
    temp=[]
    for i_y in i_x:
        temp_y=[]
        if i_y==0:
            temp_y.append("pw")
        else:
            temp_y.append("pb")
        temp_y.append("s0")
        temp.append(temp_y)
    holder.append(temp)
print(holder)
        

# image_array = binary_array*255   # 0 -> 0 (black), 1 -> 255 (white)
# print(image_array.tolist())
# Create and save the image
# image = Image.fromarray(image_array, mode="L")  # "L" = grayscale mode
# image.save("reconstructed_image.png")
# image.show()  # Opens the image