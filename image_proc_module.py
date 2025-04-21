from PIL import Image
import numpy as np




def image_proc(input_path,debug,threshold):
    image = Image.open(input_path).convert("L")  # Convert to grayscale
    #threshold = 128  # Midpoint threshold for black/white conversion
    binary_array = np.array(image) < threshold  # True = black, False = white
    binary_array = np.array(binary_array.astype(int), dtype=np.uint8)
    
    if debug==1:
        print("Binary NP Array")
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
        
    if debug==1:    
        print("SCP System Compatible")
        print(holder)
        
    return holder

if __name__ == "__main__":
    image_path = "pine_test.png"  # Replace with your image path
    print(image_proc(image_path,0))

