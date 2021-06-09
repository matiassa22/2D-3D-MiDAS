#Script to half the resolution of the 3D film
'''
takes in video
'''

import cv2

'''
input_dir: string expected: 
'''
def half_resolution_video(input_dir):
    half_vid_name = input_dir.split('/')[-1]
    cap = cv2.VideoCapture(input_dir)
    idx = 0

    #Create the output writer
    #dsize = (frame.size(0), frame.size(1) // 2, frame.size[] - 1)
    dsize=(1920,1080)
    output_video = cv2.VideoWriter('half_res'+half_vid_name,cv2.VideoWriter_fourcc(*'DIVX'), 24, dsize)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        #Half the resolution here, dsize is destination_size
        half_frame = cv2.resize(frame,dsize)
        output_video.write(half_frame)

    #Get name of video




if __name__ == "__main__":
    input_dir = 'video/Bad_Boys_Porsche_13_with_audio.mp4'
    half_resolution_video(input_dir)
