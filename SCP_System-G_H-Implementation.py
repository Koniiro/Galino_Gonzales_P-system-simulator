from skeletonizer_module import SCP_Skeletonizer
from image_proc_module import image_proc
from image_recon_module import image_recon
from log_generator import log_maker
import time
import argparse
import os


parser = argparse.ArgumentParser()
_ = parser.add_argument("path", help="path of image to skeletonize")
_ = parser.add_argument(
    "-t", "--threshold", help="threshold for binarization. must be 0 to 255", type=int
)
_ = parser.add_argument(
    "-n", "--negative", help="skeletonize the inverse of the image", action="store_true"
)
args = parser.parse_args()


# ===== inputs =====
if not args.threshold:
    args.threshold = 127

assert 0 <= args.threshold <= 255, "Threshold should be in 0-255"

img_name = os.path.basename(args.path)


st = time.time()

current_time = time.strftime("%H:%M:%S", time.localtime())
print(f"Starting Time: {current_time}")

# ===== Choose Input Image =====
debug = 0
bg = 0
neg = 1 if args.negative else 0

BW_Image = image_proc(args.path, bg, neg, args.threshold, debug)

# ===== Reconstruct BW Image =====
if "output-images" not in os.listdir():
    os.mkdir("output-images")
save_pathbw = (
    f"output-images/{img_name}-TR{args.threshold}-BW.png"
    if neg == 0
    else f"output-images/{img_name}-TR{args.threshold}-BW-neg.png"
)

debug = 0
image_gen = 1
image_save = 0
image_recon(BW_Image, debug, image_gen, image_save, save_pathbw)

# ===== Conduct Skeletonization ====
output_states, rnd = SCP_Skeletonizer(BW_Image, 1, 0)
# print(output_states)

# ===== Reconstruct SKL Image =====
save_pathproc = (
    f"output-images/{img_name}-TR{args.threshold}-SKL.png"
    if neg == 0
    else f"output-images/{img_name}-TR{args.threshold}-SKL-neg.png"
)

debug = 0
image_gen = 1
image_save = 1

image_recon(output_states, debug, image_gen, image_save, save_pathproc)
et = time.time()
elapsed = et - st
current_time = time.strftime("%H:%M:%S", time.localtime())

if "Log_Files" not in os.listdir(".."):
    os.mkdir("../Log_Files")

log_maker(args.path, args.threshold, st, et, elapsed, rnd, neg)
print(f"End Time: {current_time}")
print("Execution time:", elapsed, "seconds")
