import os
import cv2
from tqdm import tqdm

# image path
im_dir = './screenshots'
# output video path
save_video_dir = './videos'
if not os.path.exists(save_video_dir):
    os.makedirs(save_video_dir)
# set saved fps
fps = 30
# get frames list
frames = sorted(os.listdir(im_dir))
# w,h of image
img = cv2.imread(os.path.join(im_dir, frames[0]))
img_size = (img.shape[1], img.shape[0])
# get seq name
seq_name = os.path.dirname(im_dir).split('/')[-1]

# splice video_dir
video_dir = os.path.join(save_video_dir, frames[0][0:-4] + "-" + frames[-1][0:-4] + '.avi')
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
# also can write like:fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# if want to write .mp4 file, use 'MP4V'
videowriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)

for frame in tqdm(frames):
    f_path = os.path.join(im_dir, frame)
    image = cv2.imread(f_path)
    videowriter.write(image)
    # print(frame + " has been written!")

videowriter.release()
