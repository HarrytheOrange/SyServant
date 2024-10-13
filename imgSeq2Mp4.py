from moviepy.editor import ImageSequenceClip
import os

pic_dir = "./screenshots"
fps = 30

save_video_dir = './videos'
if not os.path.exists(save_video_dir):
    os.makedirs(save_video_dir)
frames = sorted(os.listdir(pic_dir))
video_dir = os.path.join(save_video_dir, frames[0][0:-4] + "-" + frames[-1][0:-4] + '.mp4')

clip = ImageSequenceClip(pic_dir, fps=fps, with_mask=False, load_images=True)
clip.write_videofile(video_dir, codec="libx264", audio=False)