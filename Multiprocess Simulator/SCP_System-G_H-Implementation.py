from skeletonizer_module import multi_proc_skeletonization_handler
from image_proc_module import image_proc
from image_recon_module import image_recon
from log_generator import log_maker
import time
import argparse
import os

    # Default values
    # file_name = "LTEST-0015.png"  # Input your image file name
    # threshold = 115  # Midpoint is 128
    # neg = 0  # 1 if negative b/w 0 otherwise
    # log = 1  # 1 if logs to be made

parser = argparse.ArgumentParser()
_ = parser.add_argument("path", help="path of image to skeletonize")
_ = parser.add_argument(
    "-t", "--threshold", help="threshold for binarization. must be 0 to 255", type=int, default=127)
_ = parser.add_argument(
    "-n", "--negative", help="skeletonize the inverse of the image", action="store_true",default=0)
_ = parser.add_argument("-l", "--logging", help="use logging", action="store_true", default=0)
_ = parser.add_argument("-d", "--debug", help="print debugging messages, 1 for yes, 0 for no", type=int, default=0)
_ = parser.add_argument("-bg", "--background", help="background of the image, 1 for white and 0 for black", type=int,default=0)
  
DEBUG=True
if __name__ == "__main__":
    for i in range(1,31):
        if DEBUG:
            args = parser.parse_args([
                f'../medium_image_test/MTEST-{i:04d}.png',  # zero-padded 4 digits
#                 "--threshold", "128",
#                 "--negative",
                "--logging",
                "--debug", "0",
                "--background", "0"
            ])
        else:
            args = parser.parse_args()  # normal CLI usage

        # ===== inputs =====
        round_debug=1
        output_symbol_debug=0
        input_symbol_debug=0
        image_gen_input=[0,0]
        image_save_input=[0,0]

        #==== Checks ====
        assert os.path.isfile(args.path)==1
        assert 0 <= args.threshold <= 255, "Threshold should be in 0-255"
        assert args.debug in (0, 1), "Debug must be 0 or 1"
        assert args.background in (0, 1), "Background must be 0 or 1"
        assert args.negative in (0, 1), "Negative must be 0 or 1"
        assert args.logging in (0, 1), "Logging must be 0 or 1"

        # ======= START =======
        img_name = os.path.basename(args.path)
       
        st = time.time()  # Start Timer
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("=====Starting MPS Skeletonization=====")
        print(f"Starting Time: {current_time}, Threshold: {args.threshold}, Negative: {args.negative}, Img: {img_name}")

        # ===== Choose Input Image =====

        BW_Image = image_proc(args.path, args.background, args.negative, args.threshold, args.debug)
        height=len(BW_Image)
        width=len(BW_Image[0])
        
        # ===== Reconstruct BW Image =====
        if 'output-images' not in os.listdir():
            os.mkdir('output-images')
        save_pathbw = f'output-images/{img_name}-TR{args.threshold}-BW-neg.png' if args.negative else f'output-images/{img_name}-TR{args.threshold}-BW.png'

        image_recon(BW_Image, args.debug, image_gen_input[0], image_save_input[0], save_pathbw)

        # ===== Conduct Skeletonization ====
        output_states, rnd = multi_proc_skeletonization_handler(BW_Image, round_debug,input_symbol_debug,output_symbol_debug, args.debug)

        # ===== Reconstruct SKL Image =====
        save_pathproc: str
        if not args.negative:
            save_pathproc = f'output-images/{img_name}-TR{args.threshold}-SKL-MPS.png'
        else:
            save_pathproc = f'output-images/{img_name}-TR{args.threshold}-SKL-neg-MPS.png' 

        image_recon(output_states, args.debug, image_gen_input[1], image_save_input[1], save_pathproc)


        et = time.time()
        elapsed = et - st
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"End Time: {current_time}")
        print("Execution time:", elapsed, "seconds")

        if args.logging:
            log_maker(
                img_name,
                width,
                height,
                args.threshold,
                st,
                et,
                elapsed,
                rnd,
                args.negative,
            )
