'''
takes in img_directory
and half all the imgs inside it.
'''

import os
import cv2

def half_res_img(input_dir):
    dsize = (1920,1080)
    for img in os.listdir(input_dir):
        if 'MiDaS_Bad_Boys_Porsche_' in img and '3d' not in img:
            frame = cv2.imread(img)
            half_img = cv2.resize(frame,dsize)
            cv2.imwrite(os.path.join(stereo,half_img) + 'half_res')

if __name__ == "__main__":
    input_dir = 'stereo/'
    half_res_img(input_dir)
