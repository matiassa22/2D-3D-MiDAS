#Script to start ffmpeg extraction and
echo 'ffmpeg extraction'

echo 'Getting Video fps information'
ffmpeg -i video/*.mp4

echo 'extracting Frames'
ffmpeg -i video/BATON.mp4 -r 1/1 example/output%04d.jpg

echo 'Running Stereo generation'
python stereo_generation_image.py

echo 'Combining the output frames together into video'
ffmpeg -framerate 1 -i stereo/MiDaS_3d_output%4d.png output.mp4

