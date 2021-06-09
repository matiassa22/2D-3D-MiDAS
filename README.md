## 2D-3D-MiDAS
2D to 3D Video Conversion using Deep Learning based on Depth Estimation Methodologies

## Setup & installation:
    *  Download the model weights from https://drive.google.com/file/d/1l_w6Jny_erNQpgc8-nzBa_adh4bBDaFw/view?usp=sharing
       and place in root folder
    * Install the corresopnding anaconda for 
      your system: windows, linux or mac
    * Refer to my installation and how tips on how to run and install nvidia
      driver on ubuntu: 
      For windows here: https://docs.nvidia.com/gameworks/content/developertools/desktop/install_nvidia_display_driver.htm

    * Dependencies: pip install -r requirements.txt
    * pip install pytorch
    * pip install torchvision
    * pip install opencv_python

## Usage
   1) Place videos in video folder
      * example: Bad_Boys_Porsche_13_with_audio.mp4
       
   2) Run: ffmpeg -i video/Bad_Boys_Porsche_13_with_audio.mp4 example/Bad_Boys_Porsche_13%04d.jpg
   3) Place input images in the folder 'example' 
      
   4) RUN: python stereo_generation_image.py 
      
   5) Extract audio file from original video:
      * ffmpeg -i video/Bad_Boys_Porsche_13_with_audio.mp4 -f mp3 Bad_Boys_Porsche_13_with_audio.mp3
      
   6) Compose frames and extracted audio 
      ffmpeg -framerate -i stereo/*.png -i Bad_Boys_Porsche_13_with_audio.mp3 video/Bad_Boys_Porsche_13_with_audio.mp4
        
## Further improvements:
   *  TODO: Rewrite pipeline for multithreading and enhanced inference on GPUs. 
   * 


## Optional: 
   * (Generate Depth map from image)
     * python depth_estimate_image.py
       (MiDas Network)
           
     * (Generate Depth map from camera)
          python depth_estimate_cam.py

