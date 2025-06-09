from skeletonizer_module import multi_proc_skeletonization_handler
from image_proc_module import image_proc
from image_recon_module import image_recon
from log_generator import log_maker
import time
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("path", help="path of image to skeletonize")
    _ = parser.add_argument(
    "-t", "--threshold", help="threshold for binarization. must be 0 to 255", type=int
    )
    _ = parser.add_argument(
        "-n", "--negative", help="skeletonize the inverse of the image", action="store_true"
    )
    _ = parser.add_argument("-m", "--multiproc", help="use multiprocessing", action="store_true")
    _ = parser.add_argument("-l", "--logging", help="use logging", action="store_true")
    _ = parser.add_argument("-d", "--debug", help="print debugging messages, 1 for yes, 0 for no", type=int)
    _ = parser.add_argument("-bg", "--background", help="background of the image, 1 for white and 0 for black", type=int)
    args = parser.parse_args()
    # Default values
    # file_name = "LTEST-0015.png"  # Input your image file name
    # threshold = 115  # Midpoint is 128
    # neg = 0  # 1 if negative b/w 0 otherwise
    # multiproc = 1  # 1 if multiprocess 0 otherwise
    # log = 1  # 1 if logs to be made


    # debug = 0
    if not args.debug:
        args.debug = 0
    
    # bg = 0  # 1: White BG; 0:Black BG
    if not args.background:
        args.background = 0

    assert 0 <= args.threshold <= 255, "Threshold should be in 0-255"

    img_name = os.path.basename(args.path)

    st = time.time()  # Start Timer
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"Starting Time: {current_time}")

    # ===== Choose Input Image =====

    BW_Image = image_proc(args.path, args.background, args.negative, args.threshold, args.debug)

    # ===== Reconstruct BW Image =====
    if 'output-images' not in os.listdir():
        os.mkdir('output-images')
    save_pathbw = f'output-images/{img_name}-TR{args.threshold}-BW-neg.png' if args.negative else f'output-images/{img_name}-TR{args.threshold}-BW.png'

    debug_recon = 0
    image_gen = 1  # 1: Generate an Image; 0 otherwise
    image_save = 1  # 1: Save Image to path; 0 otherwise
    image_recon(BW_Image, args.debug, image_gen, image_save, save_pathbw)

    # ===== Conduct Skeletonization ====
    output_states, rnd = multi_proc_skeletonization_handler(BW_Image, 0, 0)

    # ===== Reconstruct SKL Image =====
    save_pathproc: str
    if not args.negative:
        save_pathproc = f'output-images/{img_name}-TR{args.threshold}-SKL-multiproc.png'
    else:
        save_pathproc = f'output-images/{img_name}-TR{args.threshold}-SKL-neg-multiproc.png' 

    image_recon(output_states, debug_recon, image_gen, image_save, save_pathproc)
    length = len(output_states)
    width = len(output_states[0])
    pixel_count = length * width
    et = time.time()
    elapsed = et - st
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"End Time: {current_time}")
    print("Execution time:", elapsed, "seconds")

    if args.logging:
    # if log == 1:
        log_maker(
            args.path,
            args.threshold,
            st,
            et,
            elapsed,
            rnd,
            args.negative,
            args.multiproc,
            length,
            width,
            pixel_count,
        )
