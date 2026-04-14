import moviepy
import moviepy.video.fx as vfx

try:
    from moviepy import VideoFileClip
except ImportError:
    from moviepy.editor import VideoFileClip

def process_video():
    input_file = '/Users/wenyan.xia/热点/AI市集/知识库demo.mov'
    output_file = '/Users/wenyan.xia/热点/AI市集/kb_sliding_demo.mp4'
    clip = VideoFileClip(input_file)
    target_total = 5.0
    speed_factor = clip.duration / target_total
    print(f'Speeding up {clip.duration}s by factor of {speed_factor}')
    fast_clip = clip.with_effects([vfx.MultiplySpeed(speed_factor)])
    fast_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', preset='ultrafast')

if __name__ == '__main__':
    process_video()
